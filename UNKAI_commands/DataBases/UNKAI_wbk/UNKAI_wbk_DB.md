# - UNKAI WEBHOOKS -

L'utilisation des **Webhooks** nécessite d'avoir une base MariaDB dans localhost (en important le fichier "**UNKAI_wbk_DB.sql**")...

## USERS -

**ID** - *integer*  
**username** - *varchar* - discord username  
**Uid** - *varchar* - "Uid[discord id]"  
  
**user_is_register** - [Uid]  
**add_user** - [username][Uid]  
**get_id_by_Uid** - [Uid]  

## GUILDS -

**ID** - *integer*  
**guildname** - *varchar* - discord guildname  
**Gid** - *varchar* - "Gid[discord id]"  
  
**guild_is_register** - [Gid]  
**add_guild** - [guildname][Gid]  

## WEBHOOKS -

**ID** - *integer*  
**name** - *varchar* - webhook name  
**tag** - *varchar* - webhook tag  
**date** - *date* - creation date  
**Uid** - *varchar* - "Uid[discord id]"  
**avatar** - *varchar* - image url  
  
**webhook_is_register** - [wbkname][Uid]  
**webhook_is_register_by_id** - [Wid]  
**add_webhook** - [wbkname][tag][Uid][username] [avatar]  
**remove_webhook** - [Wid]  
  
**edit_webhook_name** - [newname][wbkname][Uid]  
**edit_webhook_tag** - [newtag][wbkname][Uid]  
**edit_webhook_avatar** - [avatar][wbkname][Uid]  

## REGISTRATIONS -

**ID** - *integer*  
**date** - *date* - registration date  
**Gid** - *varchar* - "Gid[discord id]"  
**Wid** - *integer* - webhook id  
  
**is_register** - [Wid][Gid]  
**set_registration** - [Wid][Gid]  
**unset_registration** - [Wid][Gid]  
