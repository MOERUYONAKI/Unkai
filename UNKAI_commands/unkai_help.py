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

async def help(ctx, catégorie : str = 'all'): # aides : liste des commandes (fonctionnel)
    if catégorie == 'all':
        embed = discord.Embed(title = 'Commandes :', color = 0x00ffff)
        embed.add_field(name = "> **ms**", value = "Mesure du ping", inline = False)
        embed.add_field(name = "> **joke**", value = "Envoie une blague", inline = False)
        embed.add_field(name = "> **invite** *[serveur]*", value = "Envoie le lien d'invitation du serveur demandé", inline = False)
        embed.add_field(name = '> **clear** *[nombre de messages]*', value = "Supprime le nombre demandé de messages", inline = False)
        embed.add_field(name = '> **nar** *[texte]*', value = "Renvoie du message par le narrateur", inline = False)
        embed.add_field(name = '> **e-nar** *[texte]*', value = "Renvoie du message par le narrateur (embed)", inline = False)
        embed.add_field(name = "> **roll** *[maximum]* *[nombre de lancers]*", value = "Calcule un nombre aléatoire entre 1 et le maximum le nombre de fois demandé", inline = False)
        embed.add_field(name = '> **meteo** *[nom de la région] [climat] [durée]*', value = "Crée une météo selon le climat sur une durée de 1 à 7 jours", inline = False)
        embed.add_field(name = '> **kick** *[utilisateur] [raison]*', value = "Exclut l'utilisateur du serveur", inline = False)
        embed.add_field(name = '> **ban** *[utilisateur] [raison]*', value = "Banni l'utilisateur du serveur", inline = False)
        
        await ctx.send(embed = embed)
    
    elif catégorie.value == 'meteo':
        await ctx.send(embed = discord.Embed(title = 'Météo :', description = '> **meteo** *[nom de la région] [climat] [durée]*' + '\n' + "Crée une météo selon le climat sur une durée de 1 à 7 jours" + '\n' + '\n' + "> **nom de la région**" + '\n' + "Choix du nom affiché sur la météo" + '\n' + '\n' + "> **climat**" + '\n' + "Choix du climat entre 'desert', 'temperate', 'cold' ou un nom secret" + '\n' + '\n' + "> **durée**" + '\n' + "Choix du nombre de jours de météo entre 1 et 7 jours", color = 0x00ffff))
    
    print("Envoie d'un coup de main")


# slash command

async def slash_help(interaction : discord.Interaction, catégorie : str = 'all'): # aides : liste des commandes (fonctionnel)
    if catégorie == 'all':
        embed = discord.Embed(title = 'Commandes :', color = 0x00ffff)
        embed.add_field(name = "> **ms**", value = "Mesure du ping", inline = False)
        embed.add_field(name = "> **joke**", value = "Envoie une blague", inline = False)
        embed.add_field(name = "> **invite** *[serveur]*", value = "Envoie le lien d'invitation du serveur demandé", inline = False)
        embed.add_field(name = '> **clear** *[nombre de messages]*', value = "Supprime le nombre demandé de messages", inline = False)
        embed.add_field(name = '> **nar** *[texte]*', value = "Renvoie du message par le narrateur", inline = False)
        embed.add_field(name = '> **e-nar** *[texte]*', value = "Renvoie du message par le narrateur (embed)", inline = False)
        embed.add_field(name = "> **roll** *[maximum]* *[nombre de lancers]*", value = "Calcule un nombre aléatoire entre 1 et le maximum le nombre de fois demandé", inline = False)
        embed.add_field(name = '> **meteo** *[nom de la région] [climat] [durée]*', value = "Crée une météo selon le climat sur une durée de 1 à 7 jours", inline = False)
        embed.add_field(name = '> **kick** *[utilisateur] [raison]*', value = "Exclut l'utilisateur du serveur", inline = False)
        embed.add_field(name = '> **ban** *[utilisateur] [raison]*', value = "Banni l'utilisateur du serveur", inline = False)
        
        await interaction.response.send_message(embed = embed)
    
    elif catégorie.value == 'meteo':
        await interaction.response.send_message(embed = discord.Embed(title = 'Météo :', description = '> **meteo** *[nom de la région] [climat] [durée]*' + '\n' + "Crée une météo selon le climat sur une durée de 1 à 7 jours" + '\n' + '\n' + "> **nom de la région**" + '\n' + "Choix du nom affiché sur la météo" + '\n' + '\n' + "> **climat**" + '\n' + "Choix du climat entre 'desert', 'temperate', 'cold' ou un nom secret" + '\n' + '\n' + "> **durée**" + '\n' + "Choix du nombre de jours de météo entre 1 et 7 jours", color = 0x00ffff))
    
    print("Envoie d'un coup de main")