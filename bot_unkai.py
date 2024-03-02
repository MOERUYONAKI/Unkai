# ~ - - - - - - - - - - - - - - - - ~  U N K A I  ~ - - - - - - - - - - - - - - - - ~ #


# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


from discord import *
import discord 
import ffmpeg
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
import ffmpeg.audio
from random import randint
from time import *
import rolls as r


# - UNKAI commands

import UNKAI_commands.unkai_help as unkai_help
import UNKAI_commands.unkai_invites as unkai_invites
import UNKAI_commands.unkai_clear as unkai_clear
import UNKAI_commands.unkai_jokes as unkai_jokes
import UNKAI_commands.unkai_meteo as unkai_meteo
import UNKAI_commands.unkai_mod as unkai_mod
import UNKAI_commands.unkai_lock as unkai_lock
import UNKAI_commands.unkai_webhooks as unkai_webhooks


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)

embed = discord.Embed(title = "title", description = "description", color = 0x00ffff)
embed.add_field(name = "field", value = "value", inline = False)

bot.remove_command('help')

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


# HELP - last update = v2

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
async def slash_help(interaction : discord.Interaction, catégorie : app_commands.Choice[str] = None): # aides : liste des commandes (fonctionnel)
    await unkai_help.slash_help(interaction, catégorie.value if catégorie != None else 'all')


# PING - last update = v2

@bot.command(name = 'ping')
async def ping(ctx : commands.Context): # mesure du ping (fonctionnel)
    print(round(bot.latency * 1000), "ms")
    await ctx.send(f'> *{round(bot.latency * 1000)} ms* \n> ||*...pong*||')

@bot.command(name = 'ms')
async def ms(ctx : commands.Context): # mesure du ping (fonctionnel)
    print(round(bot.latency * 1000), "ms")
    await ctx.send(f'> *{round(bot.latency * 1000)} ms*')

@bot.tree.command(name = 'ms')
async def slash_ms(interaction : discord.Interaction): # mesure du ping (fonctionnel)
    print(round(bot.latency * 1000), "ms")
    await interaction.response.send_message(f'> *{round(bot.latency * 1000)} ms*')


# INFOS - last update = v2

@bot.tree.command(name = 'info')
async def infos(interaction : discord.Interaction): # About Unkai (non fonctionnel)
    info_embed = discord.Embed(title = 'À propos de Unkai - More about Unkai', description = '*En cours de crétion...* \n \n *In cours of creation...*', color = 0x00ffff)
    info_embed.set_author(name = interaction.user.name, icon_url = interaction.user.avatar_url)

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
async def slash_invitations(interaction : discord.Interaction, serveur : app_commands.Choice[str]): # invitations serveurs (fonctionnel)
    await unkai_invites.slash_link(interaction, serveur.value)    


# CLEAR - last update = v2

@bot.command(name = 'clear') 
async def clear(ctx : commands.Context, nombre : int = 1):
    await unkai_clear.clear(ctx, nombre)

@bot.tree.command(name = 'clear')
@has_permissions(manage_messages = True)
async def suppression(interaction : discord.Interaction, nombre : int = 1) : # suppression de messages (fonctionnel)
    await unkai_clear.slash_clear(interaction, nombre) 


# ROLLS - last update = v1

@bot.tree.command(name = 'roll')
async def dés_roll_slash(interaction : discord.Interaction, arg1 : int = 6, arg2 : int = 1):
    rolled = []
    a = 0
    b = 0
    for i in range(arg2):
        temp = randint(1, int(arg1))
        rolled.append(temp)

    if arg1 > 2:
        for elt in rolled:
            if elt == 1:
                a += 1

            elif elt == int(arg1):
                b += 1

            rolled = str(rolled)
        await interaction.response.send_message(f'> {rolled[1:-1]}\n{a} échecs critiques - {b} réussites critiques')

    else:
        rolled = str(rolled)
        await interaction.response.send_message(f'> {rolled[1:-1]}')

@bot.tree.command(name = 'roll_2')
@app_commands.choices(nombre = [app_commands.Choice(name = "1", value = 1),
                                app_commands.Choice(name = "2", value = 2),
                                app_commands.Choice(name = "3", value = 3)])
async def makai_roll(interaction : discord.Interaction, bonus : int, nombre : app_commands.Choice[int]):
    roll = []
    for i in range(nombre.value):
        roll.append(r.Makai_roll(bonus))
    
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


# NARRATION - last update = v1

@bot.command(name = 'nar') 
async def narration(ctx : commands.Context, * , nar): # narration (fonctionnel)
    if len(nar) < 100:
        print(f'Envois du message : {nar}')

    else:
        msg = nar[0:100]
        print(f'Envois du message : {msg} ...')

    await ctx.message.delete()    
    await ctx.send(nar)

@bot.command(name = 'e-nar')
async def embed_narration(ctx : commands.Context, titre,  * , nar): # embed narration (fonctionnel)
    if len(nar) < 100:
        print(f'Envois du message : {nar} (embed)')

    else:
        msg = nar[0:100]
        print(f'Envois du message : {msg} ... (embed)')

    await ctx.message.delete()    
    await ctx.send(embed = discord.Embed(title = titre, description = nar, color=0x00ffff))


# JOKES - last update = v2
    
@bot.command(name = 'joke')
async def blague(ctx : commands.Context):
    await unkai_jokes.joke(ctx)

@bot.tree.command(name = 'joke')
async def slash_blague(interaction : discord.Interaction): # blagues (fonctionnel)
    await unkai_jokes.slash_joke(interaction)


# METEO RP - last update = v2

@bot.command(name = 'meteo')
@has_permissions(administrator = True)
async def meteo(ctx : commands.Context, nom : str, climat : int, saison : int, durée : int, last_temp : float = None) : # météo avec températures (fonctionnel)
    await unkai_meteo.meteo(ctx, nom, climat, saison, durée, last_temp)

@bot.tree.command(name = 'meteo')
@has_permissions(administrator = True)
async def slash_meteo(interaction : discord.Interaction, nom : str, climat : int, saison : int, durée : int, dernière_température : float = None) : # météo avec températures (fonctionnel)
    await unkai_meteo.slash_meteo(interaction, nom, climat, saison, durée, dernière_température)


# MODERATION - last update = v2

@bot.command(name = 'kick')
@has_permissions(kick_members = True)
async def kick(ctx : commands.Context, member : discord.Member, * , reason = 'aucune raison spécifiée') : # kick un membre (fonctionnel)
    await unkai_mod.kick(ctx, member, reason, 1)

@bot.command(name = 'ban')
@has_permissions(ban_members = True)
async def ban(ctx : commands.Context, member : discord.Member, * , reason = 'aucune raison spécifiée') : # ban un membre (fonctionnel)
    await unkai_mod.kick(ctx, member, reason, 2)

@bot.tree.command(name = 'kick')
@has_permissions(kick_members = True)
async def slash_kick(interaction : discord.Interaction, membre : discord.Member, raison : str = 'aucune raison spécifiée') : # kick un membre (fonctionnel)
    await unkai_mod.slash_kick(interaction, membre, raison, 1)

@bot.tree.command(name = 'ban')
@has_permissions(ban_members = True)
async def slash_ban(interaction : discord.Interaction, membre : discord.Member, raison : str = 'aucune raison spécifiée') : # ban un membre (fonctionnel)
    await unkai_mod.slash_kick(interaction, membre, raison, 2)

@bot.command(name = 'kick_role')
@has_permissions(administrator = True)
async def kick_role(ctx, role : discord.Role, * , reason = 'aucune raison spécifiée') : # kick tout les membres possédant le rôle demandé (fonctionnel)
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


# ANTI-RAID - last update = v2
    
@bot.command(name = 'lock')
@has_permissions(administrator = True)
async def lock(ctx : commands.Context) : # Activation anti-raid (fonctionnel)
    await unkai_lock.lock(ctx, serveurs)

@bot.command(name = 'unlock')
@has_permissions(administrator = True)
async def unlock(ctx : commands.Context) : # Désactivation anti-raid (fonctionnel)
    await unkai_lock.unlock(ctx, serveurs)

@bot.tree.command(name = 'lock')
@has_permissions(administrator = True)
async def lock(interaction) : # Activation anti-raid (fonctionnel)
    await unkai_lock.slash_lock(interaction, serveurs)

@bot.tree.command(name = 'unlock')
@has_permissions(administrator = True)
async def unlock(interaction) : # Désactivation anti-raid (fonctionnel)
    await unkai_lock.slash_unlock(interaction, serveurs)


# WEBHOOKS - last update = v2

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
async def edit_wbk_avatar(ctx : commands.Context, name : str): # Modification de l'avatar (fonctionnel)
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


# AUTRE - last update = v1

@bot.command(name = 'spam')
@has_permissions(administrator = True)
async def spam(ctx : commands.Context, arg1, arg2 : int): # Spam un message donné (fonctionnel)
    for i in range(arg2):
        await ctx.send(f'{arg1}') 

    await ctx.send(f'Spammé {arg2} fois !')
    print(arg1, "spammé", arg2, "fois !") 


# - - - - - - - - - - - - - - - -  E V E N T S  - - - - - - - - - - - - - - - - #


@bot.event
async def on_ready():
    await bot.tree.sync()
    activity = discord.Game(name = "/help")
    await bot.change_presence(status = discord.Status.idle, activity = activity)

    print('Le bot est prêt !')
    print(round(bot.latency * 1000), "ms")

    for guild in bot.guilds: # Initialisation de l'anti-raid
        serveurs.append(Serveur(guild.id))

@bot.event
async def on_message(message): # réaction aux messages (fonctionnel)
    await bot.process_commands(message)
    await unkai_webhooks.check_message(message) # - Webhooks

    list_words = ['hey', 'yo', 'yop', 'coucou', 'cc', 'bonjour', 'bjr', 'bonsoir', 'bsr', 'salutation', 'salutations', 'salut', 'slt', 're', 'wesh', 'wsh', 'salam']

    if message.content.lower() in list_words:
        await message.add_reaction("👋")
    
        if message.author.id == 489470853072027685:
            print(f'Moeru dit "{message.content.lower()}" !')
            await message.reply(f'{message.content} ô Moeru 👋')
        
        else:
            print(f'{message.author} dit "{message.content.lower()}"')

@bot.event
async def on_message_edit(before, after): # réaction aux messages (fonctionnel)
    list_words = ['hey', 'yo', 'coucou', 'cc', 'bonjour', 'bjr', 'bonsoir', 'bsr', 'salutation', 'salutations', 'salut', 'slt', 're', 'wesh', 'wsh', 'salam']
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

    elif After == 'quoi':
        msg = await after.reply("feur")
        sleep(1.5)
        await msg.delete()

@bot.event     
async def on_member_join(member : discord.Member): # bienvenue (fonctionnel)
    print(f'{member} a rejoint un de nos serveurs ({member.guild})')

    try: # Message de bienvenue - mp
        await member.send("Bienvenue sur notre serveur !") 

    except: 
        pass
    
    if member.guild.id == 1155450091398758460: # Vérification d'entrée (en test sur SDM)
        role = discord.utils.get(member.guild.roles, name = "Unchecked")
        await member.add_roles(role)
        loc = bot.get_channel(1198949752725831700)
        await loc.send(f"> {member.mention} - Suppression dans 60 secondes", delete_after = 60, embed = discord.Embed(title = "Check d'entrée", description = "Pour valider votre entrée sur le serveur, veuillez intéragir avec le bouton **Check**. Celui-ci vous donnera le rôle <@&1198947527710478366> et par la même occasion l'accès au serveur.", color = 0xFF3333), view = button_view())

    for serveur in serveurs: # Anti-raid (fonctionnel)
        if member.guild.id == serveur.id and serveur.status == 'lock':
            try: 
                await member.send(f'Le serveur est actuellement verrouillé') 
            
            except: 
                pass
            
            await member.guild.kick(user = member, reason = 'Le serveur est actuellement verrouillé')

@bot.event
async def on_member_remove(member): # adieu (fonctionnel)
    print(f'{member} a quitté un de nos serveurs ({member.guild})')


# - - - - - - - - - - - - - - - -  E N   T E S T  - - - - - - - - - - - - - - - - #


@bot.command(name = 'play')
async def play(ctx : commands.Context, * , arg): # joue la musique demandée dans un salon vocal (non fonctionnel)
    channel = ctx.message.author.voice.channel
    await channel.connect()

    if arg.lower() == 'dead to me':
        await play(discord.FFmpegPCMAudio(source = 'bot UNKAI\\songs\\Sex Whales & Fraxo - Dead to me.wav', executable = 'C:\\users\\1bbor\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\\localcache\\local-packages\\python39\\site-packages\\ffmpeg'))
    
    else:
        await ctx.send(f'Nom invalide')

@bot.command(name = 'katsu_roll')
async def katsu_roll(ctx : commands.Context, msg):
    roll = r.Katsu_roll(msg)
    if type(roll) is list:
        cmd = ''
        if msg[0] == 'd':
            for elt in roll[0][1 : len(roll[0])]:
                cmd += str(elt)
                
        else:
            for elt in roll[0]:
                cmd += str(elt)
        
        results = 0
        rolls = ""
        for i in range(len(roll[1])):
            results += roll[1][i][1]
            if i == 0:
                rolls += str(roll[1][i][0])
            
            else:
                rolls += ", " + str(roll[1][i][0])
            
        await ctx.send(f'```# {results}\nDétails : {cmd} ({rolls})```')
            
    else:
        await ctx.send(roll)

@bot.command(name = 'reset_role')
@has_permissions(administrator = True)
async def kick_role(ctx : commands.Context, role : discord.Role, * , reason = 'aucune raison spécifiée'): # reset les rôles de tout les membres possédant le rôle demandé (non fonctionnel)
    namekick = f'Les rôles des membres possédant le rôle "{role}" ont été réinitialisés'
    reasonkick = f'**Raison :** {reason}'

    for membre in ctx.guild.members:
        if role in membre.roles:
            for r in membre.roles:
                r = discord.utils.get(ctx.guild.roles, id = r)
                await membre.remove_roles(r)
                
            rl = discord.utils.get(ctx.guild.roles, id = 872067134811938867)
            await membre.add_roles(rl)

    await ctx.send(embed=discord.Embed(title = namekick, description = reasonkick, color = 0x00ffff))

@bot.command(name = 'give_all')
@has_permissions(administrator = True)
async def give_role(ctx : commands.Context, role : discord.Role):
    for membre in ctx.guild.members:
        if role not in membre.roles:
            await membre.add_roles(role)

    await ctx.send(f'Le rôle **{role}** a été ajouté à tout les membres avec succès !')


# - - - - - - - - - - - - - - - -  T O K E N  - - - - - - - - - - - - - - - - #


# Sécurisation du Token 
from unkai_tk import TOKEN
bot.run(TOKEN)


# - - - - - - - - - - - - - - - -  I N F O R M A T I O N S  - - - - - - - - - - - - - - - - #

# > Actual version - 2 
# > Uid - 1
# > Creation - 2021/07 
# > Total scripts - 11 