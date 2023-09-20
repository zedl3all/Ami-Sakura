"""Bot Discord"""
import json
import time
import discord
import genword
import viewlog
import LinkDataBase
from discord.ext import commands

@viewlog.log_return_value
def gettoken():
    """GetToken"""
    with open('Token.json', "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["tokenBotdiscord"]

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
channel_id = 1148255715937505360
messagesend = False

@viewlog.log_return_value
@client.event
async def on_ready():
    """Start Bot"""
    print(f'{client.user} has connected to Discord!')
    #channel = client.get_channel(channel_id)
    user = await client.fetch_user(307804872408039424)
    await user.send("Bot is Online")
    #await channel.send("Bot is Online")

@viewlog.log_return_value
@client.event
async def on_message(message):
    """send message"""
    global messagesend
    if message.author == client.user:
        return
    if message.content == '!play' or message.content == '!p':
        try:
            randomword = genword.generate()
            time.sleep(5)
            await message.author.send(embed = discord.Embed(title = randomword))
            messagesend = True
        except discord.HTTPException: # Ignoring exception in on_message
            await message.author.send("กรุณาลองใหม่")
    if messagesend is True:
        if '!say' in message.content:
            text_to_say = message.content.replace('!say ', '')
            await message.author.send(text_to_say+" "+"ขอบคุณที่ตอบค่ะ")
            messagesend = False
    if message.content == '!create':
        user_id = message.author.id
        if not message.author.bot:
            if LinkDataBase.check_data(user_id) is True:
                await message.author.send("คุณมีรหัสอยู่แล้ว")
            else:
                LinkDataBase.add_data(user_id)
                await message.author.send("คุณได้สร้างรหัสแล้ว")

client.run(gettoken())
