import discord
import re
import os
import time

## <    Variables   >
deleteTime = 3
embedTime = 5
##

from dotenv import load_dotenv
load_dotenv()
token = os.getenv('token')
print(f'Loaded Token')
#restricting access to the token. Just make ur own .env lol

# This bot is pretty normal. it just grabs words wrapped in [[]] and posts the wiki link to the page
# Written by Panjandemi#9301 on discord - Feel free to reach out if you've got questions
# dated 15/2/23

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True #Defining bot intents. Bot can't connect to discord if it doesn't have the right intents, so this needs to be done.
print(f'Loaded Intents')

client = discord.Client(intents=intents) # connecting to discord.

@client.event
async def on_ready():
    print (f'Logged in as {client.user} - Get Slaying!')
#When the bot logs on to discord, it sends this message into the shell.


@client.event
async def on_message(message):
    if message.author == client.user:
        apology = "Sorry, I couldn't find a wiki page with that name"
        time.sleep(embedTime)
        if ((not(message.embeds)) & (message.content != apology)): 
            # await message.delete() #If the message does not embed, delete it
            print(f'Failed to embed')
            #await message.channel.send(apology)
        elif (message.content == apology):
            time.sleep(deleteTime)
            await message.delete()
        else:
            return  # Prevents message loops in the off case that the bot would send a message that it could respond to
    
    message_content = message.content #gets the message content and puts it into a variable to be checked with the regex for any instances of the bot being called

    names = re.findall("\[\[[^\[\]]*\]\]",message_content) # Yes I know this sucks so bad to read but it's really simple I promise.
    # It's a regular expression that checks for any instance of words surrounded by [[]], *except* for when those brackets contain other brackets.
    # That exception allows you to call the bot multiple times in a single message
    
    wiki = "https://slay-the-spire.fandom.com/wiki/" # Just a quick definition for the wiki link.
    # I put this here because I thought the wiki had seperate places for cards and relics, but it turns out that's not the case
    # Still good to have for modularity's sake, just swap out the wiki page for a different wiki and hey presto, there's your wiki bot sorted. 
    # Provided of course that wiki uses the same catagorisation scheme as the STS wiki,,, Look whatever. It's so fine dw about it.
    
    for x in names:

        ### <    Manipulating String     >

        nonCapWords = ['for','and','of','the','to','with']  #I went through the game and found all instances of words that aren't capitalised.

        ##  <   Converting to a lowercase String    >
        namestr = ''.join(x) #converting the list from the findall into a string.
        namestr = re.sub("[\[\]]",'',namestr) #trim brackets off the string.
        namestr = namestr.lower() #reduces the string to lowercase
        ##

        ##  <   Checking for non-capitalised words  >
        namestrList = re.split("\s", namestr)
        A = 0
        for a in namestrList:
            
            noCap = False
            for b in nonCapWords:
                if a == b:
                    noCap = True
        ##  <   Capitalising Words  >
            if noCap == False:          
                workedWord = str(a)
                workedWord = list(workedWord)
                workedWord[0] = workedWord[0].swapcase()
                workedWord = ''.join(workedWord)
                #Wow I hope this works
            else:
                workedWord = str(a)
            
            namestrList[(A)] = workedWord
            A += 1     
        ##
        ##   

        namestr = '_'.join(namestrList) #Joining the string back together with underscores
        ###

        await message.channel.send(wiki + namestr) #Posts the wiki link into the chat
        print(f'{message.author} called for {wiki+namestr}') #sends a message into the shell to say that it posted a wiki link into the chat

client.run(token)





