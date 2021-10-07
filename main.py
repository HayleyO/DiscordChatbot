import discord

BOTTOKEN = 'Get your own bot token :p'

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await main()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(message.content == "~Clear"):
        async for message in message.channel.history(limit=200):
            await message.delete()

client.run(BOTTOKEN)
