CREATE TABLE IF NOT EXISTS `guilds` (
  `ID` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `discord_id` varchar(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `users` (
  `ID` integer PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `discord_id` varchar(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `webhooks` (
  `ID` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `tag` varchar(255) NOT NULL,
  `creation_date` date NOT NULL,
  `owner_ID` varchar(255) NOT NULL,
  `avatar` varchar(255)
);

CREATE TABLE IF NOT EXISTS `registrations` (
  `ID` integer PRIMARY KEY AUTO_INCREMENT,
  `date` date NOT NULL,
  `Gid` varchar(255) NOT NULL,
  `Wid` integer NOT NULL
);

ALTER TABLE `webhooks` ADD FOREIGN KEY (`owner_ID`) REFERENCES `users` (`discord_id`);
ALTER TABLE `registrations` ADD FOREIGN KEY (`Gid`) REFERENCES `guilds` (`discord_id`);
ALTER TABLE `registrations` ADD FOREIGN KEY (`Wid`) REFERENCES `webhooks` (`ID`);