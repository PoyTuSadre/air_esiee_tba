Air_ESIEE_TBA 🚀

Projet final pour le module de Python – ESIEE Paris (2025)

Par Messad Houcine & Thomas Quéro

🧭 Description du projet

Air ESIEE – Copilote A320 est un jeu d’aventure textuel éducatif en Python, où vous incarnez un copilote stagiaire à bord d’un Airbus A320 de la compagnie Air ESIEE.

Lors d’un vol d’entraînement entre Paris et Nice, diverses pannes techniques, urgences ECAM, et situations humaines complexes surviennent.

Le joueur doit :

Diagnostiquer les anomalies via le système ECAM (Electronic Centralized Aircraft Monitor).

Suivre les procédures QRH (Quick Reference Handbook).

Interagir efficacement avec le commandant et les passagers.

Prendre des décisions rapides mais réfléchies.

Le jeu combine apprentissage technique, simulation de vol et réflexion éthique.

🎯 Objectif du joueur

Le but est de ramener l’avion en sécurité tout en maintenant un bon score de performance.
Chaque action impacte la sécurité, le stress de l’équipage, et le score final.

🧮 Système de points

L’évaluation repose sur trois axes : technique, communication, et gestion.

🛠️ Actions techniques
Situation	Décision	Points
Analyser instruments après urgence	Bonne analyse	+1
Résoudre partiellement un problème	Avancée partielle	+3
Résolution complète	Excellente maîtrise	+7
Résolution avec légère perte	Bonne réaction	+4
Résolution avec pertes majeures	Sauvetage minimal	+1
Ignorer alarme ECAM	Mauvaise gestion	-3
Erreur de checklist	Critique	-5
🧑‍✈️ Gestion humaine
Situation	Décision	Points
Interaction positive avec commandant	Bonne communication	+2
Interaction positive passagers / ATC	Empathie	+2
Rassurer un PNJ	Leadership	+3
Comportement froid ou agressif	Manque de communication	-2
Garder son calme	Professionnalisme	+4
Perdre son sang-froid	Stress mal géré	-3
⚙️ Gestion et anticipation
Situation	Décision	Points
Vérifie systèmes avant action	Anticipation	+2
Utilise le bon outil au bon moment	Bon jugement	+3
Oublie un élément essentiel	Inattention	-2
Priorise urgences correctement	Excellente hiérarchisation	+4
🏁 Fin de mission
Résultat	Points
Vol terminé sans incident	+10
Vol terminé avec déroutement maîtrisé	+5
Vol terminé avec pertes majeures	+2
Crash ou erreur fatale	-10
Quitte avant fin du vol	-5
💯 Évaluation finale
Score	Évaluation	Mention
90–100	Pilote d’exception	🥇 Or
75–89	Copilote confirmé	🥈 Argent
50–74	Copilote stagiaire	🥉 Bronze
0–49	Non qualifié	❌ Échec
🧩 Conditions de victoire / défaite

Victoire : Vol terminé sans incident majeur.

Défaite : Erreur critique ou crash.

Mode apprentissage : Chaque erreur est commentée pour progresser.

💻 Installation
Prérequis

Python 3.10+

Tkinter (inclus par défaut)

OS : Windows, macOS, Linux

Étapes
git clone http://github.com/PoyTuSadre/air_esiee_tba
cd air_esiee_tba

Lancer le jeu

Mode terminal :

python AirEsiee.py


Mode graphique :

python AirEsiee.py --gui


Si Tkinter n’est pas disponible, le jeu bascule automatiquement en mode texte.

🕹️ Commandes principales
Commande	Description
look	Observer l’environnement
go <direction>	Se déplacer
take <objet>	Prendre un objet
drop <objet>	Poser un objet
inventory	Voir l’inventaire
talk <pnj>	Parler à un personnage
ecam	Consulter les messages ECAM
use <objet>	Utiliser un équipement
history	Voir actions passées
undo	Revenir en arrière
help	Liste des commandes
quit	Quitter le jeu

Exemple

> look
Vous êtes dans le cockpit. L’ECAM affiche une alarme moteur gauche.

> ecam
[ECAM ALERT] ENGINE 1 FIRE
Procédure : IDLE – ENG MASTER OFF – FIRE PB – AGENT 1 DISP.

> take QRH
Vous prenez le QRH et suivez la checklist d’urgence.

> talk captain
Commandant : "Feu moteur maîtrisé ! Excellent réflexe, copilote."

⏱️ Chrono et événements

Le vol est simulé sur 30 minutes, avec événements forcés dans certaines zones :

Lieux

Cockpit :

Siège

Panneau central : ECAM, FCU, MCDU

Panneau haut / bas

Altimètre

Radar

Cabine :

Crew

Business

Economy

Back crew

Événements forcés
Minute	Lieu	Événement
10	Cockpit	Urgence ECAM
15	Cabine/Economy	Problème passager
29	Cockpit	Descente finale

Le joueur est déplacé automatiquement vers la zone concernée lors de chaque événement.

def update_chrono():
    global chrono
    chrono += 1

🧩 Diagramme de classes
classDiagram
    Game --> Player
    Game --> Room
    Game --> Actions
    Room --> Item
    Room --> Character
    Player --> Item
    Player --> Command
    Character --> Command
    Game --> Win

🎨 Perspectives de développement

Interface graphique avec jauges ECAM, sons cockpit et thème Air ESIEE

PNJ avec comportements et émotions

Pannes dynamiques aléatoires

Mode multijoueur coopératif

Analyse détaillée des sessions et score pédagogique

📝 Auteurs

Messad Houcine
Thomas Quéro