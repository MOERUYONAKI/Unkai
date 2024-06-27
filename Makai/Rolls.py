# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


import Others.rolls as rolls
from discord import *
import discord 
from discord.ext import commands


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# - - - - - - - - - - - - - - - -  C O M M A N D E S  - - - - - - - - - - - - - - - - #


async def makai_roll(interaction : discord.Interaction, nombre : app_commands.Choice[int], types : app_commands.Choice[str], bonus : int = 0):
    if types.value == "fifty":
        base = 50 - bonus
        dtls = {"réussite critique" : 0, "réussite" : 0, "réussite faible" : 0, "échec" : 0, "échec critique" : 0}
        roll = []

        for i in range(nombre.value):
            roll.append(rolls.Makai_roll(bonus))
            r = roll[i][0][0]

            if r < 10 and r < base:
                dtls['échec critique'] += 1

            elif r < base and base >= 10:
                dtls['échec'] += 1

            elif r == base:
                dtls['réussite faible'] += 1

            elif r > base and r <= 90:
                dtls['réussite'] += 1

            elif r > 90 and r > base:
                dtls['réussite critique'] += 1

        txt = ""
        for key in dtls.keys():
            if dtls[key] == 1:
                txt += f"1 {key}, "

            elif dtls[key] > 1:
                txt += f"{dtls[key]} {key}s, "

        results = ""
        for j in range(nombre.value):
            results += f'{roll[j][0][0]}, '

        cmd = ""
        if bonus > 0:
            cmd = f"{nombre.value}d100 + {bonus}"

        elif bonus < 0:
            cmd = f"{nombre.value}d100 - {bonus}"

        else:
            cmd = f"{nombre.value}d100"

        await interaction.response.send_message(f'```# {results[0 : -2]} ({cmd})\nDétails : {txt[: -2]}```')

    elif types.value == "base":
        results = []
        for i in range(nombre.value):
            roll = rolls.basic_roll(100)
            results.append(roll)

        total = 0
        txt = ""
        for j in range(nombre.value):
            total += results[j]
            txt += f'{results[j]}, '

        if bonus > 0:
            cmd = f"{nombre.value}d100+{bonus}"

        elif bonus < 0:
            cmd = f"{nombre.value}d100{bonus}"

        else:
            cmd = f"{nombre.value}d100"
            
        await interaction.response.send_message(f'```# {total + bonus} \nDétails : {cmd} ({txt[0 : -2]})```')