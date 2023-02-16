import discord
import re
import os

from dotenv import load_dotenv
load_dotenv()
token = os.getenv('token')
#restricting access to the token. Just make ur own .env lol

# This bot is pretty normal. it just grabs words wrapped in [[]] and posts the wiki link to the page
# Written by Panjandemi# on discord - Feel free to reach out if you've got questions
# dated 15/2/23

intents = discord.Intents.default()
intents.message_content = True #Defining bot intents. Bot can't connect to discord if it doesn't have the right intents, so this needs to be done.

client = discord.Client(intents=intents) # connecting to discord.

@client.event
async def on_ready():
    print (f'Logged in as {client.user} - Get Slaying!')
#When the bot logs on to discord, it sends this message into the shell.

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Prevents message loops in the off case that the bot would send a message that it could respond to
    
    message_content = message.content #gets the message content and puts it into a variable to be checked with the regex for any instances of the bot being called

    #if discord.TextChannel.name == "bots":
    #putting this here to restrict it to a particular channel channel names and whatnot
    #i'd love to figure out how to get channel restrictions going. doesn't seem to want to work


    names = re.findall("\[\[[^\[\]]*\]\]",message_content) # Yes I know this sucks so bad to read but it's really simple I promise.
    # It's a regular expression that checks for any instance of words surrounded by [[]], *except* for when those brackets contain other brackets.
    # That exception allows you to call the bot multiple times in a single message
    
    wiki = "https://slay-the-spire.fandom.com/wiki/" # Just a quick definition for the wiki link.
    # I put this here because I thought the wiki had seperate places for cards and relics, but it turns out that's not the case
    # Still good to have for modularity's sake, just swap out the wiki page for a different wiki and hey presto, there's your wiki bot sorted. 
    
    for x in names:
        namestr = ''.join(x) #converting the list from the findall into a string.
    
        namestr = re.sub("\s","_",namestr) #replacing white space with underscores to ensure that it interacts with hyperlinks correctly.

        namestr = re.sub("[\[\]]",'',namestr) #trim brackets off the string.

        await message.channel.send(wiki + namestr) #Posts the wiki link into the chat
        print(f'{discord.message.author} called for {wiki+namestr}') #sends a message into the shell to say that it posted a wiki link into the chat

client.run(token)





