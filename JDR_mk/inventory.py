# - - - - - - - - - - -  I M P O R T S  - - - - - - - - - - - #

import random as rdm
from time import sleep


# - - - < J S O N > - - - #

import json

def get_item_list():
    with open('C:\\Users\\1bbor\\.vscode\\Dev\\bot UNKAI\\JDR_mk\\Ressources\\items.json', encoding = 'utf-8') as itm_bk:
        items_bank = json.load(itm_bk)

    item_list = []
    for elt in items_bank["armes"]:
        item_list.append(elt)

    for elt in items_bank["consommables"]:
        item_list.append(elt)

    for elt in items_bank["équipements"]:
        item_list.append(elt)

    for elt in items_bank["objets"]:
        item_list.append(elt)

    return item_list

with open('C:\\Users\\1bbor\\.vscode\\Dev\\bot UNKAI\\JDR_mk\\Ressources\\items.json', encoding = 'utf-8') as itm_bk:
    items_bank = json.load(itm_bk)

with open('C:\\Users\\1bbor\\.vscode\\Dev\\bot UNKAI\\JDR_mk\\Ressources\\monster_drops.json', encoding = 'utf-8') as mstr_dp:
    monsterdrop = json.load(mstr_dp)

with open('C:\\Users\\1bbor\\.vscode\\Dev\\bot UNKAI\\JDR_mk\\Ressources\\items_stats.json', encoding = 'utf-8') as itm_st:
    items_stats = json.load(itm_st)

item_list = get_item_list()


# - - - - - - - - - - -  C L A S S E S  - - - - - - - - - - - #

# Inventaire
class Inventaire():
    ''' Permet de créer et consulter son inventaire '''
    def __init__(self):
        self.items = items_bank
        self.inventory = {'or' : 0}

    def monsterdrop(self, lvl : int = 1): # Loot de monstre (aléatoire)
        if 0 < lvl < 4:
            mdrop = monsterdrop[f'level {lvl}']
            gold = rdm.randint(5, (2 + lvl) * 5)

            self.add(mdrop)
            self.add(nbr = gold)

            return [rdm.choices(mdrop), gold]

    def total(self): # Nombre total d'items dans l'inventaire
        nbr_of_items = 0
        for key in self.inventory.keys():
            nbr_of_items += self.inventory[key]

        return nbr_of_items

    def add(self, obj : str = "or", nbr : int = 1): # Ajoute l'objet demandé dans l'inventaire s'il est valide
        obj = obj.lower()
        if obj in item_list:
            if obj in self.inventory.keys():
                self.inventory[obj] = int(self.inventory[obj]) + nbr
            
            else:
                self.inventory[obj] = nbr

    def remove(self, obj : str = "or", nbr : int = 1): # Retire l'objet demandé dans l'inventaire s'il est présent dans celui-ci
        obj = obj.lower()
        if obj in self.inventory.keys() and int(self.items[obj]) > 0:
            if int(self.items[obj]) - nbr < 0:
                self.items[obj] = 0
            
            else:
                 self.items[obj] = int(self.items[obj]) - nbr
    
    def reset(self): # Réinitialise l'inventaire
        self.inventory = {'or' : 0}

    def show_inventory(self): # Affiche le contenue de l'inventaire
        for key in self.inventory.keys():
            print(f'{key} - {self.inventory[key]}')

    def is_armes(self, item : str): # Vérifie si l'item est catégorisé comme 'arme'
        if item.lower() in self.inventory.keys():
            if item.lower() in items_bank["armes"]:
                return True
            
    def is_equipements(self, item : str): # Vérifie si l'item est catégorisé comme 'équipement'
        if item.lower() in self.inventory.keys():
            if item.lower() in items_bank["équipements"]:
                return True
            
    def is_consommables(self, item : str): # Vérifie si l'item est catégorisé comme 'consommable'
        if item.lower() in self.inventory.keys():
            if item.lower() in items_bank["consommables"]:
                return True

# Personnage
class Character():
    ''' Permet de créer un personnage et ses attributs '''
    def __init__(self, name : str, inventory : Inventaire = Inventaire(), equipement : tuple = (None, None, None, None, None, None)):
        self.name = name
        self.inventory = inventory

        # ArmPpl - arme principal, ArmSnd - arme secondaire, ArrPpl - armure principale, ArrBrs - armure bras, ArrHd - armure tête, ArrJmb - armure jambe
        self.equipement = {'ArmPpl' : equipement[0], 'ArmSnd' : equipement[1], 'ArrPpl' : equipement[2], 'ArrBrs' : equipement[3], 'ArrHd' : equipement[4], 'ArrJmb' : equipement[5]}

        # Statistiques par défaut
        self.hp = 12
        self.mp = 8
        self.atk = 4
        self.dfs = 4

        self.max = {'hp' : 12, 'mp' : 8}

    def equip(self, item : str): # Équipe l'item si possible et modifie les statistiques en conséquence
        item = item.lower()
        if self.inventory.is_armes(item) or self.inventory.is_equipements(item):
            if self.equipement[items_stats[f'{item}']['id']] != None:
                base_item = self.equipement[items_stats[f'{item}']['id']]
                if self.inventory.is_armes(base_item):
                    self.atk -= items_stats[f'{base_item}']['atk']

                elif self.inventory.is_equipements(base_item):
                    self.dfs -= items_stats[f'{base_item}']['dfs']

            self.equipement[items_stats[f'{item}']['id']] = item
            if self.inventory.is_armes(item):
                self.atk += items_stats[f'{item}']['atk']

            elif self.inventory.is_equipements(item):
                self.dfs += items_stats[f'{item}']['dfs']

    def show_equipement(self): # Affiche l'équipement du personnage
        a = False
        if self.equipement['ArmPpl'] != None:
            print(f'Arme principale - {self.equipement["ArmPpl"]}')
            a = True

        if self.equipement['ArmSnd'] != None:
            print(f'Arme secondaire - {self.equipement["ArmSnd"]}')
            a = True

        if self.equipement['ArrPpl'] != None:
            print(f'Armure principale - {self.equipement["ArrPpl"]}')
            a = True

        if self.equipement['ArrHd'] != None:
            print(f'Armure tête - {self.equipement["ArrHd"]}')
            a = True

        if self.equipement['ArrBrs'] != None:
            print(f'Armure bras - {self.equipement["ArrBrs"]}')
            a = True

        if self.equipement['ArrJmb'] != None:
            print(f'Armure jambe - {self.equipement["ArrJmb"]}')
            a = True

        if a == False:
            print('Aucun item équipé')

    def show_stats(self): # Affiche les statistiques du personnage
        print(f'Points de vie - {self.hp} \nPoints de mana - {self.mp} \nAttaque - {self.atk} \nDéfense - {self.dfs}')

    def damage(self, nbr : int): # Calcul une diminution des 'hp' selon un nombre donné de dégats
        if nbr == self.dfs:
            self.hp -= 1

        elif nbr > self.dfs:
            self.hp -= nbr - (self.dfs - 1)

        if self.hp > 0:
            return True
        
        else:
            return False
        
    def potion_use(self, item : str): # Utilise le consommable souhaité si possible
        item = item.lower()
        if self.inventory.is_consommables(item):
            if items_stats[f'{item}']['id'] == "Heal":
                if self.hp < self.max['hp']:
                    self.inventory.remove(item)

                    if self.hp + items_stats[f'{item}']['hp'] >= self.max['hp']:
                        self.hp = self.max['hp']

                    else:
                        self.hp += items_stats[f'{item}']['hp']
                        
                    return 'Potion consommée avec succès'

            elif items_stats[f'{item}']['id'] == "Mana":
                if self.mp < self.max['mp']:
                    self.inventory.remove(item)

                    if self.hp + items_stats[f'{item}']['mp'] >= self.max['mp']:
                        self.mp = self.max['mp']

                    else:
                        self.mp += items_stats[f'{item}']['mp']
                        
                    return 'Potion consommée avec succès'

            elif items_stats[f'{item}']['id'] == "Atk":
                self.atk += items_stats[f'{item}']['atk']
                self.inventory.remove(item)
                return 'Potion consommée avec succès'
            
            return 'Impossible'
        
    def reset(self, invent : bool = False): # Réinitialise le personnage en gardant l'inventaire actuel ou non
        if invent:
            self = Character(self.name, self.inventory.reset())
        
        else:
            self = Character(self.name, self.inventory)

        return 'Personnage réinitialisé avec succès'