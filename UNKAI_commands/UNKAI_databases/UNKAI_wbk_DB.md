# - UNKAI WEBHOOKS -

## USERS -

**ID** - Integer *(PRIMARY KEY)*  

**username** - Varchar - discord username  

**Uid** - Varchar - "Uid[discord id]"  
  
**user_is_register** - [Uid]  
**add_user** - [username][Uid]  

## GUILDS -

**guild_is_register** - [Gid]  
**add_guild** - [guildname][Gid]  

## WEBHOOKS -

**webhook_is_register** - [wbkname][Uid]  
**webhook_is_register_by_id** - [Wid]  
**add_webhook** - [wbkname][tag][Uid][username] [avatar_url]  

**remove_webhook** - [Wid]  

## REGISTRATIONS -

**is_register** - [Wid][Gid]  
**set_registration** - [Wid][Gid]  
**unset_registration** - [Wid][Gid]  