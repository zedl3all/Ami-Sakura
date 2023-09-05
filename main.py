"""Bot Discord"""
import json
import time
import discord
import genword


def gettoken():
    """GetToken"""
    with open('Token.json', "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["tokenBotdiscord"]

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
channel_id = 1148255715937505360

@client.event
async def on_ready():
    """Start Bot"""
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(channel_id)
    await channel.send("Bot is Online")
    #while True:
    #    await channel.send(genword.generate())
    #    time.sleep(60)
@client.event
async def on_message(message):
    """send message"""
    if message.author == client.user:
        return
    if message.content == '!TEST':
        try:
            randomword = genword.generate()
            time.sleep(5)
            await message.author.send(embed = discord.Embed(title = randomword))
        except discord.HTTPException: # Ignoring exception in on_message
            await message.author.send("กรุณาลองใหม่")

client.run(gettoken())
