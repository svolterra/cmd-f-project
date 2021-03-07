import discord
import os
import random
# import time

client = discord.Client()

#Ideas:
#Can also add self-care tips for break
#Can add encouraging messages while timer is counting down


# @client.event
# async def on_ready():
#     print('Hello I am {0.user}!'.format(client))

    

# def timer_start_break(t):
#      while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1

#      print("Take a break!!!!")


#  function call
# TODO: change the input to 1500 seconds
# t = 1
# timer_start_break(t)


study_encouragements = ["You can do it!", "You got this!", "Do your best!", "Shoot for the stars!", "I believe in you!", " It always seems impossible until it’s done.", "Remember to take breaks!", "Believe you can and you’re halfway there.", "Strive for progress, not perfection."]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!inspire'):
      response = random.choice(study_encouragements)
      await message.channel.send(response)

    if message.content.startswith("pomodoro!"):
      await message.author.send("Let's go!")

    


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, I am Pomodorobo! I will be your study buddy and remind you to take frequent breaks!'
        )

client.run(os.getenv('TOKEN'))

