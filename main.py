"""Bot Discord"""
import json
import time
from datetime import datetime
import discord
from discord.ext import tasks
import genword
import viewlog
import LinkDataBase as LD
import AIcheckgb


@viewlog.log_return_value
def gettoken():
    """GetToken"""
    with open('Token.json', "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["tokenBotdiscord"]

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@tasks.loop(seconds=30)
async def slow_count():
    """slow_count"""
    if LD.get_userid_by_online() is not None:
        for user_id in LD.get_userid_by_online():
            #print(user_id)
            if int(LD.get_time(user_id)[:2]) < int(datetime.now().hour):
                user = await client.fetch_user(user_id)
                if LD.check_data(user_id) is False:
                    await user.send("กรุณาสร้าง data ก่อน !Create เพื่อสร้าง")
                else:
                    try:
                        randomword = genword.generate()
                        time.sleep(5)
                        await user.send(embed = discord.Embed(title = randomword, color = 0xeea3f9))
                        LD.update_waiting_message(user_id, True)
                        LD.update_time(user_id, datetime.now())
                    except discord.HTTPException: # Ignoring exception in on_message
                        await user.send("ขอเวลาแปป")
    print("Check")

@viewlog.log_return_value
@client.event
async def on_ready():
    """Start Bot"""
    print(f'{client.user} has connected to Discord!')
    user = await client.fetch_user(307804872408039424)
    await user.send("Bot is Online")
    if not slow_count.is_running():
        slow_count.start()

@viewlog.log_return_value
@client.event
async def on_message(message):
    """send message"""
    user_id = message.author.id
    if message.author == client.user:
        return
    if message.content.lower() == '!start' or message.content == '!s':
        LD.update_active(user_id, True)
        LD.update_time(user_id, datetime.now())
        await message.author.send(embed = discord.Embed(title = "ได้เวลาอยากคุยแล้ว! :pleading_face:", color = 0xeea3f9, description="อยากคุยเร็วๆจัง").set_thumbnail(url = r"https://user-images.githubusercontent.com/72595491/265518708-f1bc54b4-fdd0-4ac4-904a-9d67db02281c.png"))
        try:
            randomword = genword.generate()
            time.sleep(5)
            await message.author.send(embed = discord.Embed(title = randomword, color = 0xeea3f9))
            LD.update_waiting_message(user_id, True)
            LD.update_time(user_id, datetime.now())
        except discord.HTTPException: # Ignoring exception in on_message
            await message.author.send("ขอเวลาแปป")
    if message.content.lower() == '!end' or message.content == '!e':
        LD.update_active(user_id, False)
        LD.update_waiting_message(user_id, False)
        await message.author.send(embed = discord.Embed(title = "บายยยยย :face_holding_back_tears:", color = 0xeea3f9))
    if LD.get_waiting_message(user_id) is True:
        if '!reply' in message.content.lower():
            text_to_say = message.content.replace('!say ', '')
            LD.update_like_data(user_id, AIcheckgb.check(text_to_say))
            await message.author.send("ขอบคุณที่ตอบค่ะ")
            LD.update_waiting_message(user_id, False)
    if message.content.lower() == '!create':
        if not message.author.bot:
            if LD.check_data(user_id) is True:
                await message.author.send("คุณมี Data อยู่แล้ว")
            else:
                LD.add_data(user_id)
                await message.author.send("คุณได้สร้าง Data แล้ว")

client.run(gettoken())
