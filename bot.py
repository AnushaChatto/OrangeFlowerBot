import discord
from DISCORD_TOKEN import *
from random import randrange    

def get_random_line(afile, default=None):
    line = default
    for i, aline in enumerate(afile, start=1):
        if randrange(i) == 0:  # random int [0..i)
            line = aline
    return line



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        with open('greetings.txt') as f:
            greeting = get_random_line(f)
        await message.channel.send(greeting)  

client.run(DISCORD_TOKEN)