#file: botmain.py
#author: Donovan Tyler
#Creation Date: Dec. 2, 2022
#purpose: The entry point to the bot application.
#Last Edited by: Donovan Tyler
#Last Edit Time: Dec. 2, 2022 @ 20:09 EST

import os
import random
import discord
import commands

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    #boilerplate debugging code
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

#this may not throw, we do not know. this depends on commands.
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)