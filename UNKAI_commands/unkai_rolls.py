from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from time import *
from random import randint

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# Makai roll - v2

def mk_roll(bonus : int = 0):
    rolls = []
    roll = randint(0, 100)

    if roll == 50 + bonus:
        roll = randint(0, 100)

        if roll == 50 + bonus:
            roll = randint(0, 100)
    
    rolls.append(roll)
    return [rolls, 49 + bonus]


# base command

async def roll(ctx : commands.Context, faces : int = 6, nombre : int = 1):
    rolled = []
    a = 0
    b = 0
    total = 0

    for i in range(nombre):
        temp = randint(1, int(faces))
        rolled.append(temp)
        total += temp

    moyenne = int(round(total / len(rolled), 0))

    if faces > 2 and nombre > 1:
        
        for elt in rolled:
            if elt == 1:
                a += 1

            elif elt == int(faces):
                b += 1

            rolled = str(rolled)

        await ctx.send(f'```# {rolled[1:-1]}\n{a} échecs critiques - {b} réussites critiques - moyenne : {moyenne}```')

    else:
        rolled = str(rolled)
        await ctx.send(f'> {rolled[1:-1]} \n{f"> Majorité - {moyenne}" if nombre > 4 else ""}')

async def makai_roll(ctx : commands.Context, bonus : int, nombre : app_commands.Choice[int]):
    roll = []
    for i in range(nombre):
        roll.append(mk_roll(bonus))
    
    base = 49 + bonus
    dtls = {"réussite critique" : 0, "réussite" : 0, "réussite faible" : 0, "échec" : 0, "échec critique" : 0}

    r1 = roll[0][0][0]
    if r1 < 10:
        dtls['réussite critique'] += 1

    elif r1 < base:
        dtls['réussite'] += 1

    elif r1 == base + 1:
        dtls['réussite faible'] += 1

    elif r1 > 90:
        dtls['échec critique'] += 1

    elif r1 > base:
        dtls['échec'] += 1

    if len(roll) > 1:
        r2 = roll[1][0][0]
        if r2 < 10:
            dtls['réussite critique'] += 1

        elif r2 < base:
            dtls['réussite'] += 1

        elif r2 == base + 1:
            dtls['réussite faible'] += 1

        elif r2 > 90:
            dtls['échec critique'] += 1

        elif r2 > base:
            dtls['échec'] += 1

    if len(roll) > 2:
        r3 = roll[2][0][0]
        if r3 < 10:
            dtls['réussite critique'] += 1

        elif r3 < base:
            dtls['réussite'] += 1

        elif r3 == base + 1:
            dtls['réussite faible'] += 1

        elif r3 > 90:
            dtls['échec critique'] += 1

        elif r3 > base:
            dtls['échec'] += 1

    txt = ""
    for key in dtls.keys():
        if dtls[key] == 1:
            txt += f"1 {key}, "

        elif dtls[key] > 1:
            txt += f"{dtls[key]} {key}s, "

    if bonus > 0:
        cmd = f"{nombre}d100 + {bonus}"

    elif bonus < 0:
        cmd = f"{nombre}d100 - {bonus}"

    else:
        cmd = f"{nombre}d100"

    if len(roll) == 1:
        await ctx.send(f'```# {r1} ({cmd})\nDétails : {txt[: -2]}```')

    elif len(roll) == 2:
        await ctx.send(f'```# {r1}, {r2} ({cmd})\nDétails : {txt[: -2]}```')

    elif len(roll) > 2:
        await ctx.send(f'```# {r1}, {r2}, {r3} ({cmd})\nDétails : {txt[: -2]}```')


# slash command

async def slash_roll(interaction : discord.Interaction, faces : int = 6, nombre : int = 1):
    rolled = []
    a = 0
    b = 0
    total = 0

    for i in range(nombre):
        temp = randint(1, int(faces))
        rolled.append(temp)
        total += temp

    if faces > 2 and nombre > 1:
        moyenne = int(round(total / len(rolled), 0))

        for elt in rolled:
            if elt == 1:
                a += 1

            elif elt == int(faces):
                b += 1

            rolled = str(rolled)

        await interaction.response.send_message(f'```# {rolled[1:-1]}\n{a} échecs critiques - {b} réussites critiques - moyenne : {moyenne}```')

    else:
        rolled = str(rolled)
        await interaction.response.send_message(f'> {rolled[1:-1]} \n{f"> Majorité - {moyenne}" if nombre > 4 else ""}')

async def slash_makai_roll(interaction : discord.Interaction, bonus : int, nombre : app_commands.Choice[int]):
    roll = []
    for i in range(nombre.value):
        roll.append(mk_roll(bonus))
    
    base = 49 + bonus
    dtls = {"réussite critique" : 0, "réussite" : 0, "réussite faible" : 0, "échec" : 0, "échec critique" : 0}

    r1 = roll[0][0][0]
    if r1 < 10:
        dtls['réussite critique'] += 1

    elif r1 < base:
        dtls['réussite'] += 1

    elif r1 == base + 1:
        dtls['réussite faible'] += 1

    elif r1 > 90:
        dtls['échec critique'] += 1

    elif r1 > base:
        dtls['échec'] += 1

    if len(roll) > 1:
        r2 = roll[1][0][0]
        if r2 < 10:
            dtls['réussite critique'] += 1

        elif r2 < base:
            dtls['réussite'] += 1

        elif r2 == base + 1:
            dtls['réussite faible'] += 1

        elif r2 > 90:
            dtls['échec critique'] += 1

        elif r2 > base:
            dtls['échec'] += 1

    if len(roll) > 2:
        r3 = roll[2][0][0]
        if r3 < 10:
            dtls['réussite critique'] += 1

        elif r3 < base:
            dtls['réussite'] += 1

        elif r3 == base + 1:
            dtls['réussite faible'] += 1

        elif r3 > 90:
            dtls['échec critique'] += 1

        elif r3 > base:
            dtls['échec'] += 1

    txt = ""
    for key in dtls.keys():
        if dtls[key] == 1:
            txt += f"1 {key}, "

        elif dtls[key] > 1:
            txt += f"{dtls[key]} {key}s, "

    if bonus > 0:
        cmd = f"{nombre.value}d100 + {bonus}"

    elif bonus < 0:
        cmd = f"{nombre.value}d100 - {bonus}"

    else:
        cmd = f"{nombre.value}d100"

    if len(roll) == 1:
        await interaction.response.send_message(f'```# {r1} ({cmd})\nDétails : {txt[: -2]}```')

    elif len(roll) == 2:
        await interaction.response.send_message(f'```# {r1}, {r2} ({cmd})\nDétails : {txt[: -2]}```')

    elif len(roll) > 2:
        await interaction.response.send_message(f'```# {r1}, {r2}, {r3} ({cmd})\nDétails : {txt[: -2]}```')