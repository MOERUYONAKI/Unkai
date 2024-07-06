# Unkai

[ Project Unkai V2 ]

## Présentation

**Unkai** est un bot Discord créé pour répondre à des besoins sur mesure. Il offre des fonctionnalités variées allant de la modération à l'amélioration de l'expérience de jeu de rôle (RP).

## Fonctionnalités

Unkai propose une gamme de fonctionnalités pour améliorer la gestion de votre serveur et enrichir vos sessions de jeu de rôle, dont :

### Modération
- **Kick/Ban** : Expulsion des membres indésirables
- **Clear** : Suppression des messages récents

### Jeu de rôle (RP)
- **Météo** : Génère des conditions météorologiques aléatoires pour enrichir vos scénarios RP
- **Narration et Webhooks** : Outils pour faciliter la narration et l'immersion

## Prérequis

Avant d'installer et de configurer Unkai, assurez-vous d'avoir les éléments suivants :

- Python 3.10 ou supérieur
- Un compte Discord et un serveur où vous avez des droits admins
- Un token pour votre bot (à obtenir via le [Discord Developer Portal](https://discord.com/developers/applications))

## Installation

Suivez ces étapes pour installer Unkai sur votre serveur :

1. Clonez ce dépôt GitHub :
```
git clone https://github.com/MOERUYONAKI/Unkai.git
```

2. Accédez au répertoire du projet :
```
cd Unkai
```

3. Installez les dépendances :
```
pip install -r requirements.txt
```

Il est aussi possible de selectionner une certaine version grâce aux tags et au [guide des mises à jour](https://github.com/MOERUYONAKI/Unkai/tree/main/UNKAI_docs/updates.md)

> [!WARNING]
> Certaines version ne contiennent pas les requirements et le fichier de configuration et devront donc être éditée manuellement.

## Configuration

Assurez-vous que votre fichier de configuration contient toutes les informations nécessaires pour le bon fonctionnement du bot. Pour cela, il vous suffit de compléter le fichier `conf.json` ainsi : 

```
{
  "TOKEN": "Votre token",
  "PREFIX" : "Au choix, '!' par défaut"
}
```

## Utilisation

Une fois le bot lancé, vous pouvez utiliser la commande `/help` pour obtenir la liste complète des commandes disponibles. Toutes les commandes sont également accessibles via des commandes slash.

### Exemples de commandes

- `/help` : Affiche la liste des commandes et leur description
- `/ban @utilisateur` : Bannit l'utilisateur mentionné
- `/clear 5` : Supprime les 5 derniers messages du salon

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](https://github.com/MOERUYONAKI/Unkai/blob/main/LICENSE) pour plus de détails

## Auteurs et remerciements

1. Créateur
- **[MOERUYONAKI](https://github.com/MOERUYONAKI)**

2. Testeurs principaux
- **[Xanark](https://github.com/Xanark)**
- **[Rusano](https://github.com/sleddge)**

3. Autres remerciements
- **Natsu** pour le soutien et aussi pas mal de tests
- **[Chatgpt](https://chat.openai.com)** pour ce readme principalement

## Support

Pour obtenir de l'aide ou poser des questions, rejoignez notre serveur Discord via ce [lien](https://discord.gg/kZk2SUQFy7)
