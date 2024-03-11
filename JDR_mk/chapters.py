# - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - #

from discord import *
import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions
from discord.shard import EventType
from discord import app_commands
from nacl import *
from time import sleep
import random as rdm
from .inventory import *
from .mk_db import *


# - - - - - - - - - - -  B U T T O N S  - - - - - - - - - - - #

class button_view(discord.ui.View): # Changement de page (wbk_list)
    def __init__(self, Pid : int, inventory : Inventaire, character : Character):
        super().__init__(timeout = None)
        self.Pid = Pid
        self.ivtr = inventory
        self.char = character
        self.player = Players()
        
    @discord.ui.button(label = "1", custom_id = "choice_1")
    async def left(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.message.edit(view = None)
        await interaction.response.defer()
        
        if self.Pid == 0:
            self.player.set_progression(interaction.user.id, (1, 1))
            page_1(self.ivtr, self.char)

    @discord.ui.button(label = "...", custom_id = "stop")
    async def stop(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.message.edit(view = None)
        await interaction.response.send_message(f'> Session arrêtée, utilisez "**U!jdr_start**" pour reprendre...', ephemeral = True)

    @discord.ui.button(label = "2", custom_id = "choice_2")
    async def reset(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.message.edit(view = None)
        await interaction.response.defer()

        if self.Pid == 0:
            self.player.set_progression(interaction.user.id, (1, 2))
            page_2(self.ivtr, self.char)


# - - - - - - - - - - -  P A G E S  - - - - - - - - - - - #
        
# Definition des pages
def page_1(ivtr : Inventaire, char : Character) : # terminée
    sleep(3)
    print("Narrateur : Vous avancez jusqu'à une grotte obscure plutôt effrayante")
    sleep(1)
    print("1 - Entrer dans la grotte \n2 - Faire demi-tour")

    P1=int(input("Où allez-vous ? "))
    if P1==1 :
        print("Narrateur : Vous avez choisi d'enter dans la grotte")
        page_3(ivtr, char)

    elif P1==2 :
        print("Narrateur : Vous avez choisi de faire demi-tour")
        départ(ivtr, char)

    elif P1 == 0:
        b = breaks(ivtr, char)

        if b:
            page_1(ivtr, char)

    else :
        print("impossible")
        sleep(2)
        page_1(ivtr, char)

def page_2(ivtr : Inventaire, char : Character) : # terminée
    sleep(3)
    print("Narrateur : Vous avancez désormais dans un petit village paraissant abandonné depuis des années quand vous apercevez un énorme orc")
    sleep(1)
    print("1 - Attaquer l'orc \n2 - Vous cacher dans la taverne")

    P2=int(input("Où allez-vous ? "))
    if P2==1 :
        print("Narrateur : L'orc vous broie le crâne avec son immense massue")
        dmg = char.damage(15)
        if not dmg:
            ivtr.reset()
            mort(ivtr, char)

        else:
            print("Narrateur : Vous résistez miraculeusement à son coup, qui vous sonne tout de même, laissant le temps à l'orc de vous assommer")
            dmg = char.damage(5)
            if not dmg:
                ivtr.reset()
                mort(ivtr, char)

            else:
                print("Narrateur : Votre vision diminue jusqu'à ce que vous soyez parfaitement inconscient")
                page_19(ivtr, char)

    elif P2==2 :
        print("Narrateur : Vous entrez donc dans la taverne")
        page_4(ivtr, char)

    elif P2 == 0:
        b = breaks(ivtr, char)

        if b:
            page_2(ivtr, char)

    else :
        print("impossible")
        sleep(2)
        page_2(ivtr, char)  

def page_3(ivtr : Inventaire, char : Character) : # terminée
    sleep(3)
    print("Narrateur : Vous tombez nez à nez avec un ours qui dort couché sur un coffre de trésor")
    sleep(1)
    print("1 - Fuir vers la forêt \n2 - Essayer de prendre le coffre")

    P3=int(input("Où allez-vous ? "))
    if P3==1 :
        print("Narrateur : Vous retournez au coeur de la forêt")
        départ(ivtr, char)

    elif P3==2 :
        print("Narrateur : Vous tentez donc de prendre le coffre")
        page_5(ivtr, char)

    elif P3 == 0:
        b = breaks(ivtr, char)

        if b:
            page_3(ivtr, char)

    else :
        print("impossible")
        page_3(ivtr, char)

def page_4(ivtr : Inventaire, char : Character) : # terminée
    sleep(3)
    print("Narrateur : Vous apercevez un escalier qui descend dans un tunnel souterrain droit devant vous")
    sleep(1)
    print("1 - Descendre dans la cave \n2 - Retourner dans le village")

    P4=int(input("Où allez-vous ? "))
    if P4==1 :
        print("Narrateur : Vous descendez donc dans la cave")
        page_6(ivtr, char)

    elif P4==2 :
        print("Narrateur : Vous rebroussez chemin dans le village")
        page_2(ivtr, char)

    elif P4 == 0:
        b = breaks(ivtr, char)

        if b:
            page_4(ivtr, char)

    else :
        print("impossible")
        page_4(ivtr, char)

def page_5(ivtr : Inventaire, char : Character) : # terminée
    sleep(3)
    print("Narrateur : Quel maladroit ! Vous avez réveillé l'immense bête")
    sleep(1)
    print("1 - Attaquer l'ours à main nue \n2 - Avancer dans la grotte en quête d'un abri")

    P5=int(input("Où allez-vous ? "))
    if P5==1 :
        print("Narrateur : L'ours vous dévore sans difficulté")
        dmg = char.damage(20)
        if not dmg:
            ivtr.reset()
            mort(ivtr, char)

    elif P5==2 :
        print("Narrateur : Vous tentez désespérement de fuir au fond de la grotte")
        page_7(ivtr, char)

    elif P5 == 0:
        b = breaks(ivtr, char)

        if b:
            page_5(ivtr, char)

    else :
        print("impossible")
        page_5(ivtr, char)

def page_6(ivtr : Inventaire, char : Character) : # terminée
    sleep(3)
    print("Vous trouver un vieux coffre rouillé du quel émane une étrange lueure verte")
    sleep(1)
    print("1 - Ouvrir le coffre \n2 - Continuer sa route")

    P6=int(input("Où allez-vous ? "))
    if P6==1 :
        print("Narrateur : Vous ouvrez l'étrange coffre")
        page_8(ivtr, char)

    elif P6==2 :
        print("Narrateur : Vous poursuivez votre chemin dans la cave")
        page_9(ivtr, char)

    elif P6 == 0:
        b = breaks(ivtr, char)

        if b:
            page_6(ivtr, char)

    else :
        print("impossible")
        page_6(ivtr, char)

def page_7(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("Narrateur : Vous atteignez le fond de la grotte et apercevez une petite épée ainsi qu'une cavité où vous serez en sécurité, mais vous n'avez pas le temps de prendre l'épée et de vous cacher")
    sleep(1)
    print("1 - Prendre l'épée \n2 - Vous cacher dans la cavité")

    P7=int(input("Où allez-vous ? "))
    if P7==1 :
        print("Narrateur : Vous prenez donc cette magnifique arme en argent")
        ivtr.add('dague en argent')
        page_10(ivtr, char)

    elif P7==2 :
        print("Narrateur : Vous avez fait le choix de vous cacher dans la cavité")
        page_11(ivtr, char)

    elif P7 == 0:
        b = breaks(ivtr, char)

        if b:
            page_7(ivtr, char)

    else :
        print("impossible")
        page_7(ivtr, char)

def page_8(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("Narrateur : vous trouvez un grand coutelas aiguisé ainsi que 20 pièces d'or, puis vous entendez des bruits étranges dans toute la cave")
    ivtr.add("Or", 20)
    ivtr.add("grand coutelas", 1)
    sleep(1)
    print("1 - Chercher la provenance du bruit \n2 - Fuir au rez-de-chaussée")

    P8=int(input("Où allez-vous ? "))
    if P8==1 :
        print("Narrateur : Vous vous enfoncez dans les ténebres")
        page_12(ivtr, char)

    elif P8==2 :
        print("Narrateur : Vous rebroussez chemin")
        page_13(ivtr, char)

    elif P8 == 0:
        b = breaks(ivtr, char)

        if b:
            page_8(ivtr, char)

    else :
        print("impossible")
        page_8(ivtr, char)

def page_9(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("Narrateur : vous atteignez le fond de la cave quand les torches s'éteignent subitement")
    sleep(1)
    print("1 - Tenter de retrouver la sortie \n2 - Essayer de rallumer les torches")

    P9=int(input("Où allez-vous ? "))
    if P9==1 :
        print("Narrateur : Vous avancez à tatons jusqu'à la porte de la cave")
        page_14(ivtr, char)

    elif P9==2 :
        print("Narrateur : Vous tentez d'allumer un petit feu")
        page_15(ivtr, char)

    elif P9 == 0:
        b = breaks(ivtr, char)

        if b:
            page_9(ivtr, char)

    else :
        print("impossible")
        page_9(ivtr, char)

def page_10(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

def page_11(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

def page_12(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("Narrateur : vous atteignez le fond de la cave quand les torches s'éteignent subitement")
    sleep(1)
    print("1 - Tenter de retrouver la sortie \n2 - Continuer de chercher la source du bruit")

    P12=int(input("Où allez-vous ? "))
    if P12==1 :
        print("Narrateur : Vous avancez à tatons jusqu'à la porte de la cave")
        page_14(ivtr, char)

    elif P12==2 :
        print("Narrateur : Vous vous avancez jusqu'à une petit trappe entrouverte")
        page_18(ivtr, char)

    elif P12 == 0:
        b = breaks(ivtr, char)

        if b:
            page_12(ivtr, char)

    else :
        print("impossible")
        page_12(ivtr, char)

def page_13(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

def page_14(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("Narrateur : Lorsque vous essayez d'ouvrir la porte, celle-ci craque mais vous résiste")
    sleep(1)
    print("1 - Forcer la porte de la cave \n2 - Chercher une autre sortie")

    P14=int(input("Où allez-vous ? "))
    if P14==1 :
        if char.atk >= 12:
            print("Narrateur : Vous essayez de briser la porte pour vous frayer un passage")
            page_16(ivtr, char)

        else:
            print("Narrateur : Vous tentez de forcer le passage mais votre force est insuffisante")
            page_14(ivtr, char)

    elif P14==2 :
        print("Narrateur : Vous vous avancez jusqu'à une petit trappe entrouverte")
        page_17(ivtr, char)

    elif P14 == 0:
        b = breaks(ivtr, char)

        if b:
            page_14(ivtr, char)

    else :
        print("impossible")
        page_14(ivtr, char)

def page_15(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

def page_16(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

def page_17(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

def page_18(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

def page_19(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("Narrateur : Vous vous réveillez dans un petite cage en bois, avec tout votre équiment")
    sleep(1)
    print("1 - Forcer la porte de la cage \n2 - Appeler à l'aide")

    P19=int(input("Où allez-vous ? "))
    if P19==1 :
        if char.atk > 8:
            print("Narrateur : Vous essayez de briser la porte pour vous enfuir")
            page_20(ivtr, char)

        else:
            print("Narrateur : Vous tentez de forcer le passage mais votre force est insuffisante")
            page_19(ivtr, char)

    elif P19==2 :
        print("Narrateur : Vous criez jusqu'à rameuter plusieurs orcs semblants prêts à vous tuer")
        page_21(ivtr, char)

    elif P19 == 0:
        b = breaks(ivtr, char)

        if b:
            page_19(ivtr, char)

    else :
        print("impossible")
        page_19(ivtr, char)

def page_20(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

def page_21(ivtr : Inventaire, char : Character) :
    sleep(3)
    print("")

# Début de l'aventure
async def départ(ctx : commands.Context, ivtr : Inventaire, char : Character):
    embed = discord.Embed(title = '**CHAPITRE  1  -  DÉPART**', description = "> **Narrateur :** Vous arrivez donc dans une magnifique forêt, quoiqu'un peu sombre, puis le chemin se sépare en deux\n\n**1 -** Continuer vers le nord \n**2 -** Continuer vers le sud", color = 0x00ffff)
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar)
    await ctx.send(embed = embed, view = button_view(0, ivtr, char))

# Fin de l'aventure
def mort(ivtr : Inventaire, char : Character):
    sleep(3)
    print("Narrateur : Votre aventure s'arrête malheuresement ici, suite à votre terrible mort")
    sleep(1)
    print("1 - Rejouer \n2 - Terminer")
    M1 = int(input("Que choississez-vous ? "))

    if M1 == 1:
        char.reset()
        print("Narrateur : Le temps s'estompe peu à peu... jusqu'à votre nouveau reveil\n")
        sleep(1)
        départ(ivtr, char)

    elif M1 == 2:
        print("Narrateur : Le temps s'estompe peu à peu... et vous rejoignez lentement le monde des défunts")
        sleep(1)

    else:
        print("impossible")
        mort(ivtr, char)

# Menu de pause
def breaks(ivtr : Inventaire, char : Character):
    sleep(1)
    print('\n> - P A U S E - <')
    sleep(2)
    print("1 - Reprendre l'aventure \n2 - Consulter l'inventaire \n3 - Quittez l'aventure")
    Brk = int(input("Que voulez-vous faire ? "))
    print(" ")

    if Brk == 2:
        sleep(2)
        print('> - I N V E N T A I R E - <')
        sleep(0.5)
        ivtr.show_inventory()
        print(" ")
        sleep(1)
        print("1 - Reprendre l'aventure \n2 - Équiper un objet \n3 - Utiliser un consommable")
        BrkI = int(input("Que voulez-vous faire ? "))

        if BrkI == 2:
            item = input("Nom de l'objet - ")
            char.equip(item)

        elif BrkI == 3:
            item = input("Nom de l'objet - ")
            char.potion_use(item)

        elif BrkI != 1:
            print("impossible")

        print(" ")
        sleep(0.5)

    elif Brk == 3:
        return False

    elif Brk != 1:
        print("impossible")
    
    return True 

# - - - - - - - - - - -  A U T R E S  - - - - - - - - - - - #

