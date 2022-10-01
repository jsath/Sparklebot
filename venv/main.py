

#importing all necessary packages 
import discord
from time import sleep
import random
from random import choice
from server import keep_alive
import os



#connecting to server 
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    #Bot will only reply to messages that aren't from other bots and have contents from users in the server
    if (message.author.bot or message.guild is None) or (message.content is None):
        return
    if message.author == client.user:
        return

    #setting variable names 
    user = str(message.author).split('#')[0]
    user_message = str(message.content)

    #checking if messages are in sparkle-bot-raffle channel
    #sets delay and range is raffle is followed by : and two numbers 
    #format -- raffle:(delay time in seconds)-(max amount of users in raffle)
    if message.channel.name == 'sparkle-bot-raffle':
        if user_message.split(':')[0].lower() == ("raffle"):
            delay = user_message.split('-')[0]
            delay = int(delay.rsplit(':')[-1])
            max = user_message.split('!')[0]
            max = int(max.rsplit('-')[-1])

        #creates an list of all numbers x numbers in range
        nums = []
        for x in range(1,max+1):
            nums.append(x)
        i = 0

        #iterates for all numbers in list and randomly selects, then removes that number from list
        #when there is one number left, it is declared the winner
        while i < max:
            if max-i == 1:
                sleep(delay)
                current = choice(nums)
                await message.channel.send(f'{current}\u2728')
                return
            else:
                sleep(delay)
                current = choice(nums)
                await message.channel.send(f'{current}\u274C')
                nums.remove(current)
                i+=1

    #greets users in all channels of server
    if user_message.lower() == '!sparklebot':
        await message.channel.send(f'Hello {user}')
        return

#running the function with the bot's token 
keep_alive()
TOKEN = os.environ.get("Secret_Token")
client.run(TOKEN)