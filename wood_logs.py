import pygame
from config import LOG_SIZES

# ======================== PARTIE 3.1 ===========================
# 
# TODO : Définir un dictionnaire pour les bûches en bois avec trois tailles différentes : petite, moyenne et longue
# 
# Étapes à suivre : 
# - Créer un dictionnaire nommé `logs_dict` avec les trois clés suivantes : 
#      - short
#      - medium
#      - long 
#
# - Utilisez "pygame.image.load()" pour charger l'image "log.png" (à partir du dossier "images/")
#   trois fois, c'est-à-dire une fois pour chaque taille.
# - Redimensionnez (avec "pygame.transform.scale") chaque image en utilisant les clés du dictionnaire LOG_SIZES. 

logs_dict = { 
    'short' :'' ,
    'medium' :'' ,
    'long' : '',
}
buche_courte = pygame.image.load('images/log.png')
buche_moyenne = pygame.image.load('images/log.png')
buche_longue = pygame.image.load('images/log.png')

logs_dict['short'] = pygame.transform.scale(buche_courte, (LOG_SIZES['short'][0], LOG_SIZES['short'][1]))
logs_dict['medium'] = pygame.transform.scale(buche_moyenne, (LOG_SIZES['medium'][0], LOG_SIZES['medium'][1]))
logs_dict['long'] = pygame.transform.scale(buche_longue, (LOG_SIZES['long'][0], LOG_SIZES['long'][1]))
# ===============================================================