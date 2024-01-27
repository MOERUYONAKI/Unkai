import mariadb
import datetime

class Webhooks():
    def __init__(self):
        self.database = 'unkai_wbk'


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

            crs.execute(f'INSERT INTO users (`username`, `discord_id`) VALUES ("{username}", "{Uid}");')
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
        
    
    # - GUILDS
        
    def guild_is_register(self, guildid : int): # Vérifie si un serveur est enregistré par son ID discord
        Gid = f'Gid{guildid}'

        database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
        crs = database.cursor()

        crs.execute(f'SELECT ID FROM guilds WHERE discord_id = "{Gid}";')
        database.close()

        return True if len(crs.fetchall()) > 0 else False
    
    def add_guild(self, guildname : str, guildid : int): # Enregistre un serveur s'il ne l'est pas déjà
        if self.guild_is_register(guildid):
            return False
        
        else:
            Gid = f'Gid{guildid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'INSERT INTO guilds (`name`, `discord_id`) VALUES ("{guildname}", "{Gid}");')
            database.close()

            return True
        

    # - WEBHOOKS
        
    def webhook_is_register(self, name : str, owner_id : int): # Vérifie si un webhook est enregistré par son nom et son propriétaire
        if not self.user_is_register(owner_id):
            return False
        
        else:
            Uid = f'Uid{owner_id}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT * FROM webhooks WHERE owner_ID = "{Uid}" and name = "{name}";')
            database.close()

            return True if len(crs.fetchall()) > 0 else False
    
    def webhook_is_register_by_id(self, WBKid): # Vérifie si un webhook est enregistré par son ID
        database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
        crs = database.cursor()

        crs.execute(f'SELECT ID FROM webhooks WHERE ID = "{WBKid}";')
        database.close()

        return True if len(crs.fetchall()) > 0 else False

    def add_webhook(self, name : str, tag : str, owner_id : int, owner_name : str, avatar_url : str = None): # Enregistre un webhook s'il ne l'est pas déjà
        if not self.user_is_register(owner_id):
            self.add_user(owner_name, owner_id)

        if self.webhook_is_register(name, owner_id):
            return False

        else:
            Uid = f'Uid{owner_id}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            if avatar_url != None:
                crs.execute(f'INSERT INTO webhooks(`name`, `avatar`, `tag`, `creation_date`, `owner_ID`) VALUES ("{name}", "{avatar_url}", "{tag}", "{datetime.date.today()}", "{Uid}");')
            
            else:
                crs.execute(f'INSERT INTO webhooks(`name`, `tag`, `creation_date`, `owner_ID`) VALUES ("{name}", "{tag}", "{datetime.date.today()}", "{Uid}");')

            database.close()

            return True
        
    def remove_webhook(self, id : int): # Supprime un webhook s'il existe dans la base
        if not self.webhook_is_register_by_id(id):
            return False

        else:
            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'DELETE FROM webhooks WHERE ID = "{id}";')
            database.close()

            return True
        
    def get_webhooks_list(self, owner_id : int):
        if not self.user_is_register(owner_id):
            return False
        
        else:
            Uid = f'Uid{owner_id}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'SELECT ID, name, tag, avatar, creation_date FROM webhooks WHERE owner_id = "{Uid}";')
            values = crs.fetchall()
            database.close()

            return values
        

    # - WEBHOOKS EDITS
     
    def edit_webhook_name(self, newname : str, name : str, owner_id : int):
        if not self.webhook_is_register(name, owner_id):
            return False

        else:
            Uid = f'Uid{owner_id}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE webhooks SET `name` = "{newname}" WHERE name = "{name}" AND owner_ID = "{Uid}";')
            database.close()

            return True
    
    def edit_webhook_tag(self, newtag : str, name : str, owner_id : int):
        if not self.webhook_is_register(name, owner_id):
            return False

        else:
            Uid = f'Uid{owner_id}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE webhooks SET `tag` = "{newtag}" WHERE name = "{name}" AND owner_ID = "{Uid}";')
            database.close()

            return True
        
    def edit_webhook_avatar(self, avatar_url : str, name : str, owner_id : int):
        if not self.webhook_is_register(name, owner_id):
            return False

        else:
            Uid = f'Uid{owner_id}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'UPDATE webhooks SET `avatar` = "{avatar_url}" WHERE name = "{name}" AND owner_ID = "{Uid}";')
            database.close()

            return True

    
    # - REGISTRATIONS
        
    def is_register(self, WBKid, guildid): # Vérifie si un webhook est créé sur un serveur par leurs ID
        Gid = f'Gid{guildid}'

        database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
        crs = database.cursor()

        crs.execute(f'SELECT ID FROM registrations WHERE Gid = "{Gid}" and Wid = "{WBKid}";')
        database.close()

        return True if len(crs.fetchall()) > 0 else False
        
    def set_registration(self, WBKid, guildid, guildname): # Ajoute un log d'enregistrement d'un webhook sur un serveur
        if self.is_register(WBKid, guildid) or not self.webhook_is_register_by_id(WBKid):
            return False
        
        else:
            if not self.guild_is_register(guildid):
                self.add_guild(guildname, guildid)

            Gid = f'Gid{guildid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'INSERT INTO registrations(`date`, `Gid`, `Wid`) VALUES ("{datetime.date.today()}", "{Gid}", "{WBKid}");')
            database.close()

            return True
        
    def unset_registration(self, WBKid, guildid): # Supprime un log d'enregistrement d'un webhook sur un serveur
        if not self.is_register(WBKid, guildid) or not self.webhook_is_register_by_id(WBKid) or not self.guild_is_register(guildid):
            return False
        
        else:
            Gid = f'Gid{guildid}'

            database = mariadb.connect(host = "localhost", port = 3307, user = "Unkai", password = "MAKAI!host", database = self.database)
            crs = database.cursor()

            crs.execute(f'DELETE FROM registrations WHERE Gid = "{Gid}" AND Wid = "{WBKid}";')
            database.close()

            return True


# - TESTS 

test = Webhooks()

# - Users
#? user_is_register - validé
#? add_user - validé
#? get_id_by_Uid - validé

# - Guilds
#? guild_is_register - validé
#? add_guild - validé

# - Webhooks
#? webhook_is_register - validé
#? webhook_is_register_by_id - validé
#? add_webhook - validé 
#? remove_webhook - validé 
#? get_webhooks_list - validé

# Webhooks edits
#? edit_webhook_name - validé
#? edit_webhook_tag - validé
#? edit_webhook_avatar - validé

# - Registrations 
#? is_register - validé
#? set_registration - validé 
#? unset_registration - validé 