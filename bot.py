import discord
import random

TOKEN = 'OTIxODE4MjEyODY0MjI5NDA3.Yb4cHA.ZMQe5UVU_4rcASlxJpu5-97IFrE'

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
client.run(TOKEN)

