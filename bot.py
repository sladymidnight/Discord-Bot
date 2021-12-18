import discord
import os 
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

client = Discord.Client()

@client.event
async def on_ready():
  print("Bot is up and ready!")
  
@client.event
async def hello( ):
  await ctx.send("Hi!")
  
client.run(" OTIxNTIyMDU2NjQwNzQxNDQ3.Yb0ISw.rgYWY-PdoGWOSlJJLP2XIlMUJJM ")
