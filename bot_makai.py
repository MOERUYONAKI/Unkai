# ~ - - - - - - - - - - - - - - - - ~  U N K A I  -  M A K A I  ~ - - - - - - - - - - - - - - - - ~ #


# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


import discord 
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import *

# from Succes.succes import *
# import Succes.succes_logs as succes_logs

import Makai.Test as test
import Makai.Rolls as rolls
import Makai.Offrandes as offrandes
import Makai.Infos as infos
import Makai.Characters as characters


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# - - - - - - - - - - - - - - - -  C L A S S E S  - - - - - - - - - - - - - - - - #


class button_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None
        
    @discord.ui.button(label = "Oui", style = discord.ButtonStyle.green, custom_id = "yes")
    async def oui(self, interaction : discord.Interaction, button : discord.ui.Button):
        m = await interaction.response.send_message(content = f"*Démarage du test...*", delete_after = 0.3)
        self.value = 1
        self.stop()
            
    @discord.ui.button(label = "Non", style = discord.ButtonStyle.danger, custom_id = "no")
    async def non(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.message.delete()
        self.value = 2
        self.stop()

class join_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "Check", style = discord.ButtonStyle.green, custom_id = "verify")
    async def check(self, interaction : discord.Interaction, button : discord.ui.Button):
        role_verify = interaction.guild.get_role(1141363425650417676)
        role_hrp = interaction.guild.get_role(1141363072871714847)
            
        if len(interaction.user.roles) == 1:
            await interaction.user.add_roles(role_verify)
            await interaction.user.add_roles(role_hrp)
            await interaction.response.send_message(embed = discord.Embed(title = "Check d'entrée", description = "Votre entrée a été confirmée, bienvenue sur le serveur ! 👋", color = 0x74FF33), ephemeral = True)
            
        else:
            await interaction.response.send_message("> Ce check ne vous concerne pas...", ephemeral = True)
            
    @discord.ui.button(label = "Leave", style = discord.ButtonStyle.danger, custom_id = "leave")
    async def leave(self, interaction : discord.Interaction, button : discord.ui.Button):
        role_verify = interaction.guild.get_role(1141363425650417676)
        
        if len(interaction.user.roles) == 1:
            await interaction.response.send_message("> Expulsion en cours...", ephemeral = True)
            await interaction.user.kick(reason = "Check d'entrée invalide")
            
        else:
            await interaction.response.send_message("> Ce check ne vous concerne pas...", ephemeral = True)
 

# - - - - - - - - - - - - - - - -  C O M M A N D E S  -  B A S E  - - - - - - - - - - - - - - - - #


@bot.tree.command(name = 'help') # aide - liste des commandes (fonctionnel)
async def help(interaction : discord.Interaction): 
    embed = discord.Embed(title = 'Liste des commandes :', color = 0x00ffff)
    embed.add_field(name = "> **ms**", value = "Mesure du ping", inline = False)
    embed.add_field(name = '> **nar** *[texte]*', value = "Renvoie du message par le narrateur", inline = False)
    embed.add_field(name = "> **roll** *[maximum]* *[nombre de lancers]*", value = "Calcule un nombre aléatoire entre 1 et le maximum le nombre de fois demandé", inline = False)
    embed.add_field(name = "> **info** *[sujet]*", value = "Donne la définition associé au sujet", inline = False)
    embed.add_field(name = "> **succes**", value = "Renvoie la liste complète des succès de Makai", inline = False)
    
    await interaction.response.send_message(embed = embed)
    
    print("Envoie d'un coup de main")

@bot.tree.command(name = 'ms') # mesure du ping (fonctionnel)
async def ms(interaction : discord.Interaction) :
    print(round(bot.latency * 1000), "ms")
    await interaction.response.send_message(f'> *{round(bot.latency * 1000)} ms*')
 
@bot.tree.command(name = 'link') # lien d'accès (fonctionnel)
@app_commands.choices(site = [app_commands.Choice(name = "Github", value = "Github")])
async def link(interaction : discord.Interaction, site : app_commands.Choice[str]):
    if site.value == 'Github':
        await interaction.response.send_message(f'https://github.com/MOERUYONAKI', ephemeral = True)

@bot.command(name = 'nar') # narration (fonctionnel)
async def narration(ctx, * , nar) : 
    if len(nar) < 100:
        print(f'Envois du message : {nar}')

    else:
        msg = nar[0:100]
        print(f'Envois du message : {msg} ...')

    await ctx.message.delete()    
    await ctx.send(nar)


# - - - - - - - - - - - - - - - -  C O M M A N D E S  -  M A K A I  - - - - - - - - - - - - - - - - #


@bot.tree.command(name = 'test_éveil') # roll test (fonctionnel)
@has_permissions(administrator = True)
async def test_eveil(interaction : discord.Interaction, user : discord.User):
    await test.test_eveil(interaction, user, button_view)

@bot.tree.command(name = 'roll') # rolls d100 ou 50/50 (fonctionnel)
@app_commands.choices(nombre = [app_commands.Choice(name = "1", value = 1),
                                app_commands.Choice(name = "2", value = 2),
                                app_commands.Choice(name = "3", value = 3)],
                        types = [app_commands.Choice(name = "50/50", value = "fifty"),
                                app_commands.Choice(name = "d100", value = "base")])
async def makai_roll(interaction : discord.Interaction, nombre : app_commands.Choice[int], types : app_commands.Choice[str], bonus : int = 0):
    await rolls.makai_roll(interaction, nombre, types, bonus)

@bot.tree.command(name = 'offrande') # message offrande (fonctionnel)
@app_commands.choices(type = [app_commands.Choice(name = "mineure", value = 0),
                              app_commands.Choice(name = "simple", value = 1), 
                              app_commands.Choice(name = "double", value = 2)])
async def offrande(interaction : discord.Interaction, type : app_commands.Choice[int], lien : str):
    await offrandes.offrande(interaction, type, lien)

@bot.tree.command(name = 'info') # définitions (fonctionnel)
@app_commands.choices(sujet = [app_commands.Choice(name = "Jugement de plausibilité", value = 1),
                                app_commands.Choice(name = "Sélection du destin", value = 2)])
async def info(interaction : discord.Interaction, sujet : app_commands.Choice[int]):
    await infos.makai_def(interaction, sujet)
    

# - - - - - - - - - - - - - - - -  C O M M A N D E S  -  S U C C E S  - - - - - - - - - - - - - - - - #
    

@bot.tree.command(name = 'profile')
async def get_user(interaction : discord.Interaction, member : discord.User = None):
    await characters.get_user(interaction, member) if member != None else await characters.get_user(interaction)
    
@bot.tree.command(name = 'create_user')
@has_permissions(administrator = True)
@app_commands.choices(faction = [app_commands.Choice(name = "Humain", value = "humain"),
                              app_commands.Choice(name = "Ghoul", value = "Ghoul")],
                      élément = [app_commands.Choice(name = "Feu", value = "feu"),
                              app_commands.Choice(name = "Vent", value = "vent"), 
                              app_commands.Choice(name = "Eau", value = "eau"), 
                              app_commands.Choice(name = "Terre", value = "terre")])
async def create_user(interaction : discord.Interaction, member : discord.User, nom : str, faction : discord.app_commands.Choice[str], élément : discord.app_commands.Choice[str], force : int = 0, défense : int = 0, agilité : int = 0, perception : int = 0, magie : int = 0):
    await characters.create_user(interaction, member, nom, faction, élément, force, défense, agilité, perception, magie)

@bot.tree.command(name = 'upgrade_stats')
@app_commands.choices(force = [app_commands.Choice(name = "0", value = 0),
                               app_commands.Choice(name = "1", value = 1),
                               app_commands.Choice(name = "2", value = 2),
                               app_commands.Choice(name = "3", value = 3)],
                      défense = [app_commands.Choice(name = "0", value = 0),
                                 app_commands.Choice(name = "1", value = 1),
                                 app_commands.Choice(name = "2", value = 2),
                                 app_commands.Choice(name = "3", value = 3)],
                      agilité = [app_commands.Choice(name = "0", value = 0),
                                 app_commands.Choice(name = "1", value = 1),
                                 app_commands.Choice(name = "2", value = 2),
                                 app_commands.Choice(name = "3", value = 3)],
                      perception = [app_commands.Choice(name = "0", value = 0),
                                    app_commands.Choice(name = "1", value = 1),
                                    app_commands.Choice(name = "2", value = 2),
                                    app_commands.Choice(name = "3", value = 3)],
                      magie = [app_commands.Choice(name = "0", value = 0),
                               app_commands.Choice(name = "1", value = 1),
                               app_commands.Choice(name = "2", value = 2),
                               app_commands.Choice(name = "3", value = 3)])
async def add_stats(interaction : discord.Interaction, force : discord.app_commands.Choice[int], défense : discord.app_commands.Choice[int], agilité : discord.app_commands.Choice[int], perception : discord.app_commands.Choice[int], magie : discord.app_commands.Choice[int]):
    await characters.add_stats(interaction, interaction.user, force, défense, agilité, perception, magie)

@bot.tree.command(name = 'add_points')
@has_permissions(administrator = True)
async def add_points(interaction : discord.Interaction, member : discord.User, plausibilité : int = 0, éveil : int = 0, évolution : int = 0, argent : int = 0):
    await characters.add_points(interaction, member, plausibilité, éveil, évolution, argent)

@bot.tree.command(name = 'add_élément')
@app_commands.choices(element = [app_commands.Choice(name = "Feu", value = "feu"),
                               app_commands.Choice(name = "Eau", value = "eau"),
                               app_commands.Choice(name = "Terre", value = "terre"),
                               app_commands.Choice(name = "Foudre", value = "foudre"),
                               app_commands.Choice(name = "Vent", value = "vent")])
async def add_élément(interaction : discord.Interaction, element : discord.app_commands.Choice[str]):
    await characters.add_élément(interaction, element)

@bot.tree.command(name = 'fusion')
@app_commands.choices(first_element = [app_commands.Choice(name = "Feu", value = "feu"),
                               app_commands.Choice(name = "Eau", value = "eau"),
                               app_commands.Choice(name = "Terre", value = "terre"),
                               app_commands.Choice(name = "Foudre", value = "foudre"),
                               app_commands.Choice(name = "Vent", value = "vent"),
                               app_commands.Choice(name = "Brume", value = "brume"),
                               app_commands.Choice(name = "Glace", value = "glace"),
                               app_commands.Choice(name = "Cendre", value = "cendre"),
                               app_commands.Choice(name = "Roche", value = "roche"),
                               app_commands.Choice(name = "Plasma", value = "plasma")],
                        second_element = [app_commands.Choice(name = "Feu", value = "feu"),
                               app_commands.Choice(name = "Eau", value = "eau"),
                               app_commands.Choice(name = "Terre", value = "terre"),
                               app_commands.Choice(name = "Foudre", value = "foudre"),
                               app_commands.Choice(name = "Vent", value = "vent"),
                               app_commands.Choice(name = "Brume", value = "brume"),
                               app_commands.Choice(name = "Glace", value = "glace"),
                               app_commands.Choice(name = "Cendre", value = "cendre"),
                               app_commands.Choice(name = "Roche", value = "roche"),
                               app_commands.Choice(name = "Plasma", value = "plasma")])
async def fusion(interaction : discord.Interaction, first_element : discord.app_commands.Choice[str], second_element : discord.app_commands.Choice[str]):
    await characters.fusion(interaction, first_element, second_element)


# - - - - - - - - - - - - - - - -  C O M M A N D E S  -  S U C C E S  - - - - - - - - - - - - - - - - #


# @bot.command(name = 'add_user')
# @has_permissions(administrator = True)
# async def new_succes(ctx, member : discord.Member):
#     str_name = str(member.name)
#     name = ''
#     for ltr in str_name:
#         if ltr != ' ' and ltr != '-' and ltr != '.':
#             name += ltr
            
#         else:
#             name += '_'
            
#     succes = open("bot UNKAI\Succes\succes_logs.py","a")
#     if name not in succes_logs.names:
#         try:
#             succes.writelines("\n" + f"id{member.id} = Succes({member.id}) # Name - {name}\nnames.append('id{member.id}')\nids.append(id{member.id})")
#             await ctx.send(f'Utilisateur ajouté')
            
#         except:
#             await ctx.send(f"Une erreur est survenue")

#     else:
#         await ctx.send(f"Cet utilisateur est déjà enregistré")
        
#     succes.close()

# @bot.command(name = 'add_succes')
# @has_permissions(administrator = True)
# async def add_succes(ctx, member : discord.Member, succes_name : str):
#     str_name = str(member.name)
#     name = ''
#     for ltr in str_name:
#         if ltr != ' ' and ltr != '-' and ltr != '.':
#             name += ltr
            
#         else:
#             name += '_'
            
#     succes = open("bot UNKAI\succes_logs.py","a")
#     try:
#         if name in succes_logs.names:
#             succes.writelines("\n" + f'id{member.id}.add_succes("{succes_name}")')
#             await ctx.send(f'Succès ajouté')
            
#         else:
#             await ctx.send(f'Utilisateur introuvable : essayez **U!add_user**')
        
#     except:
#         await ctx.send(f"Une erreur est survenue")
        
#     succes.close()

# @bot.command(name = 'show_succes')
# async def show_succes(ctx, member : discord.Member = None):
#     if member == None:
#         str_name = str(ctx.message.author.name)
        
#     else:
#         str_name = str(member.name)
        
#     name = ''
#     for ltr in str_name:
#         if ltr != ' ' and ltr != '-' and ltr != '.':
#             name += ltr
            
#         else:
#             name += '_'
            
#     try:
#         if name in succes_logs.names:
#             i = succes_logs.names.index(name)
#             if succes_logs.ids[i].show_succes() != 'Aucun succès débloqué':
#                 s_list = succes_logs.ids[i].show_succes()
                
#             else:
#                 s_list = 'Aucun succès débloqué'
    
#         else:
#             s_list = 'Utilisateur inconnu'
        
#         if s_list == 'Utilisateur inconnu' or s_list == 'Aucun succès débloqué':
#             embed = discord.Embed(title = "Succès débloqués", description = s_list, color = 0x00ffff)
#             await ctx.send(embed = embed)
        
#         else:
#             str_s = ''
#             for id in range(len(s_list)):
#                 str_s += f'\n{id + 1} - {s_list[id]}'
                
#             embed = discord.Embed(title = "Succès débloqués", description = str_s, color = 0x00ffff)
#             await ctx.send(embed = embed)
        
#     except:
#         await ctx.send(f'Une erreur est survenue')
        
# @bot.command(name = 'succes')
# async def show_succes(ctx):
#     s_dict = [
#                 {
#                     'Premier personnage' : 'débloqué après avoir fait valider sa première fiche', 
#                     'Premiers pas' : 'débloqué après avoir rp pour la première fois', 
#                     'Voyageur' : "débloqué après avoir rp dans toute les nations de l'alliance", 
#                     'Vagabond' : 'débloqué après avoir rp dans toute les nations', 
#                     'Proprietaire' : 'débloqué avoir avoir obtenue une maison en rp',
#                     'Chasseur de monstres' : 'débloqué après avoir vaincu 1/10/25 monstres',
#                     'Chasseur de boss' : 'débloqué après avoir vaincu 1/3/8 boss', 
#                     'Hors la loi' : 'débloqué après avoir commis un acte valant la peine capitale', 
#                     'Fantôme' : 'débloqué après être mort en rp',
#                     'Acteur du destin' : 'débloqué après avoir fait une action majeure en rp',
#                     'Compagnon' : 'débloqué après avoir rp avec au moins trois personnes à la fois',
#                     'Âme damné' : 'débloqué après avoir commis un important massacre',
#                     'Régicide' : 'débloqué après avoir tué un roi',
#                     'Chasseur née' : 'débloqué après avoir chassé un animal de chaques espèces',
#                     'Créateur de désastres' : 'débloqué après avoir causé une catastrophe majeure',
#                     'Expérimentateur' : 'débloqué après avoir joué un personnage de chaque races proposées',
#                     'Indécis' : 'débloqué après avoir joué un personnage de chacune des classes proposées',
#                     'Maître de guilde' : "débloqué après avoir créé une guilde reconnue par l'équipe"
#                 },
#                 {
#                     'Maître des succès' : 'débloqué après avoir obtenu tous les succès basiques',
#                     'Assassin' : 'débloqué après avoir tué un autre personnage',
#                     'Tueur de démons' : 'débloqué après avoir éliminé un démon dans la nation de Dākurōdo',
#                     'Touche à tout' : 'débloqué après avoir obtenue les succès “expérimentateur” et “indécis”',
#                     "Lanceur d'hostilités" : 'débloqué après avoir causé une guerre entre deux nations',
#                 }
#             ]
    
#     s_list = []
#     s_list2 = []
#     str_s1 = ''

#     for key in s_dict[0].keys():
#         s_list.append(key)
#         s_list2.append(s_dict[0][key])

#     for id in range(len(s_list)):
#         str_s1 += f'\n> **{s_list[id]} -** {s_list2[id]}\n'
    
#     s_list = []
#     str_s2 = ''

#     for key in s_dict[1].keys():
#         s_list.append(key)

#     for id in range(len(s_list)):
#         str_s2 += f'\n> **{s_list[id]} -** *non découvert*\n'
    
#     await ctx.send(f'__***Succès basiques :***__\n{str_s1}\n\n__***Succès secrets :***__\n{str_s2}')


# - - - - - - - - - - - - - - - -  E V E N T S  - - - - - - - - - - - - - - - - #


@bot.event
async def on_ready() :
    await bot.tree.sync()
    activity = discord.Game(name = "/help")
    await bot.change_presence(status = discord.Status.idle, activity = activity)
    
    print('Le bot est prêt !')
    print(round(bot.latency * 1000), "ms")

@bot.event
async def on_message(message) : # réaction aux messages (fonctionnel)
    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after) : # réaction aux messages (fonctionnel)
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

@bot.event     
async def on_member_join(member : discord.Member) : # bienvenue (fonctionnel)
    print(f'{member} a rejoint un de nos serveurs ({member.guild})')
    if member.guild.id == 1101138795446935643: # Makai
        loc = bot.get_channel(1101138795446935646)
        await loc.send(f"### **Bienvenue sur M̸͐̉A̵̿̅K̴̅̊A̶̍́Ï̸̅ ̸̓̾**\n> ||{member.mention}||")

        loc = bot.get_channel(1141356443161854072)
        await loc.send(f"> {member.mention} - Suppression dans 60 secondes", delete_after = 60, embed = discord.Embed(title = "Check d'entrée", description = "Pour valider votre entrée sur le serveur, veuillez intéragir avec le bouton **Check**. Celui-ci vous donnera le rôle <@&1141363425650417676> et par la même occasion l'accès au serveur.", color = 0xFF3333), view = join_view())

@bot.event
async def on_member_remove(member) : # adieu (fonctionnel)
    print(f'{member} a quitté un de nos serveurs ({member.guild})')


# - - - - - - - - - - - - - - - -  T O K E N  - - - - - - - - - - - - - - - - #


# Sécurisation du Token 
from XXX import TOKEN
bot.run(TOKEN)


# - - - - - - - - - - - - - - - -  I N F O R M A T I O N S  - - - - - - - - - - - - - - - - #

# > Actual version - 2
# > Uid - 3
# > Creation - 2023/08
# > Total scripts - 7 