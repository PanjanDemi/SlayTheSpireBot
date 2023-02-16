import discord
## Small tester bot to get myself familiar with everything
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('MTA3NTE5MTE0MTA1NTYwNjc5NA.Gg4loO.GjzKtnzce4t66mbq6sTnAEoqJGozSJ7znAwOcI')


## TOKEN: MTA3NTE5MTE0MTA1NTYwNjc5NA.Gg4loO.GjzKtnzce4t66mbq6sTnAEoqJGozSJ7znAwOcI