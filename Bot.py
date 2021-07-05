import discord
# 반복 작업을 위한 패키지
from discord.ext import tasks
import pw.password as pw
import asyncio
import db.utils as utils
import db.check_date as date_checker
import db.spreadsheet as spreadsheet
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    result = []
    command = message.content
    channel = message.channel
    
    if command == "!backup":
        await message.channel.send("```백업할 데이터의 최대 일자를 입력해 주세요 \n ex) 2021-07-07```")
        limit_date = await utils.get_text(client, message)
        counter = 0
        async for message in channel.history(limit=None):
            name = str(message.author)
            command = message.content
            date = await date_checker.get_time(message.id)

            if date < limit_date:
                break
            else: 
                if message.author == client.user:
                    counter += 1
        
                if message.attachments!=[]:
                    result.append([date,name,command,message.attachments[0].url])
                else:
                    result.append([date,name,command])
            
        
        spreadsheet.typeToSpreadSheed(result)
        await message.channel.send("backUp!")
        
        
client.run(pw.Token())


