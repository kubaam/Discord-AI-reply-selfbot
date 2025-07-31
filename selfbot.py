import discord
import openai
import json
import random
import asyncio

with open("config.json") as f:
    cfg = json.load(f)

TOKEN = cfg["token"]
GUILD_ID = cfg["guild_id"]
CHANNEL_ID = cfg["channel_id"]
OPENAI_API_KEY = cfg["openai_key"]
BLACKLIST = cfg["blacklist"]

openai.api_key = OPENAI_API_KEY


client = discord.Client(self_bot=True)

crazy_openers = [
    "Bro I'm built diff 💀:",
    "Yooo no cap this is wild af 👉😳:",
    "Okay but hear me out 💡🔥:",
    "Sigma take incoming 🚨:",
    "Deadass? Lemme cook 👨‍🍳:"
]

@client.event
async def on_ready():
    print(f"[✅] Logged in as {client.user} — Ready to RIZZ up in CS2 style 💣")

def is_blacklisted(text):
    return any(bad.lower() in text.lower() for bad in BLACKLIST)

async def generate_reply(msg):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cracked Gen Z CS2 pro player who speaks in gamer slang and zoomer memes. Respond short, chaotic, but genius."},
                {"role": "user", "content": msg}
            ],
            max_tokens=120,
            temperature=1
        )
        reply = response['choices'][0]['message']['content'].strip()
        opener = random.choice(crazy_openers)
        return f"{opener} {reply}"
    except Exception as e:
        print(f"[❌] Error: {e}")
        return "Bro I'm lagging rn 😵, can't even reply..."

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    if message.guild is None or message.guild.id != GUILD_ID:
        return
    if message.channel.id != CHANNEL_ID:
        return
    if is_blacklisted(message.content):
        print(f"[⚠️] Skipped message: blacklisted word found")
        return

    print(f"[📩] {message.author.display_name}: {message.content}")
    reply = await generate_reply(message.content)
    await message.channel.send(reply)

client.run(TOKEN)
import discord
import openai
import json
import random
import asyncio

with open("config.json") as f:
    cfg = json.load(f)

TOKEN = cfg["token"]
GUILD_ID = cfg["guild_id"]
CHANNEL_ID = cfg["channel_id"]
OPENAI_API_KEY = cfg["openai_key"]
BLACKLIST = cfg["blacklist"]

openai.api_key = OPENAI_API_KEY


client = discord.Client(self_bot=True)

crazy_openers = [
    "Bro I'm built diff 💀:",
    "Yooo no cap this is wild af 👉😳:",
    "Okay but hear me out 💡🔥:",
    "Sigma take incoming 🚨:",
    "Deadass? Lemme cook 👨‍🍳:"
]

@client.event
async def on_ready():
    print(f"[✅] Logged in as {client.user} — Ready to RIZZ up in CS2 style 💣")

def is_blacklisted(text):
    return any(bad.lower() in text.lower() for bad in BLACKLIST)

async def generate_reply(msg):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cracked Gen Z CS2 pro player who speaks in gamer slang and zoomer memes. Respond short, chaotic, but genius."},
                {"role": "user", "content": msg}
            ],
            max_tokens=120,
            temperature=1
        )
        reply = response['choices'][0]['message']['content'].strip()
        opener = random.choice(crazy_openers)
        return f"{opener} {reply}"
    except Exception as e:
        print(f"[❌] Error: {e}")
        return "Bro I'm lagging rn 😵, can't even reply..."

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    if message.guild is None or message.guild.id != GUILD_ID:
        return
    if message.channel.id != CHANNEL_ID:
        return
    if is_blacklisted(message.content):
        print(f"[⚠️] Skipped message: blacklisted word found")
        return

    print(f"[📩] {message.author.display_name}: {message.content}")
    reply = await generate_reply(message.content)
    await message.channel.send(reply)

client.run(TOKEN)
