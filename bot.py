import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'd.')

@cleint.event 
async def on_ready():
  print('Bot is ready.')

client.run('NzI0MjI2NTkyODE3MDIwOTU4.Xu9GmA.j5daB9QgSOBLiHrrvZAcjM-1154')
