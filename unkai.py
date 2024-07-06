# ~ - - - - - - - - - - - - - - - - ~  U N K A I  ~ - - - - - - - - - - - - - - - - ~ #


# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


from discord import *
import discord 
import asyncio
import numpy
import aiohttp
import os
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord.voice_client import VoiceClient
from discord import app_commands
from nacl import *
from time import sleep

# - UNKAI commands

import UNKAI_commands.unkai_help as unkai_help
import UNKAI_commands.unkai_invites as unkai_invites
import UNKAI_commands.unkai_clear as unkai_clear
import UNKAI_commands.unkai_rolls as unkai_rolls
import UNKAI_commands.unkai_jokes as unkai_jokes
import UNKAI_commands.unkai_meteo as unkai_meteo
import UNKAI_commands.unkai_mod as unkai_mod
import UNKAI_commands.unkai_lock as unkai_lock
import UNKAI_commands.unkai_webhooks as unkai_webhooks


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)

embed = discord.Embed(title = "title", description = "description", color = 0x00ffff)
embed.add_field(name = "field", value = "value", inline = False)

bot.remove_command('help')

localhost = False

serveurs = []


# - - - - - - - - - - - - - - - -  C L A S S E S  - - - - - - - - - - - - - - - - #


class Serveur():
    ''' Statut du serveur '''
    
    def __init__(self, id : str):
        self.status = 'unlock'
        self.id = id

    def check_status(self): # True si unlock, False sinon
        return True if self.status == 'unlock' else False

    def status_lock(self):
        self.status = 'lock'
        return 'Serveur verrouillé'

    def status_unlock(self):
        self.status = 'unlock'
        return 'Serveur déverrouillé'

class button_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "Check", style = discord.ButtonStyle.green, custom_id = "verify")
    async def check(self, interaction : discord.Interaction, button : discord.ui.Button):
        role_verify = interaction.guild.get_role(1198947527710478366)
        role_non_verify = interaction.guild.get_role(1198947456302456892)
            
        if role_verify not in interaction.user.roles and role_non_verify in interaction.user.roles:
            await interaction.user.remove_roles(role_non_verify)
            await interaction.user.add_roles(role_verify)
            await interaction.response.send_message(embed = discord.Embed(title = "Check d'entrée", description = "Votre entrée a été confirmée, bienvenue sur le serveur ! 👋", color = 0x74FF33), ephemeral = True)
            
        else:
            await interaction.response.send_message("Ce check ne vous concerne pas...", ephemeral = True)
            
    @discord.ui.button(label = "Leave", style = discord.ButtonStyle.danger, custom_id = "leave")
    async def leave(self, interaction : discord.Interaction, button : discord.ui.Button):
        role_verify = interaction.guild.get_role(1198947527710478366)
        role_non_verify = interaction.guild.get_role(1198947456302456892)
        
        if role_verify not in interaction.user.roles and role_non_verify in interaction.user.roles:
            await interaction.user.kick()
            
        else:
            await interaction.response.send_message("Ce check ne vous concerne pas...", ephemeral = True)


# - - - - - - - - - - - - - - - -  C O M M A N D E S  - - - - - - - - - - - - - - - - #


# PING - mesure du ping (fonctionnel)

@bot.command(name = 'ping')
async def ping(ctx : commands.Context): 
    print(round(bot.latency * 1000), "ms")
    await ctx.send(f'> *{round(bot.latency * 1000)} ms* \n> ||*...pong*||')

@bot.command(name = 'ms')
async def ms(ctx : commands.Context): 
    print(round(bot.latency * 1000), "ms")
    await ctx.send(f'> *{round(bot.latency * 1000)} ms*')

@bot.tree.command(name = 'ms')
async def slash_ms(interaction : discord.Interaction): 
    print(round(bot.latency * 1000), "ms")
    await interaction.response.send_message(f'> *{round(bot.latency * 1000)} ms*')


# HELP - aides : liste des commandes (fonctionnel)

@bot.command(name = 'help')
async def help(ctx : commands.Context, catégorie : str = 'all'):
    if catégorie.lower() == 'meteo':
        await unkai_help.help(ctx, 'meteo')

    elif catégorie.lower() == 'webhooks':
        await unkai_help.help(ctx, 'webhooks')

    else:
        await unkai_help.help(ctx)

@bot.tree.command(name = 'help')
@app_commands.choices(catégorie = [
    app_commands.Choice(name = 'Tout', value = 'all'),
    app_commands.Choice(name = "Météo", value = "meteo"),
    app_commands.Choice(name = "Webhooks", value = "webhooks")])
async def slash_help(interaction : discord.Interaction, catégorie : app_commands.Choice[str] = None): 
    await unkai_help.slash_help(interaction, catégorie.value if catégorie != None else 'all')
    
    
# INFOS - about Unkai (non fonctionnel) / invitations serveurs (fonctionnel)

@bot.tree.command(name = 'info')
async def infos(interaction : discord.Interaction): 
    info_embed = discord.Embed(title = 'À propos de Unkai - More about Unkai', description = '*En cours de création...* \n \n *In cours of creation...*', color = 0x00ffff)
    info_embed.set_author(name = interaction.user.name, icon_url = interaction.user.avatar)

    print(f'{interaction.user.name} veut en savoir plus sur Unkai !')
    await interaction.response.send_message(embed = info_embed)

@bot.command(name = 'link')
async def link(ctx : commands.Context, site : str):
    await unkai_invites.link(ctx, site)

@bot.command(name = 'invite')
async def invitations(ctx : commands.Context, site : str):
    await unkai_invites.link(ctx, site)

@bot.tree.command(name = 'link')
@app_commands.choices(site = [
    app_commands.Choice(name = "Trello", value = "Trello"),
    app_commands.Choice(name = "Github", value = "Github")])
async def slash_link(interaction : discord.Interaction, site : app_commands.Choice[str]):
    await unkai_invites.slash_link(interaction, site.value)

@bot.tree.command(name = 'invite')
@app_commands.choices(serveur = [
    app_commands.Choice(name = "Yōsai", value = "yōsai"),
    app_commands.Choice(name = "Unkai", value = "unkai"),
    app_commands.Choice(name = "Nysux", value = "nysux")])
async def slash_invitations(interaction : discord.Interaction, serveur : app_commands.Choice[str]): 
    await unkai_invites.slash_link(interaction, serveur.value)


# CLEAR - suppression de messages (fonctionnel)

@bot.command(name = 'clear') 
async def clear(ctx : commands.Context, nombre : int = 1):
    await unkai_clear.clear(ctx, nombre)

@bot.tree.command(name = 'clear')
@app_commands.checks.has_permissions(manage_messages = True)
async def slash_clear(interaction : discord.Interaction, nombre : int = 1) : 
    await unkai_clear.slash_clear(interaction, nombre) 


# ROLLS - tirages aléatoires (fonctionnel)

@bot.command(name = 'roll')
async def dés_roll(ctx : commands.Context, faces : int = 6, nombre : int = 1):
    await unkai_rolls.roll(ctx, faces, nombre)

@bot.tree.command(name = 'roll')
async def slash_dés_roll(interaction : discord.Interaction, faces : int = 6, nombre : int = 1):
    await unkai_rolls.slash_roll(interaction, faces, nombre)

@bot.command(name = 'makai_roll')
async def makai_roll(ctx : commands.Context, bonus : int, nombre : int = 1):
    nombre = 1 if nombre < 1 else nombre
    nombre = 3 if nombre > 3 else nombre

    await unkai_rolls.makai_roll(ctx, bonus, nombre)

@bot.tree.command(name = 'makai_roll')
@app_commands.choices(nombre = [app_commands.Choice(name = "1", value = 1),
                                app_commands.Choice(name = "2", value = 2),
                                app_commands.Choice(name = "3", value = 3)])
async def slashmakai_roll(interaction : discord.Interaction, bonus : int, nombre : app_commands.Choice[int]):
    await unkai_rolls.slash_makai_roll(interaction, bonus, nombre)


# JOKES - blagues (fonctionnel)
    
@bot.command(name = 'joke')
async def blague(ctx : commands.Context):
    await unkai_jokes.joke(ctx)

@bot.tree.command(name = 'joke')
async def slash_blague(interaction : discord.Interaction): 
    await unkai_jokes.slash_joke(interaction)


# NARRATION - narration (fonctionnel / v1)

@bot.command(name = 'nar') 
async def narration(ctx : commands.Context, * , nar): 
    if len(nar) < 100:
        print(f'Envois du message : {nar}')

    else:
        msg = nar[0:100]
        print(f'Envois du message : {msg} ...')

    await ctx.message.delete()    
    await ctx.send(nar)

@bot.command(name = 'e_nar')
async def embed_narration(ctx : commands.Context, titre,  * , nar): 
    if len(nar) < 100:
        print(f'Envois du message : {nar} (embed)')

    else:
        msg = nar[0:100]
        print(f'Envois du message : {msg} ... (embed)')

    await ctx.message.delete()    
    await ctx.send(embed = discord.Embed(title = titre, description = nar, color=0x00ffff))


# METEO RP - last update = v2

@bot.command(name = 'meteo')
@has_permissions(administrator = True)
async def meteo(ctx : commands.Context, nom : str, climat : int, saison : int, durée : int, last_temp : float = None) : # météo avec températures (fonctionnel)
    await unkai_meteo.meteo(ctx, nom, climat, saison, durée, last_temp)

@bot.tree.command(name = 'meteo')
@app_commands.checks.has_permissions(administrator = True)
async def slash_meteo(interaction : discord.Interaction, nom : str, climat : int, saison : int, durée : int, dernière_température : float = None) : # météo avec températures (fonctionnel)
    await unkai_meteo.slash_meteo(interaction, nom, climat, saison, durée, dernière_température)


# MODERATION - kick/ban (fonctionnel)

@bot.command(name = 'kick')
@has_permissions(kick_members = True)
async def kick(ctx : commands.Context, member : discord.Member, * , reason = 'aucune raison spécifiée') : 
    await unkai_mod.kick(ctx, member, reason, 1)

@bot.command(name = 'ban')
@has_permissions(ban_members = True)
async def ban(ctx : commands.Context, member : discord.Member, * , reason = 'aucune raison spécifiée') : 
    await unkai_mod.kick(ctx, member, reason, 2)

@bot.tree.command(name = 'kick')
@app_commands.checks.has_permissions(kick_members = True)
async def slash_kick(interaction : discord.Interaction, membre : discord.Member, raison : str = 'aucune raison spécifiée') : 
    await unkai_mod.slash_kick(interaction, membre, raison, 1)

@bot.tree.command(name = 'ban')
@app_commands.checks.has_permissions(ban_members = True)
async def slash_ban(interaction : discord.Interaction, membre : discord.Member, raison : str = 'aucune raison spécifiée') :
    await unkai_mod.slash_kick(interaction, membre, raison, 2)

@bot.command(name = 'kick_role')
@has_permissions(administrator = True)
async def kick_role(ctx, role : discord.Role, * , reason = 'aucune raison spécifiée') :
    namekick = f'Les membres possédant le rôle "{role}" ont été expulsés du serveur'
    reasonkick = f'**Raison :** {reason}'

    for membre in ctx.guild.members:
        if role in membre.roles:

            try:
                await membre.send(embed=discord.Embed(title = 'Vous avez été expulsé du serveur', description = reasonkick, color = 0x00ffff))
            
            except:
                pass

            await ctx.guild.kick(membre, reason = reason)

    await ctx.send(embed=discord.Embed(title = namekick, description = reasonkick, color = 0x00ffff))


# ANTI-RAID - activation/désactivation anti-raid (fonctionnel)
    
@bot.command(name = 'lock')
@has_permissions(administrator = True)
async def lock(ctx : commands.Context) : 
    await unkai_lock.lock(ctx, serveurs)

@bot.command(name = 'unlock')
@has_permissions(administrator = True)
async def unlock(ctx : commands.Context) : 
    await unkai_lock.unlock(ctx, serveurs)

@bot.tree.command(name = 'lock')
@app_commands.checks.has_permissions(administrator = True)
async def lock(interaction) : 
    await unkai_lock.slash_lock(interaction, serveurs)

@bot.tree.command(name = 'unlock')
@app_commands.checks.has_permissions(administrator = True)
async def unlock(interaction) : 
    await unkai_lock.slash_unlock(interaction, serveurs)


# WEBHOOKS

@bot.command(name = "wbk_create")
async def create_wbk(ctx : commands.Context, nom : str, tag : str): # Enregistrement d'un webhook dans la DB (fonctionnel)
    avatar = None

    if ctx.message.attachments != []:
        await ctx.message.attachments[0].save("bot UNKAI\\temp_file.png")

        channel = bot.get_channel(1206621721541484607)
        image = await channel.send(file = discord.File("bot UNKAI\\temp_file.png"))
        avatar = image.attachments[0].url

        os.remove("bot UNKAI\\temp_file.png")

    await unkai_webhooks.register(ctx, nom, tag, avatar)

@bot.tree.command(name = "wbk_create")
async def slash_create_wbk(interaction : discord.Interaction, nom : str, tag : str): # Enregistrement d'un webhook dans la DB (sans avatar / fonctionnel)
    await unkai_webhooks.slash_register(interaction, nom, tag)

@bot.command(name = "wbk_list")
async def wbk_list(ctx : commands.Context):
    await unkai_webhooks.webhooks_list(ctx)

@bot.tree.command(name = "wbk_list")
async def slash_wbk_list(interaction : discord.Interaction): # Liste les webhooks d'un compte (fonctionnel)
    await unkai_webhooks.slash_webhooks_list(interaction)

@bot.command(name = "wbk_del")
async def del_wbk(ctx : commands.Context, name : str):
    await unkai_webhooks.unregister(ctx, name)

@bot.tree.command(name = "wbk_del")
async def slash_del_wbk(interaction : discord.Interaction, name : str): # Suppression d'un webhook (fonctionnel)
    await unkai_webhooks.slash_unregister(interaction, name)

@bot.command(name = "wbk_avatar")
async def edit_wbk_avatar(ctx : commands.Context, name : str): # Modification de l'avatar (fonctionnel / no slash command)
    if ctx.message.attachments != []:
        await ctx.message.attachments[0].save("bot UNKAI\\temp_file.png")

        channel = bot.get_channel(1206621721541484607)
        image = await channel.send(file = discord.File("bot UNKAI\\temp_file.png"))
        avatar = image.attachments[0].url

        os.remove("bot UNKAI\\temp_file.png")
        await unkai_webhooks.avatar_edit(ctx, name, avatar)

    else:
        await ctx.send("Une image est nécessaire pour modifier l'avatar...")

@bot.command(name = "wbk_rename")
async def edit_wbk_name(ctx : commands.Context, name : str, new_name : str):
    await unkai_webhooks.name_edit(ctx, name, new_name)

@bot.tree.command(name = "wbk_rename")
async def slash_edit_wbk_name(interaction : discord.Interaction, name : str, new_name : str): # Modification du nom (fonctionnel)
    await unkai_webhooks.slash_name_edit(interaction, name, new_name)

@bot.command(name = "wbk_tag")
async def edit_wbk_name(ctx : commands.Context, name : str, new_tag : str):
    await unkai_webhooks.tag_edit(ctx, name, new_tag)

@bot.tree.command(name = "wbk_tag")
async def slash_edit_wbk_name(interaction : discord.Interaction, name : str, new_tag : str): # Modification du tag (fonctionnel)
    await unkai_webhooks.slash_tag_edit(interaction, name, new_tag)

@bot.command(name = "wbk_search")
async def search_wbk(ctx : commands.Context, name : str):
    await unkai_webhooks.search(ctx, name)

@bot.tree.command(name = "wbk_search")
async def slash_search_wbk(interaction : discord.Interaction, name : str): # Liste les webhooks correspondants (fonctionnel)
    await unkai_webhooks.slash_search(interaction, name)


# - - - - - - - - - - - - - - - -  E V E N T S  - - - - - - - - - - - - - - - - #


@bot.event
async def on_ready():
    await bot.tree.sync()
    activity = discord.Game(name = "/help")
    await bot.change_presence(status = discord.Status.idle, activity = activity)

    for guild in bot.guilds: # Initialisation de l'anti-raid
        serveurs.append(Serveur(guild.id))

    print(f'Initialisation terminée ! \n{round(bot.latency * 1000)} ms - {len(serveurs)} serveurs')

@bot.event
async def on_message(message): # réaction aux messages (fonctionnel)
    await bot.process_commands(message)
    global localhost

    if localhost:
        await unkai_webhooks.check_message(message) # - Webhooks
    
    list_words = ['hey', 'heya', 'hello', 'yo', 'yop', 'coucou', 'cc', 'bonjour', 'bjr', 'bonsoir', 'bsr', 'salutation', 'salutations', 'salut', 'slt', 'salute', 're', 'wesh', 'wsh', 'salam']

    if message.content.lower() in list_words:
        await message.add_reaction("👋")
    
        if message.author.id == 489470853072027685:
            print(f'Moeru dit "{message.content.lower()}" !')
            await message.reply(f'{message.content} ô Moeru 👋')
        
        else:
            print(f'{message.author} dit "{message.content.lower()}"')

@bot.event
async def on_message_edit(before, after): # réaction aux messages (fonctionnel)
    list_words = ['hey', 'heya', 'hello', 'yo', 'yop', 'coucou', 'cc', 'bonjour', 'bjr', 'bonsoir', 'bsr', 'salutation', 'salutations', 'salut', 'slt', 'salute', 're', 'wesh', 'wsh', 'salam']
    Before = before.content.lower()
    After = after.content.lower()

    if Before in list_words and After in list_words:
        pass

    elif Before not in list_words and After in list_words:
        await after.add_reaction("👋")
    
        if after.author.id == 489470853072027685:
            await after.reply(f'{after.content} ô Moeru 👋')
    
    elif Before in list_words and After not in list_words:
        await after.remove_reaction(member = id('864220103113834516'), emoji = "👋")

@bot.event     
async def on_member_join(member : discord.Member): # bienvenue (fonctionnel)
    print(f'{member} a rejoint un de nos serveurs ({member.guild})')
    lock = False

    for serveur in serveurs: # Anti-raid (fonctionnel)
        if member.guild.id == serveur.id and serveur.status == 'lock':
            try: 
                await member.send(f'Le serveur est actuellement verrouillé') 
            
            except: 
                pass
            
            await member.guild.kick(user = member, reason = 'Le serveur est actuellement verrouillé')
            lock = True

    if not lock:
        try: # Message de bienvenue - mp
            await member.send("Bienvenue sur notre serveur !") 

        except: 
            pass
    
        if member.guild.id == 1155450091398758460: # Vérification d'entrée (en test sur SDM)
            role = discord.utils.get(member.guild.roles, name = "Unchecked")
            await member.add_roles(role)
            loc = bot.get_channel(1198949752725831700)
            await loc.send(f"> {member.mention} - Suppression dans 60 secondes", delete_after = 60, embed = discord.Embed(title = "Check d'entrée", description = "Pour valider votre entrée sur le serveur, veuillez intéragir avec le bouton **Check**. Celui-ci vous donnera le rôle <@&1198947527710478366> et par la même occasion l'accès au serveur.", color = 0xFF3333), view = button_view())

@bot.event
async def on_member_remove(member): # adieu (fonctionnel)
    print(f'{member} a quitté un de nos serveurs ({member.guild})')


# - - - - - - - - - - - - - - - -  T O K E N  - - - - - - - - - - - - - - - - #


bot.run("TOKEN")


# - - - - - - - - - - - - - - - -  I N F O R M A T I O N S  - - - - - - - - - - - - - - - - #

# > Actual version - 2 
# > Uid - 1
# > Creation - 2021/07 