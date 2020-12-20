import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NzkwMDAxOTQ4MTE5MTM4MzY2.X96QpQ.qXGdAu-JdzS4fAqNEPndh8n424I')