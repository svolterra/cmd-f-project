import discord
import os
import random
import time

client = discord.Client()


#Ideas:
#Can also add self-care tips for break
#Can add encouraging messages while timer is counting down

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

# def timer_start_study():
#   seconds = 10
#   while seconds != 0:
#     mins, secs = divmod(seconds, 60)
#     timer = '{:02d}:{:02d}'.format(mins, secs)
#     print(timer, end="\r")
#     seconds -= 1
#     time.sleep(1)
  
#   timer_take_break()

# def timer_take_break():
#   seconds = 5
#   while seconds != 0:
#     mins, secs = divmod(seconds, 60)
#     timer = '{:02d}:{:02d}'.format(mins, secs)
#     print(timer, end="\r")
#     seconds -= 1
#     time.sleep(1)

#   timer_start_study()


def timer_start_break(t1):
    while t1:
        mins, secs = divmod(t1, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t1 -= 1
    


def timer_start_study(t2):
    while t2:
        mins, secs = divmod(t2, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t2 -= 1


# function call
# TODO: change the input to 1500 seconds
t1 = 10
t2 = 10
#timer_start_break(t1)



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
      '\n Say $hello and I will say hello back! 👋' 
      '\n Send !inspire and I will send you a random inspirational message to keep you going! I belive in you! ✨'
      '\n Send !care and I will remind you to give yourself some time for self-care (I need it too!) ❤️'
      '\n Send !pomodoro and I will remind you to take frequent breaks using the Pomodoro technique!' 
      ) 



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
        await message.add_reaction('\U0001F44B')

    if message.content.startswith('!inspire'):
        response = random.choice(study_encouragements)
        await message.channel.send(response)
        await message.add_reaction("✨")

    if message.content.startswith("!care"):
        care_response = random.choice(self_care)
        await message.channel.send(care_response)
        await message.add_reaction('\U0001F917', '\U0001F49C')

    if message.content.startswith("pomodoro!"):
        await message.add_reaction('\U0001F345')
        await message.author.send("Let's study hard! 25 minutes on the clock!")
        timer_start_study(t2)
        await message.author.send("Time to take a 5 minute break!")
        timer_start_break(t1)
        await message.author.send("If you would like to reset timer, please send !repeat to the chat!")

    if message.content.startswith('!repeat'):
      channel = message.channel
      await channel.send('Back to studying! You got this!')
      timer_start_study(t2)
      await message.author.send("Great work! Five minute break time!")
      timer_start_break(t1)
      await message.author.send("If you would like to reset timer, please send !repeat to the chat!")

 
client.run(os.getenv('TOKEN'))