import discord
import random

TOKEN = "MTUyNzg3MzcwNTMxNTY2ODAzMQ.G_0jq-.iBlDXVv-skbeef6mBFEae-aN3smUGBD15dBDHA"
WELCOME_CHANNEL_ID = 1527871481227378752

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
