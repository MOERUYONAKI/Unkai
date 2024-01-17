# ~ - - - - - - - - - - - - - - - - ~  U N K A I   A G A I N  ~ - - - - - - - - - - - - - - - - ~ #


# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


from discord import *
import discord 
import asyncio
import numpy
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord.voice_client import VoiceClient
# from nacl import *
from random import randint
from time import *
from Autres.météo import create
from Succes.succes import *
import Succes.succes_logs as succes_logs
import Autres.rolls as r


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)
bot.remove_command('help')

embed = discord.Embed(title = "title", description = "description", color = 0x00ffff)
embed.add_field(name = "field", value = "value", inline = False)


# - - - - - - - - - - - - - - - -  C L A S S E S  - - - - - - - - - - - - - - - - #


class check_view(discord.ui.View): # Check buttons 
    def __init__(self):
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "Check", style = discord.ButtonStyle.green, custom_id = "verify")
    async def check(self, interaction : discord.Interaction, button : discord.ui.Button):
        role_verify = interaction.guild.get_role(698181876615086120)
        role_non_verify = interaction.guild.get_role(836321227047698432)
            
        if role_verify not in interaction.user.roles and role_non_verify in interaction.user.roles:
            await interaction.user.remove_roles(role_non_verify)
            await interaction.user.add_roles(role_verify)
            await interaction.response.send_message(embed = discord.embed(title = "Check d'entrée", description = "Votre entrée a été confirmée, bienvenue sur Izaria !", color = 0x74FF33), ephemeral = True)
            
        else:
            await interaction.response.send_message("Ce check ne vous concerne pas...", ephemeral = True)
            
    @discord.ui.button(label = "Leave", style = discord.ButtonStyle.danger, custom_id = "leave")
    async def leave(self, interaction : discord.Interaction, button : discord.ui.Button):
        role_verify = interaction.guild.get_role(698181876615086120)
        role_non_verify = interaction.guild.get_role(836321227047698432)
        
        if role_verify not in interaction.user.roles and role_non_verify in interaction.user.roles:
            await interaction.user.kick()
            
        else:
            await interaction.response.send_message("Ce check ne vous concerne pas...", ephemeral = True)
            

# - - - - - - - - - - - - - - - -  C O M M A N D E S  - - - - - - - - - - - - - - - - #


@bot.command(name = 'help')
async def help(ctx, arg = None) : # aides : liste des commandes (fonctionnel)
    if arg == None:
        embed = discord.Embed(title = 'Commandes :', color = 0x00ffff)
        embed.add_field(name = "> **ms**", value = "Mesure du ping", inline = False)
        embed.add_field(name = '> **clear** *[nombre de messages]*', value = "Supprime le nombre demandé de messages", inline = False)
        embed.add_field(name = '> **nar** *[texte]*', value = "Renvoie du message par le narrateur", inline = False)
        embed.add_field(name = "> **roll** *[chance de réussite]* *[chance d'échec]*", value = "Calcule un nombre aléatoire donnant la réussite ou l'échec selon les taux donnés", inline = False)
        embed.add_field(name = '> **meteo**', value = "Crée une météo pour chaque nation sur une durée de 7 jours", inline = False)
        embed.add_field(name = '> **succes**', value = "Donne la liste des succès à obtenir", inline = False)
        embed.add_field(name = '> **kick** *[utilisateur] [raison]*', value = "Exclut le joueur du serveur", inline = False)
        embed.add_field(name = '> **ban** *[utilisateur] [raison]*', value = "Banni le joueur du serveur", inline = False)
    
    await ctx.send(embed = embed)
    print("Envoie d'un coup de main")

@bot.command(name = 'ms')
async def ms(ctx) : # mesure du ping (fonctionnel)
    print(round(bot.latency * 1000), "ms")
    await ctx.send(f'{round(bot.latency * 1000)} ms')

@bot.command(name = 'nar') 
async def narration(ctx, * , nar) : # narration (fonctionnel)
    if len(nar) < 100:
        print(f'Envois du message : {nar}')

    else:
        msg = nar[0:100]
        print(f'Envois du message : {msg} ...')

    await ctx.message.delete()    
    await ctx.send(nar)

@bot.command(name = 'clear')
@has_permissions(manage_messages = True)
async def suppression(ctx, Nmessage : int) : # suppression de messages (fonctionnel)
    print('Suppression en cours')
    a = -1

    msg = await ctx.channel.history(limit = Nmessage + 1).flatten()
    for messages in msg:
        a += 1
        await messages.delete()

    if a == 0 or a == 1:
        print(a,'message supprimé')
        msg = await ctx.send(f'{a} message supprimé')
        sleep(1.5)
        await msg.delete()

    elif a == -1:
        print('aucun message supprimé')

    else:
        print(a,'messages supprimés')
        await ctx.send(f'{a} messages supprimés')
        sleep(1.5)
        await msg.delete()

@bot.command(name = 'roll')
async def dés_roll(ctx, arg1 : int = 50, arg2 : int = 50):
    total = arg1 + arg2
    if total == 100:
        nbr = randint(0,100)
        if nbr <= arg1:
            await ctx.send(f'Réussite *({arg1}%)*')
            
        else:
            await ctx.send(f'Échec *({arg1}%)*')
            
        print(f'{ctx.message.author} tente un roll !')
            
    elif (arg1 < 0 and arg2 > 0) or (arg1 > 0 and arg2 < 0):
        if arg1 < 0 and arg2 > 0:
            arg1 = -arg1
            await dés_roll(ctx, arg1, arg2)
            
        else:
            arg2 = -arg2
            await dés_roll(ctx, arg1, arg2)
            
    elif arg1 < 0 and arg2 < 0:
        arg1 = -arg1
        arg2 = -arg2
        await dés_roll(ctx, arg1, arg2)
        
    elif arg1 == 0 and arg2 == 0:
        await ctx.send('Valeurs incorrectes')
        
    else:
        arg1 = round(arg1 * 100 / total, 0)
        arg2 = round(arg2 * 100 / total, 0)
        total = arg1 + arg2
        if total == 99:
            arg1 += 0.5
            arg2 += 0.5
            
        elif total == 101:
            arg1 += 0.5
            arg2 += 0.5
            
        await dés_roll(ctx, arg1, arg2)

@bot.command(name = 'meteo')
@has_permissions(administrator = True)
async def météo(ctx, arg1, arg2 = None, arg3 = None) : # météo avec températures (fonctionnel)
    if arg1 == "izaria" and arg2 == None and arg3 == None:
        L_temps = create("t",7,1)
        T_temps = create("t",7,2)
        await ctx.send(embed=discord.Embed(title="Toundra",description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C'+'\n'+L_temps[5]+' - '+str(T_temps[5])+'°C'+'\n'+L_temps[6]+' - '+str(T_temps[6])+'°C',color=0x00ffff))
        
        L_temps = create("c",7,1)
        T_temps = create("c",7,2)
        await ctx.send(embed=discord.Embed(title="Asdorath",description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C'+'\n'+L_temps[5]+' - '+str(T_temps[5])+'°C'+'\n'+L_temps[6]+' - '+str(T_temps[6])+'°C',color=0x00ffff))
        
        L_temps = create("d",7,1)
        T_temps = create("d",7,2)
        await ctx.send(embed=discord.Embed(title="Saltir",description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C'+'\n'+L_temps[5]+' - '+str(T_temps[5])+'°C'+'\n'+L_temps[6]+' - '+str(T_temps[6])+'°C',color=0x00ffff))
        
        L_temps = create("d",7,1)
        T_temps = create("d",7,2)
        await ctx.send(embed=discord.Embed(title="Mitsurin",description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C'+'\n'+L_temps[5]+' - '+str(T_temps[5])+'°C'+'\n'+L_temps[6]+' - '+str(T_temps[6])+'°C',color=0x00ffff))
        
        L_temps = create("daku",7,1)
        T_temps = create("daku",7,2)
        await ctx.send(embed=discord.Embed(title="Dākurōdo",description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C'+'\n'+L_temps[5]+' - '+str(T_temps[5])+'°C'+'\n'+L_temps[6]+' - '+str(T_temps[6])+'°C',color=0x00ffff))
        
        L_temps = create("t",7,1)
        T_temps = create("t",7,2)
        await ctx.send(embed=discord.Embed(title="Tengoku",description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C'+'\n'+L_temps[5]+' - '+str(T_temps[5])+'°C'+'\n'+L_temps[6]+' - '+str(T_temps[6])+'°C',color=0x00ffff))
        print("Envoie de la météo d'Izaria")

    elif arg2 != None and arg3 != None:
        liste_climats = ["desert","d","temperate","t","cold","c","dākurōdo","daku"]
        arg2 = str(arg2)
        arg3 = int(arg3)
        if arg3>7:
            arg3=7
        elif arg3<1:
            arg3=1
        else:
            pass

        if arg2 in liste_climats:
            L_temps = create(arg2,arg3,1)
            T_temps = create(arg2,arg3,2)
            print('envoie de',arg3,'jours de météo')

            if arg3 == 1:
                await ctx.send(embed=discord.Embed(title=arg1,description=L_temps[0]+' - '+str(T_temps[0])+'°C',color=0x00ffff))
            
            elif arg3 == 2:
                await ctx.send(embed=discord.Embed(title=arg1,description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C',color=0x00ffff))
            
            elif arg3 == 3:
                await ctx.send(embed=discord.Embed(title=arg1,description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C',color=0x00ffff))
            
            elif arg3 == 4:
                await ctx.send(embed=discord.Embed(title=arg1,description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C',color=0x00ffff))
            
            elif arg3 == 5:
                await ctx.send(embed=discord.Embed(title=arg1,description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C',color=0x00ffff))
            
            elif arg3 == 6:
                await ctx.send(embed=discord.Embed(title=arg1,description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C'+'\n'+L_temps[5]+' - '+str(T_temps[5])+'°C',color=0x00ffff))
            
            elif arg3 == 7:
                await ctx.send(embed=discord.Embed(title=arg1,description=L_temps[0]+' - '+str(T_temps[0])+'°C'+'\n'+L_temps[1]+' - '+str(T_temps[1])+'°C'+'\n'+L_temps[2]+' - '+str(T_temps[2])+'°C'+'\n'+L_temps[3]+' - '+str(T_temps[3])+'°C'+'\n'+L_temps[4]+' - '+str(T_temps[4])+'°C'+'\n'+L_temps[5]+' - '+str(T_temps[5])+'°C'+'\n'+L_temps[6]+' - '+str(T_temps[6])+'°C',color=0x00ffff))
        
        else:
            await ctx.send(f"Ce climat n'est pas dans ma base de donnée")

    else:
        await ctx.send(f'Une erreur est survenue')

@bot.command(name = 'kick')
@has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, * , reason = 'aucune raison spécifiée') : # kick un membre (fonctionnel)
    namekick = f'{member} a été expulsé du serveur'
    reasonkick = f'**Raison :** {reason}'

    await member.send(embed=discord.Embed(title = "Vous avez été expulsé d'Izaria", description = reasonkick, color = 0x00ffff))
    await ctx.guild.kick(member, reason = reason)
    await ctx.send(embed=discord.Embed(title = namekick, description = reasonkick, color = 0x00ffff))

@bot.command(name = 'ban')
@has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, * , reason = 'aucune raison spécifiée') : # ban un membre (fonctionnel)
    namekick = f'{member} a été banni du serveur'
    reasonkick = f'**Raison :** {reason}'

    await member.send(embed=discord.Embed(title = "Vous avez été banni d'Izaria", description = reasonkick, color = 0x00ffff))
    await ctx.guild.ban(member, reason = reason)
    await ctx.send(embed=discord.Embed(title = namekick, description = reasonkick, color = 0x00ffff))

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

@bot.command(name = 'add_user')
@has_permissions(administrator = True)
async def new_succes(ctx, member : discord.Member):
    str_name = str(member.name)
    name = ''
    for ltr in str_name:
        if ltr != ' ' and ltr != '-' and ltr != '.':
            name += ltr
            
        else:
            name += '_'
            
    succes = open("bot UNKAI\succes_logs.py","a")
    try:
        succes.writelines("\n" + f"{name} = Succes({member.id})\nnames.append('{name}')\nids.append({name})")
        await ctx.send(f'Utilisateur ajouté')
        
    except:
        await ctx.send(f"Une erreur est survenue")
        
    succes.close()
    
@bot.command(name = 'add_succes')
@has_permissions(administrator = True)
async def add_succes(ctx, member : discord.Member, succes_name : str):
    str_name = str(member.name)
    name = ''
    for ltr in str_name:
        if ltr != ' ' and ltr != '-' and ltr != '.':
            name += ltr
            
        else:
            name += '_'
            
    succes = open("bot UNKAI\succes_logs.py","a")
    try:
        if name in succes_logs.names:
            succes.writelines("\n" + f'{name}.add_succes("{succes_name}")')
            await ctx.send(f'Succès ajouté')
            
        else:
            await ctx.send(f'Utilisateur introuvable : essayez **U!add_user**')
        
    except:
        await ctx.send(f"Une erreur est survenue")
        
    succes.close()
    
@bot.command(name = 'show_succes')
async def show_succes(ctx, member : discord.Member = None):
    if member == None:
        str_name = str(ctx.message.author.name)
        
    else:
        str_name = str(member.name)
        
    name = ''
    for ltr in str_name:
        if ltr != ' ' and ltr != '-' and ltr != '.':
            name += ltr
            
        else:
            name += '_'
            
    try:
        if name in succes_logs.names:
            i = succes_logs.names.index(name)
            if succes_logs.ids[i].show_succes() != 'Aucun succès débloqué':
                s_list = succes_logs.ids[i].show_succes()
                
            else:
                s_list = 'Aucun succès débloqué'
    
        else:
            s_list = 'Utilisateur inconnu'
        
        if s_list == 'Utilisateur inconnu' or s_list == 'Aucun succès débloqué':
            embed = discord.Embed(title = "Succès débloqués", description = s_list, color = 0x00ffff)
            await ctx.send(embed = embed)
        
        else:
            str_s = ''
            for id in range(len(s_list)):
                str_s += f'\n{id + 1} - {s_list[id]}'
                
            embed = discord.Embed(title = "Succès débloqués", description = str_s, color = 0x00ffff)
            await ctx.send(embed = embed)
        
    except:
        await ctx.send(f'Une erreur est survenue')
        
@bot.command(name = 'succes')
async def show_succes(ctx):
    s_dict = [
                {
                    'Premier personnage' : 'débloqué après avoir fait valider sa première fiche', 
                    'Premiers pas' : 'débloqué après avoir rp pour la première fois', 
                    'Voyageur' : "débloqué après avoir rp dans toute les nations de l'alliance", 
                    'Vagabond' : 'débloqué après avoir rp dans toute les nations', 
                    'Proprietaire' : 'débloqué avoir avoir obtenue une maison en rp',
                    'Chasseur de monstres' : 'débloqué après avoir vaincu 1/10/25 monstres',
                    'Chasseur de boss' : 'débloqué après avoir vaincu 1/3/8 boss', 
                    'Hors la loi' : 'débloqué après avoir commis un acte valant la peine capitale', 
                    'Fantôme' : 'débloqué après être mort en rp',
                    'Acteur du destin' : 'débloqué après avoir fait une action majeure en rp',
                    'Compagnon' : 'débloqué après avoir rp avec au moins trois personnes à la fois',
                    'Âme damné' : 'débloqué après avoir commis un important massacre',
                    'Régicide' : 'débloqué après avoir tué un roi',
                    'Chasseur née' : 'débloqué après avoir chassé un animal de chaques espèces',
                    'Créateur de désastres' : 'débloqué après avoir causé une catastrophe majeure',
                    'Expérimentateur' : 'débloqué après avoir joué un personnage de chaque races proposées',
                    'Indécis' : 'débloqué après avoir joué un personnage de chacune des classes proposées',
                    'Maître de guilde' : "débloqué après avoir créé une guilde reconnue par l'équipe"
                },
                {
                    'Maître des succès' : 'débloqué après avoir obtenu tous les succès basiques',
                    'Assassin' : 'débloqué après avoir tué un autre personnage',
                    'Tueur de démons' : 'débloqué après avoir éliminé un démon dans la nation de Dākurōdo',
                    'Touche à tout' : 'débloqué après avoir obtenue les succès “expérimentateur” et “indécis”',
                    "Lanceur d'hostilités" : 'débloqué après avoir causé une guerre entre deux nations',
                }
            ]
    
    s_list = []
    s_list2 = []
    str_s1 = ''
    for key in s_dict[0].keys():
        s_list.append(key)
        s_list2.append(s_dict[0][key])
    for id in range(len(s_list)):
        str_s1 += f'\n> **{s_list[id]} -** {s_list2[id]}\n'
    
    s_list = []
    str_s2 = ''
    for key in s_dict[1].keys():
        s_list.append(key)
    for id in range(len(s_list)):
        str_s2 += f'\n> **{s_list[id]} -** *non découvert*\n'
    
    await ctx.send(f'__***Succès basiques :***__\n{str_s1}\n\n__***Succès secrets :***__\n{str_s2}')


# - - - - - - - - - - - - - - - -  E V E N T S  - - - - - - - - - - - - - - - - #


@bot.event
async def on_ready() :
    await bot.change_presence(activity = discord.Streaming(url = 'https://www.discord.gg/ucXkrv5yHs', name = 'discord rp', game = 'Discord'))
    
    genrp = bot.get_channel(1107728975012311050)
    await genrp.send(f'*Unkai is now online !*')
    
    print('Le bot est prêt !')
    print(round(bot.latency * 1000), "ms")

@bot.event     
async def on_member_join(member) : # bienvenue (fonctionnel) / check (fonctionnel - désactivé)
    '''if member.guild.id == 693568556217925652:
        role = discord.utils.get(member.guild.roles, name = "| Non vérifié")
        await member.add_roles(role)
        loc = bot.get_channel(836321228091293786)
        await loc.send(embed = discord.Embed(title = "Check d'entrée", description = "Pour valider votre entrée sur le serveur, veuillez intéragir avec le bouton **Check**. Celui-ci vous donnera le rôle <@&698181876615086120> et par la même occasion l'accès au serveur.", color = 0xFF3333), view = check_view())'''
        
    print(f'{member} a rejoint Izaria !')
    general = bot.get_channel(694474742614458488)
    await general.send(f"Hey {member.mention}, bienvenue sur Izaria !")

@bot.event
async def on_member_remove(member) : # adieu (fonctionnel)
    print(f'{member} a quitté Izaria...')


# - - - - - - - - - - - - - - - -  E N   T E S T  - - - - - - - - - - - - - - - - #


@bot.command(name = "rdm_events")
@has_permissions(administrator = True)
async def random_events(ctx, * , arg : str = "random"):
    arguments = ["random", "patrol", "invasion"]
    base = ctx.channel.id

    # 0 = cité tengoku | 1 village tengoku | 2 à 6 = cités | 7 à fin = villages
    cities_id = [942821599831269467, 942820623015612566, 942092566185275402, 927531924145176606, 927535331337715754, 927535891239563274, 927538568975507476, 942349198068690994, 927532531849515049, 927532947282743306, 927533419880132629, 927533883040333866, 927535230456299550, 927536331310116964, 927539441025843210]
    temp = []

    if arg.lower() == "patrol":
        nbr_event = randint(2, 4)
        a = 0
        for i in range(nbr_event):
            word = randint(1, 3)
            loc_event = randint(0, len(cities_id))

            if word == 1 or word == 3:
                mot = 'soldats'

            elif word == 2:
                mot = 'guerriers'

            if cities_id[loc_event] not in temp:
                temp.append(int(cities_id[loc_event]))
                place = bot.get_channel(cities_id[loc_event])

                if loc_event == 0:
                    await place.send(f'**Une patrouille de sentinelles traverse la cité**')

                elif loc_event == 1:
                    await place.send(f'**Une patrouille de sentinelles traverse le village**')

                elif loc_event > 1 and loc_event < 7:
                    await place.send(f'**Une patrouilles de {mot} traverse la cité**')

                elif loc_event > 7:
                    await place.send(f'**Une patrouille de {mot} traverse le village**')

                a += 1
        
        place = bot.get_channel(base)
        if a > 1:
            await place.send(f'{a} patrouilles envoyés dans le rp avec succès !')
            print(f'{a} patrouilles envoyés sur Izaria')
        
        elif a == 1:
            await place.send(f'Une patrouille envoyés dans le rp avec succès !')
            print(f'Une patrouille envoyés sur Izaria')

        else:
            await place.send(f"Les patrouilles n'ont pas pu partir")

    elif arg.lower() == "invasion":
        word = randint(1, 3)
        if word == 1 or word == 3:
            mot = 'Un groupe'

        elif word == 2:
            mot = 'Une horde'

        loc_event = randint(2, len(cities_id))
        place = bot.get_channel(cities_id[loc_event])

        if loc_event <= 6:
            await place.send(f'**{mot} de pillards attaque la cité !**')

        elif loc_event > 6:
            await place.send(f'**{mot} de pillards attaque le village !**')

        base.send(f'Une inavasion a été lancé avec succès !')
        print('Une invasion a été lancé sur Izaria')
    
    else:
        a = randint(1, len(arguments))
        arg = arguments[a]
        
@bot.command(name = 'katsu_roll')
async def katsu_roll(ctx, msg):
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
        

# - - - - - - - - - - - - - - - -  T O K E N  - - - - - - - - - - - - - - - - #


# Sécurisation du Token 
from unkai_tk import TOKENS
bot.run(TOKENS)


# - - - - - - - - - - - - - - - -  I N F O R M A T I O N S  - - - - - - - - - - - - - - - - #

# > Actual version - 1
# > Uid - 2
# > Creation - 2022/10
# > Total scripts - 4