

#importing all necessary packages 
from distutils.command.clean import clean
import discord
from time import sleep
import random
from random import randint
from server import keep_alive




#connecting to server 
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in {0.user}".format(client))



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

    #checking if messages are in raffle channel
    #sets delay and range is raffle is followed by : and two numbers 
    #format -- raffle:(delay time in seconds)-(max amount of users in raffle)



    if user_message.split('!')[0].lower() == ("help"):
        await message.channel.send(f'Commands: \n raffle:(delay)-(max)! standard elimination style raffle \n rafflem:1/(role - all users my default)! raffle for members with role \n raffleo:(delay)!  all online users raffle \n rafflex:(delay)-(max)!  faster raffle\n raffle5:(delay)-(max)!  picks 5 winners')


    if user_message.split(':')[0].lower() == ("raffle"):
        delay = user_message.split('-')[0]
        delay = float(delay.rsplit(':')[-1])
        max = user_message.split('!')[0]
        max = int(max.rsplit('-')[-1])
        if(delay > 30 or max > 1001):
            return
        nums = []
        for x in range(1,max+1):
            nums.append(x)
        i = 0
        while i < max:
            longest = len(nums) - 1
            if max-i == 1:
                sleep(delay)
                current = str(nums[0])
                await message.channel.send(f'{current}\u2728')
                return
            elif i % 5 == 0:
                await message.channel.send(f'Remaining: {nums}\U0001F4B0')
                current = nums.pop(random.randint(0, longest))
                await message.channel.send(f'{current}\u274C')
                i+=1
            else:
                current = nums.pop(random.randint(0, longest))
                await message.channel.send(f'{current}\u274C')
                i+=1


    if user_message.split(':')[0].lower() == "rafflem":
        delay = user_message.split('/')[0]
        delay = float(delay.rsplit(':')[-1])
        roleinput = user_message.split('!')[0]
        roleinput = str(roleinput.rsplit('/')[-1])
        if(roleinput.lower() == "keep it 100"):
            roleid = 1024718547848527962
            role = discord.utils.get(message.guild.roles, id=roleid)
        else:
            role = discord.utils.get(message.guild.roles, name=roleinput)
        
        if(len(roleinput) < 2):
            roleinput = False
        i = 0
        if(delay > 30):
            return 
        author = message.author
        channel = message.channel
        guild = message.guild
        if(roleinput == False):
            members = [
        member for member in guild.members if not member.bot and member != author
        ]
        else:
            members = [
        member for member in guild.members if not member.bot and member != author and role in member.roles
        ]
        
        max = len(members)
        while i < max:
            if i == 0: 
                sleep(delay)
                member = members.pop(random.randint(0, len(members)-1))
                await message.channel.send('\U0001F4A3 Elimination starting \U0001F4A3')
                await message.channel.send(f'{member.display_name}\u274C')
                await message.channel.send(f'{len(members)} users left')
                i+=1
                
            if max-i == 1:
                sleep(delay)
                member = members[0]
                await message.channel.send(f'{member.mention}\u2728')
                return
            else:
                sleep(delay)
                member = members.pop(random.randint(0, len(members)-1))
                await message.channel.send(f'{member.display_name}\u274C')
                await message.channel.send(f'{len(members)} users left')
                i+=1




    if user_message.split(':')[0].lower() == ("raffleo"):
            delay = user_message.split('!')[0]
            delay = float(delay.rsplit(':')[-1])
            author = message.author
            channel = message.channel
            guild = message.guild

            members = [
            member for member in guild.members if not member.bot and member != author and member.status != discord.Status.offline
                ]
            await message.channel.send(f'{len(members)} users online')
            i = 0
            max = len(members)
            while i < max:
                if i == 0: 
                    sleep(delay)
                    member = members.pop(random.randint(0, len(members)-1))
                    await message.channel.send('\U0001F4A3 Elimination starting \U0001F4A3')
                    await message.channel.send(f'{member.display_name}\u274C')
                    await message.channel.send(f'{len(members)} users left')
                    i+=1
                    
                if max-i == 1:
                    sleep(delay)
                    member = members[0]
                    await message.channel.send(f'{member.mention}\u2728')
                    return
                else:
                    sleep(delay)
                    member = members.pop(random.randint(0, len(members)-1))
                    await message.channel.send(f'{member.display_name}\u274C')
                    await message.channel.send(f'{len(members)} users left')
                    i+=1


    if user_message.split(':')[0].lower() == ("rafflex"):
        delay = user_message.split('-')[0]
        delay = float(delay.rsplit(':')[-1])
        max = user_message.split('!')[0]
        max = int(max.rsplit('-')[-1])
        if(delay > 30 or max > 1001):
            return
        nums = []
        for x in range(1,max+1):
            nums.append(x)
        i = 0
        while i < max:
            longest = len(nums) - 1
            if len(nums) - 2 <= 1:
                while len(nums) > 1: 
                    longest = len(nums) - 1
                    nums.pop(random.randint(0, longest))
                sleep(delay)
                current = str(nums[0])
                await message.channel.send(f'\u2728{current}\u2728')
                return
            else:
                for i in range(0, 2):
                    longest = len(nums) - 1
                    nums.pop(random.randint(0, longest))
                await message.channel.send(f'\U0001F4A3Remaining: {nums}\U0001F4B0')
                i+=1


    if user_message.split(':')[0].lower() == ("raffle5"):
        delay = user_message.split('-')[0]
        delay = float(delay.rsplit(':')[-1])
        max = user_message.split('!')[0]
        max = int(max.rsplit('-')[-1])
        if(delay > 30 or max > 1001):
            return
        nums = []
        for x in range(1,max+1):
            nums.append(x)
        i = 0
        while i < max:
            longest = len(nums) - 1
            if len(nums) - 2 <= 5:
                for i in range(0,5):
                    await message.channel.send(f'\u2728{nums[i]}\u2728')
                return
            else:
                for i in range(0, 2):
                    longest = len(nums) - 1
                    nums.pop(random.randint(0, longest))
                await message.channel.send(f'Remaining: \U0001F4B0{nums}\U0001F4B0')
                i+=1

        


#running the function with the bot's token 
keep_alive()
TOKEN = "MTAyNTI0NDgwNDAyMTQ5Nzg2Ng.Gd9Mc4.RTUKPfN48gU1SW5-NYaFyx2-q0AiIjjlI9CchU"
client.run(TOKEN)