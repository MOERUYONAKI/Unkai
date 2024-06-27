# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


import Others.rolls as r
from discord import *
import discord 
from discord.ext import commands
from time import *


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)

def attribute():
    roll = r.eveil_roll("base")

    if roll[0] < 4000:
        value = "faible"

    elif roll[0] >= 8000:
        value = "élevé"

    else:
        value = "moyen"

    return [roll, value]

def rangs(stats : list):
    temp_rang = 0

    for stat in stats:
        if stat == "faible":
            temp_rang += 1

        elif stat == "moyen":
            temp_rang += 2

        elif stat == "élevé":
            temp_rang += 3 

        elif stat == "supérieur":
            temp_rang += 4

        elif stat == "maître":
            temp_rang += 6

    if temp_rang <= 5:
        rang = "F"

    elif temp_rang == 6 or temp_rang == 7:
        rang = "E"

    elif temp_rang == 8 or temp_rang == 9:
        rang = "D"

    elif temp_rang > 9 and temp_rang < 13:
        rang = "C"

    elif temp_rang > 12 and temp_rang < 16:
        rang = "B"

    elif temp_rang > 15 and temp_rang <= 20:
        rang = "A"

    elif temp_rang > 20:
        rang = "S"

    return rang


# - - - - - - - - - - - - - - - -  C O M M A N D E S  - - - - - - - - - - - - - - - - #


async def test_eveil(interaction : discord.Interaction, user : discord.User, button_view):
    await interaction.response.defer(thinking = True)

    agilité = attribute()
    puissance = attribute()
    résistance = attribute()
    perception = attribute()
    magie = attribute()
    
    rolls = [agilité[0][0], puissance[0][0], résistance[0][0], perception[0][0], magie[0][0]]
    for i in range(len(rolls)):
        if rolls[i] > 9500:
            if i == 0:
                view = button_view()
                m1 = await interaction.channel.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Agilité" + "\n" +
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                await view.wait()

                if view.value == 1:
                    ag_roll = r.eveil_roll("sup")
                    agilité[0][0] = 7500 + ag_roll

                    if ag_roll < 500:
                        agilité[1] = "moyen"

                    elif ag_roll >= 4500:
                        agilité[1] = "supérieur"

                    else:
                        agilité[1] = "élevé"

                    sleep(0.5)

                    await m1.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Agilité" + "\n" +
                            f"> **Résultat :** {agilité[1]} *({ag_roll})*"), view = None, delete_after = 20)

            if i == 1:
                view = button_view()
                m2 = await interaction.channel.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Puissance" + "\n" +
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                await view.wait()

                if view.value == 1:
                    ps_roll = r.eveil_roll("sup")
                    puissance[0][0] = 7500 + ps_roll

                    if ps_roll < 500:
                        puissance[1] = "moyen"

                    elif ps_roll >= 4500:
                        puissance[1] = "supérieur"

                    else:
                        puissance[1] = "élevé"

                    sleep(0.5)

                    await m2.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Puissance" + "\n" +
                            f"> **Résultat :** {puissance[1]} *({ps_roll})*"), view = None, delete_after = 20)

            if i == 2:
                view = button_view()
                m3 = await interaction.channel.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Résistance" + "\n" +
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                await view.wait()

                if view.value == 1:
                    rs_roll = r.eveil_roll("sup")
                    résistance[0][0] = 7500 + rs_roll 

                    if rs_roll < 500: 
                        résistance[1] = "moyen"

                    elif rs_roll >= 4500:
                        résistance[1] = "supérieur"

                    else:
                        résistance[1] = "élevé"

                    sleep(0.5)

                    await m3.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Résistance" + "\n" +
                            f"> **Résultat :** {résistance[1]} *({rs_roll})*"), view = None, delete_after = 20)

            if i == 3:
                view = button_view()
                m4 = await interaction.channel.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Perception" + "\n" + 
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                await view.wait()

                if view.value == 1:
                    pr_roll = r.eveil_roll("sup")
                    perception[0][0] = 7500 + pr_roll

                    if pr_roll < 500:
                        perception[1] = "moyen"

                    elif pr_roll >= 4500:
                        perception[1] = "supérieur"

                    else:
                        perception[1] = "élevé"

                    sleep(0.5)

                    await m4.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Perception" + "\n" +
                            f"> **Résultat :** {perception[1]} *({pr_roll})*"), view = None, delete_after = 20)

            if i == 4:
                view = button_view()
                m4 = await interaction.channel.send(f"### __**Test supérieur**__" + "\n" +
                         f"> Vous êtes apte à passer le **test supérieur** - catégorie Magie" + "\n" + 
                         f"*Ps : il est important qu'un test supérieurs peut détecter une erreur au test précédent et rectifier votre catégorie au niveau moyen*", view = view)

                await view.wait()

                if view.value == 1:
                    mg_roll = r.eveil_roll("sup")
                    magie[0][0] = 7500 + mg_roll

                    if mg_roll < 500:
                        magie[1] = "moyen"

                    elif mg_roll >= 4500:
                        magie[1] = "supérieur"

                    else:
                        magie[1] = "élevé"

                    sleep(0.5)

                    await m4.edit(content = (f"### __**Test supérieur**__" + "\n" +
                            f"> Vous êtes apte à passer le **test supérieur** - catégorie Magie" + "\n" + 
                            f"> **Résultat :** {magie[1]} *({mg_roll})*"), view = None, delete_after = 20)
    
    lvls = [agilité[1], puissance[1], résistance[1], perception[1], magie[1]]
    rang = rangs(lvls)

    embed = Embed(title = "Résultats - éveil", color = 0x2C2F33)
    embed.set_author(name = user.name, icon_url = user.avatar.url)

    agilité_text = f"> **{agilité[0][0]}** \n> *{agilité[0][1][0]} / {agilité[0][1][1]}*"
    try: 
        agilité_text += f"\n> *{ag_roll}*" 
    except: 
        pass

    puissance_text = f"> **{puissance[0][0]}** \n> *{puissance[0][1][0]} / {puissance[0][1][1]}*"
    try: 
        puissance_text += f"\n> *{ps_roll}*"
    except: 
        pass

    résistance_text = f"> **{résistance[0][0]}** \n> *{résistance[0][1][0]} / {résistance[0][1][1]}*"
    try:
        résistance_text += f"\n> *{rs_roll}*"
    except:
        pass

    perception_text = f"> **{perception[0][0]}** \n> *{perception[0][1][0]} / {perception[0][1][1]}*"
    try:
        perception_text += f"\n> *{pr_roll}*"
    except:
        pass

    magie_text = f"> **{magie[0][0]}** \n> *{magie[0][1][0]} / {magie[0][1][1]}*"
    try:
        magie_text += f"\n> *{mg_roll}*"
    except:
        pass

    embed.add_field(name = "Agilité", value = agilité_text, inline = False)
    embed.add_field(name = "Puissance", value = puissance_text, inline = False)
    embed.add_field(name = "Résistance", value = résistance_text, inline = False)
    embed.add_field(name = "Perception", value = perception_text, inline = False)
    embed.add_field(name = "Magie", value = magie_text, inline = False)
    
    sleep(1.5)
    print(f'Un test vient de s\'achever : \n> Rang {rang}')

    await interaction.followup.send(f"### __**Test d'éveil**__" + "\n" +
                                f"Le test est désormais terminé :" + "\n"
                                f"> ||Rang {rang}||" + "\n" + "\n" + 
                                f"> **Agilité :** {agilité[1]}" + "\n" +
                                f"> **Puissance :** {puissance[1]}" + "\n" + 
                                f"> **Résistance :** {résistance[1]}" + "\n" + 
                                f"> **Perception :** {perception[1]}" + "\n" + 
                                f"> **Magie :** {magie[1]}", embed = embed)