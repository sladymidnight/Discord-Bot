import discord
import random

TOKEN = OTIxNTIyMDU2NjQwNzQxNDQ3.Yb0ISw.rgYWY-PdoGWOSlJJLP2XIlMUJJM

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
client.run(TOKEN)

