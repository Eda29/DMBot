#file: botmain.py
#author: Donovan Tyler
#Creation Date: Dec. 2, 2022
#purpose: The entry point to the bot application.
#Last Edited by: Donovan Tyler
#Last Edit Time: Dec. 3, 2022 @ 13:38 EST

import os
import random
import discord
import itertools

from dotenv import load_dotenv
from discord import option

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(name='roll', guild_id=1048352661130461304)
@option("num_dice", description="The number of dice you wish to roll.")
@option("dice_face", description="The type of die you wish to roll. Acceptable answers are 4, 6, 8, 10, 12, 20, 100")
async def roll(ctx, num_dice: int, dice_face: int):
    faceTuple = (4, 6, 8, 10, 12, 20, 100)
    if dice_face not in faceTuple:
        await ctx.respond("The type of die must be of values: 4, 6, 8, 10, 12, 20, or 100")

    totalValue = 0

    for val in itertools.repeat(None, num_dice):
        dieValue = random.randint(1, dice_face)
        totalValue = totalValue + dieValue

    await ctx.respond(totalValue)

bot.run(TOKEN)