import mariadb

class Players():
    def __init__(self):
        self.database = 'XXX'


    # - USERS

    def user_is_register(self, userid : int): # Vérifie si un utilisateur est enregistré par son ID discord
        Uid = f'Uid{userid}'

        database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
        crs = database.cursor()

        crs.execute(f'SELECT ID FROM users WHERE discord_id = "{Uid}";')
        database.close()

        return True if len(crs.fetchall()) > 0 else False
    
    def add_user(self, username : str, userid : int): # Enregistre un utilisateur s'il ne l'est pas déjà
        if self.user_is_register(userid):
            return False
        
        else:
            Uid = f'Uid{userid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'INSERT INTO users (`username`, `chapter_id`, `page_id`, `discord_id`) VALUES ("{username}", 1, 0, "{Uid}");')
            database.close()

            return True
        
    def get_id_by_Uid(self, userid : int):
        if not self.user_is_register(userid):
            return False
        
        else:
            Uid = f'Uid{userid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
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

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT chapter_id, page_id FROM users WHERE discord_id = "{Uid}";')
            DBid = crs.fetchall()
            database.close()

            return DBid[0]
        
    def set_progression(self, userid : int, new_progression : tuple): # Modifie le chapitre et la page où le joueur s'est arrêté
        if not self.user_is_register(userid) or not type(new_progression) != 'tuple':
            return False
        
        else:
            Uid = f'Uid{userid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE `users` SET `chapter_id` = "{new_progression[0]}", `page_id` = "{new_progression[1]}" WHERE discord_id = "{Uid}";')
            database.close()

            return True


    # - ITEMS

    def get_item_id(self, item_name : str): # Renvoie l'ID de l'item s'il existe
        database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
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
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
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
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
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
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            if self.is_in_inventory(Uid, item_name):
                crs.execute(f'UPDATE `inventory` SET `quantity` = "{actual_quantity + quantity}" WHERE `item_id` = "{itemid}" AND `user_id` = "{userid}";')
                database.close()

                return True

            else:
                crs.execute(f'INSERT INTO `inventory`(`quantity`, `item_id`, `user_id`) VALUES ("{quantity}", "{itemid}", "{userid}");')
                database.close()

                return True


    # - CHARACTERS
            
    def make_character(self, Uid : int):
        userid = self.get_id_by_Uid(Uid)

        if userid == False:
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'INSERT INTO `characters`(`user_id`) VALUES ("{userid}");')
            database.close()

            return True
        
    def char_is_register(self, Uid : int):
        userid = self.get_id_by_Uid(Uid)

        if userid == False:
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT ID FROM characters WHERE user_id = "{userid}";')
            database.close()

            return True if len(crs.fetchall()) > 0 else False
        
    def get_stats(self, Uid : int):
        userid = self.get_id_by_Uid(Uid)

        if userid == False:
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT hp, mp, atk, dfs FROM characters WHERE user_id = "{userid}";')
            DBid = crs.fetchall()
            database.close()

            return DBid[0]
        
    def set_stats(self, Uid : int, new_stats : tuple):
        userid = self.get_id_by_Uid(Uid)

        if userid == False or not self.char_is_register(Uid):
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE characters SET hp = "{new_stats[0]}", mp = "{new_stats[1]}", atk = "{new_stats[2]}", dfs = "{new_stats[3]}" WHERE user_id = "{userid}";')
            database.close()

            return True

    def get_equipement(self, Uid : int):
        userid = self.get_id_by_Uid(Uid)

        if userid == False:
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT ArmPpl_id, ArmSnd_id, ArrPpl_id, ArrBrs_id, ArrHd_id, ArrJmb_id FROM characters WHERE user_id = "{userid}";')
            DBid = crs.fetchall()
            database.close()

            return DBid[0]
        
    def set_ArmPpl(self, Uid : int, item_name : str):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)

        if userid == False or itemid == False or not self.is_in_inventory(Uid, item_name) or not self.char_is_register(Uid):
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE characters SET ArmPpl_id = "{itemid}" WHERE user_id = "{userid}";')
            database.close()

            return True
        
    def set_ArmSnd(self, Uid : int, item_name : str):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)

        if userid == False or itemid == False or not self.is_in_inventory(Uid, item_name) or not self.char_is_register(Uid):
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE characters SET ArmSnd_id = "{itemid}" WHERE user_id = "{userid}";')
            database.close()

            return True
        
    def set_ArrPpl(self, Uid : int, item_name : str):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)

        if userid == False or itemid == False or not self.is_in_inventory(Uid, item_name) or not self.char_is_register(Uid):
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE characters SET ArrPpl_id = "{itemid}" WHERE user_id = "{userid}";')
            database.close()

            return True
        
    def set_ArrBrs(self, Uid : int, item_name : str):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)

        if userid == False or itemid == False or not self.is_in_inventory(Uid, item_name) or not self.char_is_register(Uid):
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE characters SET ArrBrs_id = "{itemid}" WHERE user_id = "{userid}";')
            database.close()

            return True
        
    def set_ArrHd(self, Uid : int, item_name : str):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)

        if userid == False or itemid == False or not self.is_in_inventory(Uid, item_name) or not self.char_is_register(Uid):
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE characters SET ArrHd_id = "{itemid}" WHERE user_id = "{userid}";')
            database.close()

            return True
        
    def set_ArrJmb(self, Uid : int, item_name : str):
        userid = self.get_id_by_Uid(Uid)
        itemid = self.get_item_id(item_name)

        if userid == False or itemid == False or not self.is_in_inventory(Uid, item_name) or not self.char_is_register(Uid):
            return False
        
        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "XXX", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE characters SET ArrJmb_id = "{itemid}" WHERE user_id = "{userid}";')
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

# - Characters
#? make_character - validé
#? char_is_register - validé
#? get_stats - validé
#? set_stats - validé
#? get_equipement - validé
#? set_equipement(ArmPpl_id, ArmSnd_id, ArrPpl_id, ArrBrs_id, ArrHd_id, ArrJmb_id) - validé