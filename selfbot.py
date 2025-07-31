import json
import random
import asyncio
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


@client.event
async def on_ready():
    print(f"[✅] Logged in as {client.user}")

def is_blacklisted(text: str) -> bool:
    """Check if any blacklist word is present in the text."""
    return any(bad.lower() in text.lower() for bad in BLACKLIST)

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
                        "Only reply with short no effort max 5 words messsages."
                        "Implement gen Z slang like idk etc atd.."
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

    print(f"[📩] {message.author.display_name}: {message.content}")
    lower_msg = message.content.lower()
    if "who receive big drop" in lower_msg or "who received big drop" in lower_msg:
        await asyncio.sleep(random.uniform(0.5, 2.0))
        await message.channel.send("OF COURSE YOU BRO!!!")
        return
    reply = await generate_reply(message.content)
    await asyncio.sleep(random.uniform(15.5, 120.0))
    await message.channel.send(reply)
client.run(TOKEN)
