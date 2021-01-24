import random
import discord
import json

bot = discord.Client()

jdata = json.load(open("config.json"))
replies = jdata["replies"]
commands = jdata["commands"]
bot_token = jdata["token"]
prefix = jdata["prefix"]

class Command:
    command:str
    reply:str

    def __init__(self,command:str,reply:str):
        self.command = command
        self.reply = reply

commands_ = list()
for com in commands:
    commands_.append(Command(com["command"],com["reply"]))

commands = commands_

@bot.event
async def on_ready():
    print("The bot is ready!")

#@bot.command    
async def sa(channel):
    await channel.send(replies[random.randint(0,len(replies) - 1)])

@bot.event
async def on_message(message:discord.message.Message):
    if message.author == bot.user:
        return
    #print(type(message))

    for com in commands:
        if prefix + com.command == message.content:
            await message.channel.send(com.reply)
            return

    await message.channel.send(replies[random.randint(0,len(replies) - 1)])

bot.run(bot_token)