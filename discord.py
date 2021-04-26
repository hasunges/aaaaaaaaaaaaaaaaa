import asyncio
import discord

client = discord.Client()

token = "2CLlVeVHwN3st_2hzDx5DSi3MaocbebQ"

@client.event
async def on_ready():
     print("Logged in as ") 
    print(client.user.name)
    print(client.user.id)
    print("===========")

    await client.change_presence(game=discord.Game(name="ㄹ!커맨드", type=1))

    @client.event
async def on_message(message):
    if message.author.bot: 
        return None

            id = message.author.id 
    channel = message.channel

        if message.content.startswith('ㄹ!커맨드'): 
        await client.send_message(channel, '아직 생각중...')

client.run(2CLlVeVHwN3st_2hzDx5DSi3MaocbebQ)