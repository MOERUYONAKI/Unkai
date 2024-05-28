# ~ - - - - - - - - - - - - - - - - ~  U N K A I  -  M A K A I  ~ - - - - - - - - - - - - - - - - ~ #


# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


import Autres.rolls as r
from discord import *
import discord 
from random import randint
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import *
from Succes.succes import *
import Succes.succes_logs as succes_logs


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


@bot.command(name = 'test_éveil') # roll test (fonctionnel)
async def test_eveil(ctx):
    msg = Embed(title = "Résultats - éveil", color = 0x00ffff)
    msg.add_field(name = "Agilité", value = "*calcul en cours*", inline = False)
    msg.add_field(name = "Puissance", value = "*calcul en cours*", inline = False)
    msg.add_field(name = "Résistance", value = "*calcul en cours*", inline = False)
    msg.add_field(name = "Magie", value = "*calcul en cours*", inline = False)
    message = await ctx.send(f"### __**Test d'éveil**__" + "\n" +
                             f"Le test se dérouleras en quatre parties, donnant un score à chacune." + "\n" + "À la fin de ces évalutations, votre score total révélera votre rang initial.", embed = msg)

    sleep(3)
    roll = r.eveil_roll("base")

    msg2 = Embed(title = "Résultats - éveil", color = 0x00ffff)
    msg2.add_field(name = "Agilité", value = f"> **{roll[0]}** *({roll[1][0]} / {roll[1][1]})*", inline = False)
    msg2.add_field(name = "Puissance", value = "*calcul en cours*", inline = False)
    msg2.add_field(name = "Résistance", value = "*calcul en cours*", inline = False)
    msg2.add_field(name = "Magie", value = "*calcul en cours*", inline = False)

    if roll[0] < 4000:
        a = "faible"

    elif roll[0] > 8000:
        a = "élevé"

    else:
        a = "moyen"

    await message.edit(content = "### __**Test d'éveil**__" + "\n" +
                             f"Le test se dérouleras en quatre parties, donnant un score à chacune." + "\n" + "À la fin de ces évalutations, votre score total révélera votre rang initial." + "\n" + "\n" +
                             f"> **Agilité :** {a}", embed = msg2)

    sleep(3)
    roll2 = r.eveil_roll("base")

    msg3 = Embed(title = "Résultats - éveil", color = 0x00ffff)
    msg3.add_field(name = "Agilité", value = f"> **{roll[0]}** *({roll[1][0]} / {roll[1][1]})*", inline = False)
    msg3.add_field(name = "Puissance", value = f"> **{roll2[0]}** *({roll2[1][0]} / {roll2[1][1]})*", inline = False)
    msg3.add_field(name = "Résistance", value = "*calcul en cours*", inline = False)
    msg3.add_field(name = "Magie", value = "*calcul en cours*", inline = False)

    if roll2[0] < 4000:
        b = "faible"

    elif roll2[0] > 8000:
        b = "élevé"

    else:
        b = "moyen"

    await message.edit(content = "### __**Test d'éveil**__" + "\n" +
                             f"Le test se dérouleras en quatre parties, donnant un score à chacune." + "\n" + "À la fin de ces évalutations, votre score total révélera votre rang initial." + "\n" + "\n" +
                             f"> **Agilité :** {a}" + "\n" +
                             f"> **Puissance :** {b}", embed = msg3)
    
    sleep(3)
    roll3 = r.eveil_roll("base")

    msg4 = Embed(title = "Résultats - éveil", color = 0x00ffff)
    msg4.add_field(name = "Agilité", value = f"> **{roll[0]}** *({roll[1][0]} / {roll[1][1]})*", inline = False)
    msg4.add_field(name = "Puissance", value = f"> **{roll2[0]}** *({roll2[1][0]} / {roll2[1][1]})*", inline = False)
    msg4.add_field(name = "Résistance", value = f"> **{roll3[0]}** *({roll3[1][0]} / {roll3[1][1]})*", inline = False)
    msg4.add_field(name = "Magie", value = "*calcul en cours*", inline = False)

    if roll3[0] < 4000:
        c = "faible"

    elif roll3[0] > 8000:
        c = "élevé"

    else:
        c = "moyen"

    await message.edit(content = "### __**Test d'éveil**__" + "\n" +
                             f"Le test se dérouleras en quatre parties, donnant un score à chacune." + "\n" + "À la fin de ces évalutations, votre score total révélera votre rang initial." + "\n" + "\n" +
                             f"> **Agilité :** {a}" + "\n" + 
                             f"> **Puissance :** {b}" + "\n" + 
                             f"> **Résistance:** {c}", embed = msg4)
    
    sleep(3)
    roll4 = r.eveil_roll("base")

    msg5 = Embed(title = "Résultats - éveil", color = 0x00ffff)
    msg5.add_field(name = "Agilité", value = f"> **{roll[0]}** *({roll[1][0]} / {roll[1][1]})*", inline = False)
    msg5.add_field(name = "Puissance", value = f"> **{roll2[0]}** *({roll2[1][0]} / {roll2[1][1]})*", inline = False)
    msg5.add_field(name = "Résistance", value = f"> **{roll3[0]}** *({roll3[1][0]} / {roll3[1][1]})*", inline = False)
    msg5.add_field(name = "Magie", value = f"> **{roll4[0]}** *({roll4[1][0]} / {roll4[1][1]})*", inline = False)

    if roll4[0] < 4000:
        d = "faible"

    elif roll4[0] > 8000:
        d = "élevé"

    else:
        d = "moyen"

    await message.edit(content = "### __**Test d'éveil**__" + "\n" +
                             f"Le test se dérouleras en quatre parties, donnant un score à chacune." + "\n" + "À la fin de ces évalutations, votre score total révélera votre rang initial." + "\n" + "\n" +
                             f"> **Agilité :** {a}" + "\n" +
                             f"> **Puissance :** {b}" + "\n" + 
                             f"> **Résistance :** {c}" + "\n" + 
                             f"> **Magie :** {d}", embed = msg5)
    
    rolls = [roll[0], roll2[0], roll3[0], roll4[0]]
    for i in range(len(rolls)):
        if rolls[i] > 9750:
            if i == 0:
                view = button_view()
                m1 = await ctx.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Agilité" + "\n" + "\n" +
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                sleep(1)
                await view.wait()

                if view.value == 1:
                    await m1.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Agilité" + "\n" + "\n" +
                            f"> Résultat : *calcul en cours*"))
                        
                    sleep(3)
                    rl = r.eveil_roll("sup")
                    if rl < 500:
                        a = "moyen"

                    elif rl > 4200:
                        a = "supérieur"

                    else:
                        a = "élevé"

                    await m1.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Agilité" + "\n" + "\n" +
                            f"> **Résultat :** {a} *({rl})*"))

        if rolls[i] > 9750:
            if i == 1:
                view = button_view()
                m2 = await ctx.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Puissance" + "\n" + "\n" +
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                sleep(1)
                await view.wait()

                if view.value == 1:
                    await m2.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Puissance" + "\n" + "\n" +
                            f"> Résultat : *calcul en cours*"))
                        
                    sleep(3)
                    rl = r.eveil_roll("sup")
                    if rl < 500:
                        b = "moyen"

                    elif rl > 4200:
                        b = "supérieur"

                    else:
                        b = "élevé"

                    await m2.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Puissance" + "\n" + "\n" +
                            f"> **Résultat :** {b} *({rl})*"))

        if rolls[i] > 9750:
            if i == 2:
                view = button_view()
                m3 = await ctx.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Résistance" + "\n" + "\n" +
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                sleep(1)
                await view.wait()

                if view.value == 1:
                    await m3.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Résistance" + "\n" + "\n" +
                            f"> Résultat : *calcul en cours*"))
                        
                    sleep(3)
                    rl = r.eveil_roll("sup")
                    if rl < 500:
                        c = "moyen"

                    elif rl > 4200:
                        c = "supérieur"

                    else:
                        c = "élevé"

                    await m3.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Résistance" + "\n" + "\n" +
                            f"> **Résultat :** {c} *({rl})*"))

        if rolls[i] > 9750:
            if i == 3:
                view = button_view()
                m4 = await ctx.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Magie" + "\n" + "\n" +
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                sleep(1)
                await view.wait()

                if view.value == 1:
                    await m4.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Magie" + "\n" + "\n" +
                            f"> Résultat : *calcul en cours*"))
                        
                    sleep(3)
                    rl = r.eveil_roll("sup")
                    if rl < 500:
                        d = "moyen"

                    elif rl > 4200:
                        d = "supérieur"

                    else:
                        d = "élevé"

                    await m4.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Magie" + "\n" + "\n" +
                            f"> **Résultat :** {d} *({rl})*"))

    await message.edit(content = "### __**Test d'éveil**__" + "\n" +
                             f"Le test se dérouleras en quatre parties, donnant un score à chacune." + "\n" + "À la fin de ces évalutations, votre score total révélera votre rang initial." + "\n" + "\n" +
                             f"> **Agilité :** {a}" + "\n" +
                             f"> **Puissance :** {b}" + "\n" + 
                             f"> **Résistance :** {c}" + "\n" + 
                             f"> **Magie :** {d}", embed = msg5)
    
    lvls = [a, b, c, d]
    temp_rang = 0
    for cat in lvls:
        if cat == "faible":
            temp_rang += 1

        elif cat == "moyen":
            temp_rang += 2

        elif cat == "élevé":
            temp_rang += 3 

        elif cat == "supérieur":
            temp_rang += 4

        elif cat == "maître":
            temp_rang += 6

    if temp_rang <= 5:
        rang = "E"

    elif temp_rang == 6 or temp_rang == 7:
        rang = "D"

    elif temp_rang == 8 or temp_rang == 9:
        rang = "C"

    elif temp_rang == 10 or temp_rang == 11 or temp_rang == 12:
        rang = "B"

    elif temp_rang > 12 and temp_rang <= 16:
        rang = "A"

    elif temp_rang > 16:
        rang = "S"
    
    sleep(1.5)
    print(f'Un test vient de s\'achever : \n> Rang {rang}')
    await ctx.send(f"### __**Test d'éveil**__" + "\n" +
                    f"Le test est désormais terminé :" + "\n" +
                    f"> ||Rang {rang}||")

@bot.tree.command(name = 'roll') # rolls d100 ou 50/50 (fonctionnel)
@app_commands.choices(nombre = [app_commands.Choice(name = "1", value = 1),
                                app_commands.Choice(name = "2", value = 2),
                                app_commands.Choice(name = "3", value = 3)],
                        types = [app_commands.Choice(name = "50/50", value = "fifty"),
                                app_commands.Choice(name = "d100", value = "base")])
async def makai_roll(interaction : discord.Interaction, bonus : int, nombre : app_commands.Choice[int], types : app_commands.Choice[str]):
    if types.value == "fifty":
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

    elif types.value == "base":
        results = []
        for i in range(nombre.value):
            roll = r.basic_roll(100)
            results.append(roll)

        if bonus > 0:
            cmd = f"{nombre.value}d100+{bonus}"

        elif bonus < 0:
            cmd = f"{nombre.value}d100{bonus}"

        else:
            cmd = f"{nombre.value}d100"
        
        r1 = results[0]
        if len(results) == 1:
            await interaction.response.send_message(f'```# {r1 + bonus}\nDétails : {cmd} ({r1})```')

        elif len(results) == 2:
            r2 = results[1]
            await interaction.response.send_message(f'```# {r1 + r2 + bonus}\nDétails : {cmd} ({r1}, {r2})```')

        elif len(results) > 2:
            r2 = results[1]
            r3 = results[2]
            await interaction.response.send_message(f'```# {r1 + r2 + r3 + bonus}\nDétails : {cmd} ({r1}, {r2}, {r3})```')

@bot.tree.command(name = 'offrande') # message offrande (fonctionnel)
@app_commands.choices(type = [app_commands.Choice(name = "simple", value = 1), 
                              app_commands.Choice(name = "double", value = 2)])
async def offrande(interaction : discord.Interaction, type : app_commands.Choice[int], lien : str):
    if type.value == 1:
        await interaction.response.send_message(f'***Une Nébuleuse est impressionnée par une action et offre 500 pièces...***\n> {lien}')

    elif type.value == 2:
        await interaction.response.send_message(f'***Une Nébuleuse est subjuguée par une action et offre 1000 pièces...***\n> {lien}')

@bot.tree.command(name = 'info') # définitions (fonctionnel)
@app_commands.choices(sujet = [app_commands.Choice(name = "Jugement de plausibilité", value = 1),
                                app_commands.Choice(name = "Sélection du destin", value = 2)])
async def makai_roll(interaction : discord.Interaction, sujet : app_commands.Choice[int]):
    if sujet.value == 1: # Jugement de plausibilité
        await interaction.response.send_message(f'__**Jugement de plausibilité**__' + "\n \n" + 
                                                f"Le **jugement de plausibilité** est une réunion des Nébuleuses au sujet d'un choix, d'une action ou d'une conséquence. Le but de ce jugement est de débattre sur la possibilité que ce sujet ait lieu ou si, au contraire, cela semble irréalisable. Lorsque ce jugement est demandé par un joueur, il peut être amené à débattre sur le sujet pour défendre ses idées mais ce n’est pas nécessairement le cas. Le résultat du jugement de plausibilité est incontestable et ne peut en aucun cas être réutilisé pour un autre cas même similaire." + "\n \n" + 
                                                f"Il est possible de demander un **jugement de plausibilité** dans plusieurs cas, comme la préparation d’une action complexe ou au conséquence importante, mais aussi si une action à notre encontre nous semble incohérente. Le jugement apportera dans ces situations un “laissez passer” ou bien un arrêt pouvant aller jusqu’à un “changement de destin”, soit la suppression d’une action et sa modification. Outre cela, les Nébuleuses peuvent aussi décider d’en faire un en secret si une action leur semble non plausible ou contre le règlement.")

    elif sujet.value == 2: # Sélection du destin
        await interaction.response.send_message(f'__**Sélection du destin**__' + "\n \n" + 
                                                f'La **sélection du destin** est un choix imposé au joueur et ayant des conséquences particulièrement importantes sur l’avenir de son personnage. La principale sélection est celle de la mort. Une telle sélection peut venir des Nébuleuses mais aussi du scénario de l’histoire ou bien simplement de vos actions, comme pour la mort. Les options de la sélection sont imposées et ne peuvent être évitées ou arrangées.')
 

# - - - - - - - - - - - - - - - -  C O M M A N D E S  -  S U C C E S  - - - - - - - - - - - - - - - - #


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
            
    succes = open("bot UNKAI\Succes\succes_logs.py","a")
    if name not in succes_logs.names:
        try:
            succes.writelines("\n" + f"id{member.id} = Succes({member.id}) # Name - {name}\nnames.append('id{member.id}')\nids.append(id{member.id})")
            await ctx.send(f'Utilisateur ajouté')
            
        except:
            await ctx.send(f"Une erreur est survenue")

    else:
        await ctx.send(f"Cet utilisateur est déjà enregistré")
        
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
            succes.writelines("\n" + f'id{member.id}.add_succes("{succes_name}")')
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
    await bot.tree.sync()
    activity = discord.Game(name = "/help")
    await bot.change_presence(status = discord.Status.idle, activity = activity)
    print('Le bot est prêt !')
    print(round(bot.latency * 1000), "ms")

@bot.event
async def on_message(message) : # réaction aux messages (fonctionnel)
    await bot.process_commands(message)
    list_words = ['hey', 'yo', 'coucou', 'cc', 'bonjour', 'bjr', 'bonsoir', 'bsr', 'salutation', 'salutations', 'salut', 'slt', 're', 'wesh', 'wsh', 'salam']

    if message.content.lower() in list_words:
        await message.add_reaction("👋")
    
        if message.author.id == 489470853072027685:
            print(f'Moeru dit "{message.content.lower()}" !')
            await message.reply(f'{message.content} ô Moeru 👋')
        
        else:
            print(f'{message.author} dit "{message.content.lower()}"')

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
    try:
        await member.send("Bienvenue sur notre serveur !")
    
    except:
        pass
    
    if member.guild.id == 1101138795446935643:
        loc = bot.get_channel(1101138795446935646)
        await loc.send(f"### **Bienvenue sur M̸͐̉A̵̿̅K̴̅̊A̶̍́Ï̸̅ ̸̓̾**\n> ||{member.mention}||")

@bot.event
async def on_member_remove(member) : # adieu (fonctionnel)
    print(f'{member} a quitté un de nos serveurs ({member.guild})')


# - - - - - - - - - - - - - - - -  T O K E N  - - - - - - - - - - - - - - - - #


# Sécurisation du Token 
from XXX import TOKEN
bot.run(TOKEN)


# - - - - - - - - - - - - - - - -  I N F O R M A T I O N S  - - - - - - - - - - - - - - - - #

# > Actual version - 1
# > Uid - 3
# > Creation - 2023/08
# > Total scripts - 3