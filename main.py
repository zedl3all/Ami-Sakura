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
import AIcheckgb2


@viewlog.log_return_value
def gettoken():
    """GetToken"""
    with open('Token.json', "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["tokenBotdiscord"]

intents = discord.Intents.all()
client = discord.Client(intents=intents)
randomword = ""

@tasks.loop(seconds=30)
async def slow_count():
    """slow_count"""
    if LD.get_userid_by_online() is not None:
        for user_id in LD.get_userid_by_online():
            #print(user_id)
            if int(LD.get_time(user_id)[:2]) < int(datetime.now().hour):
                user = await client.fetch_user(user_id)
                if LD.get_waiting_message(user_id) is True:
                    LD.update_like_data(user_id, -10)
                try:
                    global randomword
                    randomword = genword.generate()
                    time.sleep(5)
                    await user.send(embed = discord.Embed(title = randomword, color = 0xeea3f9))
                    LD.update_waiting_message(user_id, True)
                    LD.update_time(user_id, datetime.now())
                except discord.HTTPException: # Ignoring exception in on_message
                    await user.send("ขอเวลาแปป")
            time.sleep(5)
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
    ###play command###
    if message.content.lower() == '!start' or message.content == '!s':
        if LD.check_data(user_id) is False:
            await message.author.send("กรุณาสร้าง data ก่อน !Create เพื่อสร้าง")
        else:
            LD.update_active(user_id, True)
            await message.author.send(embed = discord.Embed(title = "ได้เวลาอยากคุยแล้ว! :pleading_face:", color = 0xeea3f9, description="อยากคุยเร็วๆจัง").set_thumbnail(url = r"https://user-images.githubusercontent.com/72595491/265518708-f1bc54b4-fdd0-4ac4-904a-9d67db02281c.png"))
            try:
                global randomword
                randomword = genword.generate()
                time.sleep(5)
                await message.author.send(embed = discord.Embed(title = randomword, color = 0xeea3f9))
                LD.update_waiting_message(user_id, True)
                LD.update_time(user_id, datetime.now())
            except discord.HTTPException: # Ignoring exception in on_message
                await message.author.send("ขอเวลาแปป")
    ###end command###
    if message.content.lower() == '!end' or message.content == '!e':
        if LD.check_data(user_id) is False:
            await message.author.send("กรุณาสร้าง data ก่อน !Create เพื่อสร้าง")
        else:
            LD.update_active(user_id, False)
            LD.update_waiting_message(user_id, False)
            await message.author.send(embed = discord.Embed(title = "บายยยยย :face_holding_back_tears:", color = 0xeea3f9))
    ###reply command###
    if LD.get_waiting_message(user_id) is True:
        if '!reply' in message.content.lower():
            text_to_say = message.content.replace('!reply ', '')
            if AIcheckgb2.check2(randomword) == AIcheckgb2.check2((text_to_say)):
                LD.update_like_data(user_id, 1)
            elif AIcheckgb2.check2(text_to_say) == "tell":
                LD.update_like_data(user_id, 1)
            else:
                LD.update_like_data(user_id, -5)
            LD.update_like_data(user_id, AIcheckgb.check(text_to_say))
            await message.author.send("ขอบคุณที่ตอบค่ะ")
            LD.update_waiting_message(user_id, False)
    ###create data command###
    if message.content.lower() == '!create':
        if not message.author.bot:
            if LD.check_data(user_id) is True:
                await message.author.send("คุณมี Data อยู่แล้ว")
            else:
                LD.add_data(user_id)
                await message.author.send("คุณได้สร้าง Data แล้ว")
    ###help command###
    if message.content.lower() == '!help':
        if not message.author.bot:
            embed = discord.Embed(title = ":no_entry: วิธีการใช้งาน :no_entry:", color = 0xeea3f9, description="!Create: To set up your profile.\n !Start: Begin a chat with me.\n !Reply: Use to answer my questions.\n 　Ex: !Reply Hello\n !End: To stop chatting with me.\n !Level: To see your data. \n\n If you're active, I'll chat with you every hour ♥️.\n")
            embed.set_thumbnail(url = r"https://user-images.githubusercontent.com/72595491/265518708-f1bc54b4-fdd0-4ac4-904a-9d67db02281c.png")
            await message.author.send(embed = embed)
    ###level command###
    if message.content.lower() == '!level' or message.content == "!l":
        if not message.author.bot:
            if LD.check_data(user_id):
                #mention = message.author.mention
                username = message.author.global_name
                avatar = message.author.display_avatar
                data = LD.get_level_like(user_id)
                embed = discord.Embed(title = "Level", color = 0xeea3f9, description=f'Your Level: {data[0]}\n Your Like: {data[1]}')
                embed.set_thumbnail(url=(avatar))
                embed.set_author(name = f'{username}', icon_url=avatar)
                await message.author.send(embed=embed)
            else:
                await message.author.send("กรุณาสร้าง data ก่อน !Create เพื่อสร้าง")

client.run(gettoken())
