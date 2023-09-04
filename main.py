"""Bot Discord"""
import json
import discord
from discord.ext import tasks
import time
import genword


def gettoken():
    """GetToken"""
    with open("token.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["tokenBotdiscord"]

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
canloop = False
channel_id = 1148255715937505360

@client.event
async def on_ready():
    """Start Bot"""
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(channel_id)
    await channel.send("Bot is Online")
    while True:
        await channel.send(genword.generate())
        time.sleep(60)


client.run(gettoken())
