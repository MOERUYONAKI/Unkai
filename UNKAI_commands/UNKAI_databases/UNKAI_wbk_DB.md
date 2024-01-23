# - UNKAI WEBHOOKS -

## USERS -

user_is_register - [Uid]  
add_user - [username][Uid]  

## GUILDS -

guild_is_register - [Gid]  
add_guild - [guildname][Gid]  

## WEBHOOKS -

webhook_is_register - [wbkname][Uid]  
webhook_is_register_by_id - [Wid]  
add_webhook - [wbkname][tag][Uid][username] [avatar_url]  
remove_webhook - [Wid]  

## REGISTRATIONS -

is_register - [Wid][Gid]  
set_registration - [Wid][Gid]  
unset_registration - [Wid][Gid]  

```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```