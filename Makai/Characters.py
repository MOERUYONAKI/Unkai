# - - - - - - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - - - - - - #


import discord 
from discord.ext import commands
import json


# - - - - - - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - - - - - - #


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = 'U!', description = 'narrateur rp', intents = intents)


# - - - - - - - - - - - - - - - -  C O M M A N D E S  - - - - - - - - - - - - - - - - #


async def get_user(interaction : discord.Interaction, member : discord.User = None):
    with open("Makai\\ressources\\characters.json", "r") as json_file:
        characters = json.load(json_file)

    if member == None:
        member = interaction.user

    if f'Uid{member.id}' in characters.keys():
        embed = discord.Embed(title = f"{characters[f'Uid{member.id}']['Nom du personnage']} - rang {characters[f'Uid{member.id}']['rang']}")
        embed.set_author(name = member.name, icon_url = member.avatar.url)
        
        elts = ''
        for i in range(len(characters[f'Uid{member.id}']['elements'])):
            elts += f"> {characters[f'Uid{member.id}']['elements'][i]} \n"
        
        embed.add_field(name = f'Éléments -', value = elts, inline = False)
        
        stats = ''
        for stat in characters[f'Uid{member.id}']['statistiques'].keys():
            stats += f"> **{stat} -** {characters[f'Uid{member.id}']['statistiques'][stat]} \n"
        
        embed.add_field(name = f'Statistiques -', value = stats, inline = False)
        
        points = ''
        for point in characters[f'Uid{member.id}']['points'].keys():
            points += f"> **{point} -** {characters[f'Uid{member.id}']['points'][point]} \n"
        
        embed.add_field(name = f'Points -', value = points)

        await interaction.response.send_message(embed = embed)
    
    else:
        await interaction.response.send_message("> Aucun résultat trouvé...", ephemeral = True)

async def create_user(interaction : discord.Interaction, member : discord.User, nom : str, faction : discord.app_commands.Choice[str], élément : discord.app_commands.Choice[str], force : int, défense : int, agilité : int, perception : int, magie):
    with open("Makai\\ressources\\characters.json", "r") as json_file:
        characters = json.load(json_file)

    if f'Uid{member.id}' in characters.keys():
        await interaction.response.send_message("> Ce joueur possède déjà un personnage...", ephemeral = True)

    else:
        rang = ''
        pv = 20
        rang_value = 0
        stats = [force, défense, agilité, perception, magie]

        for key in stats:
            if key < 4:
                rang_value += 1
                
            elif key < 8:
                rang_value += 2
                
            elif key < 12:
                rang_value += 3
                
            elif key <= 20:
                rang_value += 4

            else:
                rang_value += 6

        if rang_value <= 5:
            rang = "F"

        elif rang_value == 6 or rang_value == 7:
            rang = "E"
            pv += 5

        elif rang_value == 8 or rang_value == 9:
            rang = "D"
            pv += 10

        elif rang_value > 9 and rang_value < 13:
            rang = "C"
            pv += 15

        elif rang_value > 12 and rang_value < 16:
            rang = "B"
            pv += 20

        elif rang_value > 15 and rang_value <= 20:
            rang = "A"
            pv += 25

        elif rang_value > 20:
            rang = "S"
            pv += 30

        user = {
            "Nom du personnage" : nom,
            "Faction" : faction.value,
            "rang" : rang,
            "elements" : [
                élément.value
            ],
            "statistiques" : {
                "Force" : force, 
                "Defense" : défense, 
                "Agilite" : agilité, 
                "Perception" : perception, 
                "Magie" : magie, 
                "Points de vie" : pv, 
                "Sante mentale" : 10, 
                "Chance" : 1
            },
            "points" : {
                "Plausibilite" : 0,
                "Evolution" : 0,
                "Eveil" : 0,
                "Argent" : 50
            },
            "elements" : []
        }

        characters[f'Uid{member.id}'] = user

        with open("Makai\\ressources\\characters.json", "w") as json_file_writting:
            json.dump(characters, json_file_writting, indent = 4)

        await interaction.response.send_message(f"> Le personnage de {member.mention} a été créé avec succès...", ephemeral = True)

async def add_stats(interaction : discord.Interaction, member : discord.User, force : discord.app_commands.Choice[int], défense : discord.app_commands.Choice[int], agilité : discord.app_commands.Choice[int], perception : discord.app_commands.Choice[int], magie : discord.app_commands.Choice[int]):
    with open("Makai\\ressources\\characters.json", "r") as json_file:
        characters = json.load(json_file)
    
    if f'Uid{member.id}' not in characters.keys():
        await interaction.response.send_message("> Vous ne possèdez pas de personnage...", ephemeral = True)

    else:
        rang_actuel = characters[f'Uid{member.id}']['rang']
        total = force.value + défense.value + agilité.value + perception.value + magie.value
        rang_value = 0

        if total < int(characters[f'Uid{member.id}']['points']["Evolution"]):
            interaction.response.send_message("> Vous n'avez pas assez de points...", ephemeral = True)

        else:
            characters[f'Uid{member.id}']['points']["Evolution"] -= total

            characters[f'Uid{member.id}']['statistiques']['Force'] += force.value
            characters[f'Uid{member.id}']['statistiques']['Defense'] += défense.value
            characters[f'Uid{member.id}']['statistiques']['Agilite'] += agilité.value
            characters[f'Uid{member.id}']['statistiques']['Perception'] += perception.value
            characters[f'Uid{member.id}']['statistiques']['Magie'] += magie.value

            for key in characters[f'Uid{member.id}']['statistiques'].keys():
                if characters[f'Uid{member.id}']['statistiques'][key] < 4:
                    rang_value += 1
                    
                elif characters[f'Uid{member.id}']['statistiques'][key] < 8:
                    rang_value += 2
                    
                elif characters[f'Uid{member.id}']['statistiques'][key] < 12:
                    rang_value += 3
                    
                elif characters[f'Uid{member.id}']['statistiques'][key] <= 20:
                    rang_value += 4

                else:
                    rang_value += 6

                if rang_value <= 5:
                    rang = "F"

                elif rang_value == 6 or rang_value == 7:
                    rang = "E"

                elif rang_value == 8 or rang_value == 9:
                    rang = "D"

                elif rang_value > 9 and rang_value < 13:
                    rang = "C"

                elif rang_value > 12 and rang_value < 16:
                    rang = "B"

                elif rang_value > 15 and rang_value <= 20:
                    rang = "A"

                elif rang_value > 20:
                    rang = "S"

                characters[f'Uid{member.id}']['rang'] = rang

                with open("Makai\\ressources\\characters.json", "w") as json_file_writting:
                    json.dump(characters, json_file_writting, indent = 4)

                await interaction.response.send_message(f"> Vos statistiques ont été modifiées avec succès... \n{f'|| Vous avez atteint le rang {rang} ||' if str(rang) != str(rang_actuel) else ''}", ephemeral = True)

async def add_points(interaction : discord.Interaction, member : discord.User, plausibilité : int = 0, éveil : int = 0, évolution : int = 0, argent : int = 0):
    with open("Makai\\ressources\\characters.json", "r") as json_file:
        characters = json.load(json_file)
    
    if f'Uid{member.id}' not in characters.keys():
        await interaction.response.send_message("> Ce joueur ne possède pas de personnage...", ephemeral = True)

    else:
        characters[f'Uid{member.id}']['points']['Plausibilite'] += plausibilité
        characters[f'Uid{member.id}']['points']['Eveil'] += éveil
        characters[f'Uid{member.id}']['points']['Evolution'] += évolution
        characters[f'Uid{member.id}']['points']['Argent'] += argent

        with open("Makai\\ressources\\characters.json", "w") as json_file_writting:
            json.dump(characters, json_file_writting, indent = 4)

        await interaction.response.send_message(f'> Les points ont été ajoutés...', ephemeral = True)

async def add_élément(interaction : discord.Interaction, element : discord.app_commands.Choice[str]):
    with open("Makai\\ressources\\characters.json", "r") as json_file:
        characters = json.load(json_file)
    
    if f'Uid{interaction.user.id}' not in characters.keys():
        await interaction.response.send_message("> Vous ne possèdez pas de personnage...", ephemeral = True)

    else:
        if not characters[f'Uid{interaction.user.id}']['points']['Eveil'] > 0:
            await interaction.response.send_message(f'> Vos points d\'éveil sont insuffisants...', ephemeral = True)

        else:
            if element.value not in characters[f'Uid{interaction.user.id}']['elements']:
                characters[f'Uid{interaction.user.id}']['elements'].append(element.value)
                characters[f'Uid{interaction.user.id}']['points']['Eveil'] -= 1

                with open("Makai\\ressources\\characters.json", "w") as json_file_writting:
                    json.dump(characters, json_file_writting, indent = 4)

                await interaction.response.send_message(f'> L\'élément **{element.name}** a été ajouté...', ephemeral = True)

            else:
                await interaction.response.send_message(f'> Vous possédez déjà cet élément...', ephemeral = True)

async def fusion(interaction : discord.Interaction, first_element : discord.app_commands.Choice[str], second_element : discord.app_commands.Choice[str]):
    with open("Makai\\ressources\\characters.json", "r") as json_file:
        characters = json.load(json_file)
    
    if f'Uid{interaction.user.id}' not in characters.keys():
        await interaction.response.send_message("> Vous ne possèdez pas de personnage...", ephemeral = True)

    else:
        if not characters[f'Uid{interaction.user.id}']['points']['Eveil'] > 0:
            await interaction.response.send_message(f'> Vos points d\'éveil sont insuffisants...', ephemeral = True)

        else:
            if first_element.value in characters[f'Uid{interaction.user.id}']['elements'] and second_element.value in characters[f'Uid{interaction.user.id}']['elements']:
                elts = [first_element.value, second_element.value]
                new_elt = ""

                # - Fusions Primaires
                if "feu" in elts and "eau" in elts:
                    new_elt = "brume"

                elif "vent" in elts and "eau" in elts:
                    new_elt = "glace"

                elif "feu" in elts and "terre" in elts:
                    new_elt = "cendre"

                elif "vent" in elts and "terre" in elts:
                    new_elt = "roche"

                elif "foudre" in elts and "feu" in elts:
                    new_elt = "plasma"

                # - Fusions Radiantes
                elif "vent" in elts and "cendre" in elts:
                    new_elt = "fumée"

                elif "feu" in elts and "roche" in elts:
                    new_elt = "magma"

                elif "foudre" in elts and "roche" in elts:
                    new_elt = "métal"

                elif "brume" in elts and "cendre" in elts:
                    new_elt = "fumée explosive"

                if new_elt not in characters[f'Uid{interaction.user.id}']['elements'] and new_elt != "":
                    characters[f'Uid{interaction.user.id}']['elements'].append(new_elt)
                    characters[f'Uid{interaction.user.id}']['points']['Eveil'] -= 1

                    with open("Makai\\ressources\\characters.json", "w") as json_file_writting:
                        json.dump(characters, json_file_writting, indent = 4)

                    await interaction.response.send_message(f'> L\'élément **{new_elt}** a été ajouté...', ephemeral = True)

                else:
                    if new_elt == "":
                        await interaction.response.send_message(f'> Aucune fusion n\'a été trouvée...', ephemeral = True)

                    elif new_elt in characters[f'Uid{interaction.user.id}']['elements']:
                        await interaction.response.send_message(f'> Vous possédez déjà cet élément...', ephemeral = True)

            else:
                await interaction.response.send_message(f'> Vous ne possédez pas ces éléments...', ephemeral = True)

#! à ajouter - shop (selon l'argent)