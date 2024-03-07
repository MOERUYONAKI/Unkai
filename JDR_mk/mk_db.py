import mariadb

class Players():
    def __init__(self):
        self.database = 'unkai_jdr'


    # - USERS

    def user_is_register(self, userid : int): # Vérifie si un utilisateur est enregistré par son ID discord
        Uid = f'Uid{userid}'

        database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
        crs = database.cursor()

        crs.execute(f'SELECT ID FROM users WHERE discord_id = "{Uid}";')
        database.close()

        return True if len(crs.fetchall()) > 0 else False
    
    def add_user(self, username : str, userid : int): # Enregistre un utilisateur s'il ne l'est pas déjà
        if self.user_is_register(userid):
            return False
        
        else:
            Uid = f'Uid{userid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'INSERT INTO users (`username`, `chapter_id`, `page_id`, `discord_id`) VALUES ("{username}", 1, 1, "{Uid}");')
            database.close()

            return True
        
    def get_id_by_Uid(self, userid : int):
        if not self.user_is_register(userid):
            return False
        
        else:
            Uid = f'Uid{userid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT ID FROM users WHERE discord_id = "{Uid}";')
            DBid = crs.fetchall()
            database.close()

            return DBid[0][0]
        
    def get_progression(self, userid : int): # Renvoie un tuple contenant le chapitre et la page où le joueur s'est arrêté
        if not self.user_is_register(userid):
            return False
        
        else:
            Uid = f'Uid{userid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT chapter_id, page_id FROM users WHERE discord_id = "{Uid}";')
            DBid = crs.fetchall()
            database.close()

            return DBid[0]
        
    def set_progression(self, userid : int, new_progression : tuple): # Modifie le chapitre et la page où le joueur s'est arrêté
        if not self.user_is_register(userid) or type(new_progression) != 'tuple':
            return False
        
        else:
            Uid = f'Uid{userid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE `users` SET `chapter_id` = "{new_progression[0]}", `page_id` = "{new_progression[1]}" WHERE discord_id = "{Uid}";')
            database.close()

            return True


    # - ITEMS

    def get_item_id(self, item_name : str): # Renvoie l'ID de l'item s'il existe
        database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
        crs = database.cursor()

        crs.execute(f'SELECT ID FROM items WHERE itemname = "{item_name}";')
        DBid = crs.fetchall()
        database.close()

        try:
            return DBid[0][0] 
        
        except:
            return False


    # - INVENTORY

    def is_in_inventory(self, Uid : int, item_name : str):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)

        if userid == False or itemid == False:
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT * FROM inventory WHERE item_id = "{itemid}" AND user_id = "{userid}";')
            database.close()

            return True if len(crs.fetchall()) > 0 else False
        
    def get_quantity(self, Uid : int, item_name : str):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)

        if userid == False or itemid == False or not self.is_in_inventory(Uid, item_name):
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT quantity FROM inventory WHERE item_id = "{itemid}" AND user_id = "{userid}";')
            DBid = crs.fetchall()
            database.close()

            return DBid[0][0]
        
    def add_items(self, Uid : int, item_name : str, quantity : int):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)
        actual_quantity = self.get_quantity(Uid, item_name)

        if userid == False or itemid == False or actual_quantity == False or actual_quantity + quantity < 0:
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            if self.is_in_inventory(Uid, item_name):
                crs.execute(f'UPDATE `inventory` SET `quantity` = "{actual_quantity + quantity}" WHERE `item_id` = "{itemid}" AND `user_id` = "{userid}";')
                database.close()

                return True

            else:
                crs.execute(f'INSERT INTO `inventory`(`quantity`, `item_id`, `user_id`) VALUES ("{quantity}", "{itemid}", "{userid}");')
                database.close()

                return True


# - TESTS 

test = Players()

# - Users
#? user_is_register - validé
#? add_user - validé
#? get_id_by_Uid - validé
#? get_progression - validé
#? set_progression - validé

# - Items
#? get_item_id - validé

# - Inventory
#? is_in_inventory - validé
#? get_quantity - validé
#? add_items - validé