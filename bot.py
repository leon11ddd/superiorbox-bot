import discord
import os
import sys
import random

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
WELCOME_CHANNEL_ID_RAW = os.environ.get("WELCOME_CHANNEL_ID")

if not TOKEN:
    print("ERROR: DISCORD_BOT_TOKEN environment variable is not set.", file=sys.stderr)
    sys.exit(1)

if not WELCOME_CHANNEL_ID_RAW:
    print("ERROR: WELCOME_CHANNEL_ID environment variable is not set.", file=sys.stderr)
    sys.exit(1)

try:
    WELCOME_CHANNEL_ID = int(WELCOME_CHANNEL_ID_RAW)
except ValueError:
    print(f"ERROR: WELCOME_CHANNEL_ID must be a number, got: {WELCOME_CHANNEL_ID_RAW}", file=sys.stderr)
    sys.exit(1)

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="SuperiorBox"))
    print(f"✅ Bot is online as {client.user} (ID: {client.user.id})")

@client.event
async def on_member_join(member: discord.Member):
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        return
    embed = discord.Embed(
        title=f"Добро пожаловать на {member.guild.name}! 🎉",
        description=(f"Привет, {member.mention}, рады тебя видеть!\n\nНе стесняйся представиться и изучить сервер."),
        color=discord.Color.from_rgb(255, random.randint(80, 200), 0),
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text=f"Участник #{member.guild.member_count}")
    await channel.send(embed=embed)

client.run(TOKEN)
