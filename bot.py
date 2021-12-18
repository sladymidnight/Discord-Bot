import discord
import random

TOKEN = 'OTIxNTIyMDU2NjQwNzQxNDQ3.Yb0ISw.yjCySIduVuk91juzx1B02gaVrIY'

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
client.run(TOKEN)

