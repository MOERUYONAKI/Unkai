CREATE TABLE users (
    ID int PRIMARY KEY AUTO_INCREMENT,
    username varchar(255),
    chapter_id int,
    page_id int,
    discord_id varchar(255) -- ID discord du joueur - Uid{discord_id}
);

CREATE TABLE items (
    ID int PRIMARY KEY,
    itemname VARCHAR(255)
);

CREATE TABLE inventory (
    ID int PRIMARY KEY AUTO_INCREMENT,
    quantity int,
    item_id int,
    user_id int,

    FOREIGN KEY (item_id) REFERENCES items(ID),
    FOREIGN KEY (user_id) REFERENCES users(ID)
);

INSERT INTO items (ID, itemname) VALUES
    -- armes - 1
    (100, 'dague rouillée'),
    (101, 'dague en argent'),
    (102, 'grand coutelas'),
    (103, 'petite épée'),

    -- équipement - 2
    (200, 'casque abimé'),
    (201, 'côte de mailles'),
    (202, 'gantelet usagé'),
    (203, 'vieilles jambières'),
    (204, 'vieux heaume'),

    -- consommables - 3
    (300, 'potion de force'),
    (301, 'potion de mana'),
    (302, 'potion de soin'),
    (303, 'potion de soin avancée'),
    (304, 'viande sèche'),

    -- objets - 4
    (400, 'or'),
    (401, 'osselet'),
    (402, 'peau'),
    (403, 'vieille rune');