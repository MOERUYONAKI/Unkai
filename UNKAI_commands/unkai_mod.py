from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from time import *

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# base command

async def kick(ctx : commands.Context, member : discord.Member, reason : str, id : int):
    reasonkick = f'**Raison :** {reason}'

    if id == 1:
        namekick = f'{member} a été expulsé du serveur'

    elif id == 2:
        namekick = f'{member} a été banni du serveur'


    try:
        if id == 1:
            await member.send(embed = discord.Embed(title = 'Vous avez été expulsé du serveur', description = reasonkick, color = 0x00ffff))
        
        elif id == 2:
            await member.send(embed = discord.Embed(title = 'Vous avez été banni du serveur', description = reasonkick, color = 0x00ffff))

    except:
        pass
    
    if id == 1:
        await ctx.guild.kick(member, reason = reason)

    elif id == 2:
        await ctx.guild.ban(member, reason = reason)

    await ctx.send(embed = discord.Embed(title = namekick, description = reasonkick, color = 0x00ffff))


# slash command

async def slash_kick(interaction : discord.Interaction, member : discord.Member, reason : str, id : int):
    reasonkick = f'**Raison :** {reason}'

    if id == 1:
        namekick = f'{member} a été expulsé du serveur'

    elif id == 2:
        namekick = f'{member} a été banni du serveur'


    try:
        if id == 1:
            await member.send(embed = discord.Embed(title = 'Vous avez été expulsé du serveur', description = reasonkick, color = 0x00ffff))
        
        elif id == 2:
            await member.send(embed = discord.Embed(title = 'Vous avez été banni du serveur', description = reasonkick, color = 0x00ffff))

    except:
        pass
    
    if id == 1:
        await interaction.guild.kick(member, reason = reason)

    elif id == 2:
        await interaction.guild.ban(member, reason = reason)

    await interaction.response.send_message(embed = discord.Embed(title = namekick, description = reasonkick, color = 0x00ffff))