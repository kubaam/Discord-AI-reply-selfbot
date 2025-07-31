import json
import random
import asyncio
import re
import discord
import openai

with open("config.json") as f:
    cfg = json.load(f)

TOKEN = cfg["token"]
GUILD_ID = cfg["guild_id"]
CHANNEL_ID = cfg["channel_id"]
OPENAI_API_KEY = cfg["openai_key"]
BLACKLIST = cfg["blacklist"]

openai.api_key = OPENAI_API_KEY

client = discord.Client(self_bot=True)
message_queue: asyncio.Queue[discord.Message] = asyncio.Queue(maxsize=1)

async def send_with_retry(channel: discord.abc.Messageable, text: str, retries: int = 1, delay: float = 10.0) -> None:
    """Send a message with a simple retry mechanism."""
    for attempt in range(retries + 1):
        try:
            await channel.send(text)
            return
        except discord.HTTPException as exc:
            if attempt < retries:
                print(f"[⚠️] Send failed, retrying in {delay}s: {exc}")
                await asyncio.sleep(delay)
            else:
                print(f"[❌] Couldn't send message after retry: {exc}")

async def process_queue() -> None:
    while True:
        message = await message_queue.get()
        lower_msg = message.content.lower()
        if "who receive big drop" in lower_msg or "who received big drop" in lower_msg:
            await asyncio.sleep(random.uniform(0.5, 2.0))
            await send_with_retry(message.channel, "OF COURSE YOU BRO!!!")
        else:
            reply = await generate_reply(message.content)
            await asyncio.sleep(random.uniform(15.5, 120.0))
            await send_with_retry(message.channel, reply)
        message_queue.task_done()


@client.event
async def on_ready():
    print(f"[✅] Logged in as {client.user}")
    client.loop.create_task(process_queue())

def is_blacklisted(text: str) -> bool:
    """Check if any blacklist word is present in the text."""
    return any(bad.lower() in text.lower() for bad in BLACKLIST)

def contains_real_words(text: str) -> bool:
    """Return True if the text contains at least one real-looking word."""
    # Ignore typical links
    if re.search(r"https?://|www\.\S+|\.[a-z]{2,3}/?", text, re.IGNORECASE):
        return False

    # Look for tokens with letters and at least one vowel
    for token in re.findall(r"[A-Za-z]{2,}", text):
        if re.search(r"[aeiouAEIOU]", token):
            return True
    return False

async def generate_reply(msg: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Counter-Strike 2 gamer chatting casually. "
                        "You're friendly but sometimes sarcastic and a little wild. "
                        "Keep replies short and never mention that you are an AI."
                        "Only reply with short no effort max 10 words messsages."
                        "Implement gen Z slang like idk omg etc.."
                        "Act like human with all human feelings"
                    )
                },
                {"role": "user", "content": msg},
            ],
            max_tokens=120,
            temperature=0.9,
        )
        reply = response["choices"][0]["message"]["content"].strip()
        return reply
    except Exception as exc:
        print(f"[❌] Error: {exc}")
        return "Sorry, I couldn't come up with a reply."

@client.event
async def on_message(message: discord.Message):
    if message.author.id == client.user.id:
        return
    if message.guild is None or message.guild.id != GUILD_ID:
        return
    if message.channel.id != CHANNEL_ID:
        return
    if is_blacklisted(message.content):
        print("[⚠️] Skipped blacklisted message")
        return
    if not contains_real_words(message.content):
        print("[⚠️] Skipped message with no real words")
        return

    print(f"[📩] {message.author.display_name}: {message.content}")
    if message_queue.full():
        print("[⚠️] Queue full, ignoring new message")
        return
    await message_queue.put(message)
client.run(TOKEN)
