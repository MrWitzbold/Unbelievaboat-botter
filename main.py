import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    if message.content.split(" ")[0] == ";bot":
        while True:
            await message.channel.send("!work")
            await message.channel.send("!slut")
            time.sleep(30)
        
client.run("TOKEN", bot=False)
