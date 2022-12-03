#file: commands.py
#author: Donovan Tyler
#Creation Date: Dec. 2, 2022
#purpose: encapsulates all of the commands the bot uses
#Last Edited by: Donovan Tyler
#Last Edit Time: Dec. 2, 2022 @ 20:09 EST

#import requests
#
#url = "https://discord.com/api/v10/applications/1048385686732034198/commands"
#
#json = {
#    "name" : "roll",
#    "description": "Roll Dice. Requires the number of dice and how many faces it will have as parameter",
#    "options": [
#        #{
#            #"name": "dice",
#            #"description": "Details on the dice to roll",
#            #"type": 1,  #sub commands.
#            #"options": [
#            #    {
#            #        "name": "Number",
#            #        "description":"How many dice do you want to roll?",
#            #        "type": 4,
#            #        "required":"true"
#            #    },
#            #    {
#            #        "name": "Faces",
#            #        "description":"How many sides does each die have?",
#            #        "type": 4,
#            #        "required":"true"
#            #    }
#            #]
#        #}
#        {
#            "name":"numDice",
#            "description":"Number of dice to be rolled",
#            "type":4
#        },
#        {
#            "name":"numDiceFace",
#            "description":"Number of faces the die has",
#            "type":4
#        }
#    ]
#}
#
#headers = {
#    "Authorization": "Bot MTA0ODM4NTY4NjczMjAzNDE5OA.GSgBsN.fI1UYnbZG-9WsmMkuUAfsfljunH7zjFSvewqjk"
#}
#
#r = requests.post(url, headers=headers, json=json)

import random
import botmain
import itertools
bot = botmain.bot
commands = botmain.commands

@bot.command(description='roll a die or twenty')
async def roll(ctx: commands.Context, arg1:int, arg2:int):
    totalValue = 0

    for val in itertools.repeat(None, arg1):
        dieValue = random.randint(1, arg2)
        totalValue = totalValue + dieValue
