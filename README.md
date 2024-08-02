# Projet : Feux Tricolores Améliorés avec Barrière de Servomoteur au Feu Rouge
Bienvenue dans le dépôt "Feux Tricolores Améliorés avec Barrière de Servomoteur au Feu Rouge" ! Ce projet propose un système de feux tricolores intégrant une barrière automatique contrôlée par un servomoteur qui s'abaisse lorsque le feu est rouge, améliorant ainsi la sécurité routière.

# Table des Matières
Introduction
Matériel Requis
Configuration de l'Environnement
Installation et Utilisation
Code Source
Contribuer
Licence
Contact
# Introduction
Ce projet vise à développer un système de feux tricolores amélioré avec une barrière contrôlée par un servomoteur. La barrière se ferme lorsque le feu passe au rouge et se lève lorsque le feu passe au vert, assurant une meilleure gestion du trafic et augmentant la sécurité des passages piétons.

# Matériel Requis
ESP32
LEDs (Rouge, Jaune, Verte)
Servomoteur
Résistances
Câbles et connecteurs
Plaque d'essai (Breadboard)
Alimentation (batterie ou adaptateur secteur)
# Configuration de l'Environnement
Installer MicroPython sur l'ESP32 :

Télécharger l'image MicroPython depuis MicroPython.org.
Flasher l'image sur l'ESP32 en utilisant esptool.py ou un autre outil.
Configurer l'IDE :

Utiliser Thonny IDE, uPyCraft, ou tout autre IDE compatible avec MicroPython.
# Installation et Utilisation
Cloner le dépôt :

bash
Copier le code
git clone https://github.com/votre-utilisateur/feux-tricolores-barriere.git
cd feux-tricolores-barriere
Téléverser le code sur l'ESP32 :

Connecter l'ESP32 à votre ordinateur.
Ouvrir l'IDE et charger les scripts depuis le répertoire cloné.
Téléverser les scripts sur l'ESP32.
Code Source
Code pour les Feux Tricolores et Barrière de Servomoteur :

python
Copier le code
from machine import Pin, PWM
from time import sleep

# Initialisation des LEDs
led_rouge = Pin(2, Pin.OUT)
led_jaune = Pin(4, Pin.OUT)
led_verte = Pin(5, Pin.OUT)

# Initialisation du Servomoteur
servo = PWM(Pin(15), freq=50)

def set_servo_angle(angle):
    duty = int((angle / 180) * 1023)
    servo.duty(duty)

while True:
    # Feu Vert
    led_verte.value(1)
    led_jaune.value(0)
    led_rouge.value(0)
    set_servo_angle(0)  # Lever la barrière
    sleep(5)
    
    # Feu Jaune
    led_verte.value(0)
    led_jaune.value(1)
    sleep(2)
    
    # Feu Rouge
    led_jaune.value(0)
    led_rouge.value(1)
    set_servo_angle(90)  # Abaisser la barrière
    sleep(5)
# Contribuer
Les contributions sont les bienvenues ! Merci de suivre les étapes ci-dessous pour contribuer :

Forker le dépôt
Créer une branche de fonctionnalité (git checkout -b fonctionnalite/ma-nouvelle-fonctionnalite)
Commiter les modifications (git commit -am 'Ajoute une nouvelle fonctionnalité')
Pousser vers la branche (git push origin fonctionnalite/ma-nouvelle-fonctionnalite)
Créer une Pull Request
# Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

# Contact
Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur le dépôt GitHub.
