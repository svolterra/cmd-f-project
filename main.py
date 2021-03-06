import discord
import time

client = discord.Client()

#Ideas:
#Can also add self-care tips for break
#Can add encouraging messages while timer is counting down


@client.event
async def on_ready():
    print('Hello I am {0.user}!'.format(client))

    

def timer_start_break(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Take a break!!!!")


# function call
#TODO: change the input to 1500 seconds
t = 10
timer_start_break(t)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run("ODE3ODQ4MjY0MDMxMjA3NDc1.YEPejQ.7-Q7kOtk_q66cV9GQM_Z6-1FfEE")
