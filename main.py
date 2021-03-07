import discord
import os
import random
import time

client = discord.Client()


study_encouragements = [
    "You can do it!", "You got this!", "Do your best!", "Shoot for the stars!",
    "I believe in you!", " It always seems impossible until it’s done.",
    "Remember to take breaks!", "Believe you can and you’re halfway there.",
    "Strive for progress, not perfection."
]

self_care = [
    "Drink some water!",
    "Go for a walk!",
    "Get some food!",
    "Get some rest. You deserve it!",
]

self_care_tips_for_break = [
  "Get moving! Exercise!", 
  "Make some tea", 
  "Chat with some friends or family!", 
  "Listen to your favourtie music!"
  "Meditate"
]


# This function starts the break timer. Breaks are 5 mins long
def break_time(five_mins):
    while five_mins:
        mins, secs = divmod(five_mins, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        five_mins -= 1


# This function starts the study time. Study times are 25 mins lomg
def study(twenty_five_mins):
    while twenty_five_mins:
        mins, secs = divmod(twenty_five_mins, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        twenty_five_mins -= 1


five_mins = 5*60 #5 minutes in seconds
twenty_five_mins = 25*60 #25 minutes in second


@client.event
async def on_ready():
    print('Hello I am {0.user}!'.format(client))


async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, I am Pomodorobo! I will be your study buddy and remind you to take frequent breaks!'
    )

    await member.dm_channel.send(
        'Here are my commands:  '
        '\n Say **$hello** and I will say hello back! 👋'
        '\n Send **!inspire** and I will send you a random inspirational message to keep you going! I believe in you! ✨'
        '\n Send **!care** and I will remind you to give yourself some time for self-care (I need it too!) ❤️'
        '\n Send **!pomodoro** and I will remind you to take frequent breaks using the Pomodoro technique!'
        '\n Send **!tips** and I will give you some suggestions for things to do while taking a break!'
        )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
        await message.add_reaction('\U0001F44B')
        
    if message.content.startswith('!introduce'):
       await message.author.send(
        'Hi there, I am Pomodorobo! I will be your study buddy and remind you to take frequent breaks!'
    )
      await message.author.send(
        'Here are my commands:  '
        '\n Say **!hello** and I will say hello back! 👋'
        '\n Send **!inspire** and I will send you a random inspirational message to keep you going! I believe in you! ✨'
        '\n Send **!care** and I will remind you to give yourself some time for self-care (I need it too!) ❤️'
        '\n Send **!pomodoro** and I will remind you to take frequent breaks using the Pomodoro technique!'
        '\n Send **!tips** and I will give you some suggestions for things to do while taking a break!'
      )

    if message.content.startswith('!inspire'):
       response = random.choice(study_encouragements)
       await message.author.send(response)
       await message.add_reaction("✨")

    if message.content.startswith("!care"):
      response = random.choice(self_care)
      await message.author.send(response)
      await message.add_reaction('\U0001F917', '\U0001F49C')
        
    if message.content.startswith("!tips"):
      await message.add_reaction('\U0001F601')
      tips_response = random.choice(self_care_tips_for_break)
      await message.author.send(tips_response)
      await message.add_reaction('\U0001F917', '\U0001F49C')

    if message.content.startswith("!pomodoro"):
        await message.add_reaction('\U0001F345')
        await message.author.send("Let's study hard! 25 minutes on the clock!")
        study(twenty_five_mins)
        await message.author.send("Time to take a 5 minute break!")
        break_time(five_mins)
        await message.author.send("If you would like to reset timer, please send **!repeat** to the chat!")

    if message.content.startswith('!repeat'):
        channel = message.channel
        await channel.send('Back to studying! You got this!')
        study(twenty_five_mins)
        await message.author.send("Great work! Five minute break time!")
        break_time(five_mins)
        await message.author.send(
            "If you would like to reset timer again, please send !repeat to the chat!")
        await message.author.send(
            "Remember to take a 45 minute break after four 25 minute study sessions (4 pomodoro cycles)! ❤️")
    
 
    


client.run(os.getenv('TOKEN'))
