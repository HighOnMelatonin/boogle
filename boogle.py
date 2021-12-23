import discord
import os
from googlesearch import search
import random

client = discord.Client()

TOKEN = 'OTE0NDAyMzg4NTkxMzk0ODQ4.YaMhlg.8M55uVBIm_YckXrVeuRuVLDoS_s'
GUILD = os.getenv('GUILD')

def googlesearch(query):
    responses = search(query, num_results = 5)
    return responses[0], responses

@client.event
async def on_ready():
    print(client.guilds)
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

help = 'Enter query after double question marks and I will return the first google result from the query\n\nExample:\n\n> ??python\n> Embeded link: https://www.python.org'
messages = ['I found this', 'This is what I could find','Here you go','','Hope this helps','']
greetings = ['hello', 'hi','hey','yo','sup', 'hello :)']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<@!914402388591394848>'):
        await message.channel.send(embed = discord.Embed(title = help))

    if message.content.startswith('??'):
        query = message.content[2:]

        if query == "good bot":
            await message.channel.send("Thank you :)")
            return
            
        if query == 'help' or query == 'h':
            await message.channel.send(embed = discord.Embed(title = "Help", description = help))
            return

        if query.lower() in greetings:
            greeting = random.choice(greetings)
            await message.channel.send(greeting)
            return

        if query.lower() == 'how are you' or query.lower() == 'how are u':
            await message.channel.send("I'm fine, thx\nHow are you")
            return

        else:
            response, responses = googlesearch(query)
            ##responses is a list of urls from the google search
            embeded = discord.Embed(title = query, url = response)
            rmessage = random.choice(messages)
            await message.channel.send(content = rmessage, embed = embeded)

if __name__ == '__main__':
    client.run(TOKEN)
