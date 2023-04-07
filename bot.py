import discord
from DISCORD_TOKEN import *
from random import randrange, choice, seed, uniform
from datetime import datetime   
import os 
import youtube_dl

def get_random_line(afile, default=None):
    line = default
    for i, aline in enumerate(afile, start=1):
        if randrange(i) == 0:  # random int [0..i)
            line = aline
    return line

intents = discord.Intents.default()
intents.message_content = True

#client = discord.Client(command_prefix='$',intents=intents)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messageContent = message.content.lower()

    if messageContent.startswith('$hello'):
        with open('greetings.txt') as f:
            greeting = get_random_line(f)
        await message.channel.send(greeting)  

    if messageContent.startswith('$time'):
        now = datetime.now()
        await message.channel.send(now)

    if messageContent.startswith('$are you lonely?'):
        await message.channel.send("I can't tell you about myself, but this may help you")  
        with open('lonely.txt') as f:
            quotes = get_random_line(f)
        await message.channel.send(quotes)

        

    if messageContent.startswith('$tell me a joke!'):
        with open('jokes.txt') as f:
            joke = get_random_line(f)
        await message.channel.send(joke)  

    if messageContent.startswith('$doggo'):
        filename = choice(os.listdir("dog-images//"))
        filepath = ("dog-images/" + filename)
        await message.channel.send(file=discord.File(filepath))
        with open('doggo-greetings.txt') as f:
            henlo = get_random_line(f)
        await message.channel.send(henlo)

        



client.run(DISCORD_TOKEN)