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

async def link(ctx : commands.Context, site : str):
    site = site.lower()
    
    if site == 'trello':
        await ctx.send(f'Voici le lien vers ma page Trello : \n> https://trello.com/invite/b/A8X0t81i/b8a12886e485b7b0bfa623b679b1b6d1/unkai')

    elif site == 'github':
        await ctx.send(f'Voici le lien du Github de mon créateur : \n> https://github.com/MOERUYONAKI')

    elif site == "yōsai":
        await ctx.send("Voilà le lien de Yōsai : \n> https://discord.gg/pVGppPrYvj")
        print('invitation sur Yōsai envoyée')

    elif site == "unkai":
        await ctx.send("Voilà le lien de [Unkai](https://discord.com/oauth2/authorize?client_id=864220103113834516) : \n> https://discord.gg/CDN88EtgSU")
        print('invitation sur Unkai envoyée')

    elif site == "nysux":
        await ctx.send("Voilà le lien de Nysux : \n> https://discord.gg/VyFpt4qG5J")
        print('invitation sur Nysux envoyée')

    elif site == "izaria":
        await ctx.send("Voilà le lien de Izaria : \n> https://discord.gg/e5GkEtA3fq")
        print('invitation sur Izaria envoyée')

    else :
        await ctx.send("Une erreur est survenue...")
        print('erreur : nom manquant ou incorrect')


# slash command

async def slash_link(interaction : discord.Interaction, site : str):
    if site == 'Trello':
        await interaction.response.send_message(f'Voici le lien vers ma page Trello : \n> https://trello.com/invite/b/A8X0t81i/b8a12886e485b7b0bfa623b679b1b6d1/unkai', ephemeral = True)

    elif site == 'Github':
        await interaction.response.send_message(f'Voici le lien du Github de mon créateur : \n> https://github.com/MOERUYONAKI', ephemeral = True)

    elif site == "yōsai":
        await interaction.response.send_message("Voilà le lien de Yōsai : \n> https://discord.gg/pVGppPrYvj", ephemeral = True)
        print('invitation sur Yōsai envoyée')

    elif site == "unkai":
        await interaction.response.send_message("Voilà le lien de [Unkai](https://discord.com/oauth2/authorize?client_id=864220103113834516) : \n> https://discord.gg/CDN88EtgSU", ephemeral = True)
        print('invitation sur Unkai envoyée')

    elif site == "nysux":
        await interaction.response.send_message("Voilà le lien de Nysux : \n> https://discord.gg/VyFpt4qG5J", ephemeral = True)
        print('invitation sur Nysux envoyée')

    else :
        await interaction.response.send_message("Une erreur est survenue...", ephemeral = True)
        print('erreur : nom manquant ou incorrect')