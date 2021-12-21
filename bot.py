import discord
import random

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
    
    if user_message.lower() == '!anywhere':
      await message.channel.send('This can be used anywhere!')
      return

import time 
global eggplants 
global condoms
eggplants = 0 
condoms = 0 

def start() : 
  print ("Hello all of the whores who come!")
  name = input("What is your stripper name:")
  print("Welcome, "+name+" !")
  print("Your objective is to collect eggplants and condoms before the show.")
  print("Each eggplant you collect, you will get a condom.")
  choice = input("Do you want to continue Y/N")
  if choice == "Y":
    def begin() :
      if choice == "N":
        print("Goodbye you fucking stick up the ass party pooper.")
  def start() :
    print("Let us collect the dil- I mean eggplants.")
    pick = input("Would you like to pick up this eggplants Y/N")
    if pick == "Y":
      time.sleep(1)
      print ("You picked up the purple, big, volumed...uhhhh....eggplant!")

start()

  
client.run(TOKEN)
