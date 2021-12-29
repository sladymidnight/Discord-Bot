import discord
import random
import timeit

TOKEN = 'OTIxODE4MjEyODY0MjI5NDA3.Yb4cHA.ZMQe5UVU_4rcASlxJpu5-97IFrE'

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}: {user_message} ({channel})')
  
  if message.author == client.user:
    return
  
  if message.channel.name == 'general':
    if user_message.lower() == 'hello': 
      await message.channel.send(f'Hello {username}!')
      return
    elif user_message.lower() == 'bye':
      await message.channel.send(f'See you later {username}!')
      return
    elif user_message.lower() == '!random':
      response = f'This is your random number: {random.randrange(10000000)}'
      await message.channel.send(response)
      return
    elif user_message.lower() == '!ping':
      await message.channel.send(f'Pong you dirty whore {username}!')
      return

    elif user_message.lower() == 'whore':
        await message.channel.send(f'you are right, you are a whore!')
        return

    elif user_message.lower() == 'commands':
        await message.channel.send(f'The commands are hello, bye, !random, !ping, and whore')
        return

    elif user_message.lower() == 'weather':
        await message.channel.send(f'I am not a meterologist')
        return

    timeit

    square_numbers = []
    for num in range [1, 1000]:
        square_numbers.append(num**2)

        
    if user_message.lower() == '!anywhere':
      await message.channel.send('This can be used anywhere!')
      return
