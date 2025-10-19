import pygame
import random
from config import LANES, SCREEN_WIDTH, SCREEN_HEIGHT, LANE_HEIGHT, CARS_SIZE, LOG_SIZES
from frog import frog_dict, frog_img
from cars import cars_dict
from wood_logs import logs_dict
import sys

# Paramètres de l'écran
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("frogger")

# Charger l'image de l'arrière-plan
background_img = pygame.image.load("images/background.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


# ======================== PARTIE 2.2 ========================
#
# TODO : Complétez la fonction `add_road_lanes()`, qui permettra d'ajouter 4 voies de route avec des voitures aléatoires. 
# 
# Contraintes à respecter : 
# - Les voies paires (i=0,2) doivent contenir des voitures qui vont vers la droite
# - Les voies impaires (i=1,3) doivent contenir des voitures qui vont vers la gauche
# - Les voitures doivent être centrée en y à l'intérieur de la voie. 
# - On veut avoir 3 voitures par voie, de position de départ aléatoire. 
# - Ajoutez un espacement (ex: 250 pixels) pour éviter que les voitures ne se chevauchent. 
# - La vitesse des voitures doit être aléatoire, entre 2, 3 ou 4, et le signe (+ ou -)
#   doit être appliqué selon la direction de la voie. 

# - Ajoutez la voie complète à la structure qui gère l’ensemble des voies (lanes).

def add_road_lanes():
    position_base = int(SCREEN_HEIGHT) - int(LANE_HEIGHT)

    for i in range(4):
        position = position_base - (i) * int(LANE_HEIGHT)
        direction = 'droite' if i % 2 == 0 else 'gauche'

        import random

        vitesse = 0
        if direction == 'droite' :
            vitesse = (random.choice([1,1.5,2]))
        else : vitesse = -(random.choice([1,1.5,2]))

        cars = []
        for j in range(3):
            car = {
                'width' :  CARS_SIZE,
                'height': CARS_SIZE,
                'x': j * 250 + int(random.randint(300,400)),
                'y': position - 1.2 * int(CARS_SIZE[1]) ,
                'image': ''
            }
            if i % 2 == 0 : 
                car['image'] = random.choice(cars_dict['right'])
            else : car['image'] = random.choice(cars_dict['left'])

            cars.append(car)

            LANES.append({
            "type": 'road',
            "speed": vitesse,
            "y": position,
            "entities": cars
            })

    return


# ===============================================================

# Ajouter 1 voie de pelouse (entre la route et la rivière)
def add_grass_lane():
    grass_y = SCREEN_HEIGHT - (6 * LANE_HEIGHT)
    LANES.append({"type": "grass", "speed": 0, "y": grass_y, "entities": []})

# ======================== PARTIE 3.2 ===========================
# 
# TODO : Complétez la fonction `add_river_lanes()`, qui permettra d'ajouter les bûches de bois dans la rivière de position et de vitesse aléatoire. 
# 
# Étapes à suivre : 
#
# - Créer une boucle pour ajouter 4 voies de rivière
# 
# - Pour chaque voie :
#     - Calculez la position verticale (y) à partir du bas de l’écran, en tenant compte de l’index de la voie.
#     - Attribuez une vitesse aléatoire pour la voie, parmi [2, 3, 4].
#     - La direction dépend de si l’indice est pair (vers la droite) ou impair (vers la gauche).
# 
# - Dans chaque voie :
#     - Ajoutez 3 bûches.
#       - Pour chaque bûche :
#           - Choisissez une taille aléatoire parmi les options disponibles.
#           - Récupérez la longueur de la bûche à partir du dictionnaire de tailles.
#           - La position en x doit être aléatoire. Ajoutez un espacement (ex: 250) pour ne pas que les bûches ne se chevauchent sur la voie. 
#           - Calculez la position verticale de la bûche pour qu’elle soit centrée dans sa voie, en fonction de la longueur de la bûche et celle de la voie.
# 
# - Ajoutez la voie complète à la structure qui gère l’ensemble des voies (lanes). 

def add_river_lanes():
    position_base = int(SCREEN_HEIGHT) - 7*int(LANE_HEIGHT)

    for i in range(4):
        position = position_base - i*int(LANE_HEIGHT)
        direction = 'droite' if i % 2 == 0 else 'gauche'

        import random

        vitesse = 0
        if direction == 'droite' :
            vitesse = (random.choice([1,1.5,2]))
        else : vitesse = -(random.choice([1,1.5,2]))

        logs = []
        for j in range(3):
            log = {
                'width' :  random.choice([LOG_SIZES['short'][0], LOG_SIZES['medium'][0], LOG_SIZES['long'][0]]),
                'height': LOG_SIZES['short'][1],
                'x': j * 250 + int(random.randint(300,400)),
                'y': position + (4/7)*int(LOG_SIZES['short'][1]) ,
                'image': ''
            }
            if log['width'] == LOG_SIZES['short'][0] : 
                log['image'] = logs_dict['short']
            if log['width'] == LOG_SIZES['medium'][0] : 
                log['image'] = logs_dict['medium']
            if log['width'] == LOG_SIZES['long'][0] : 
                log['image'] = logs_dict['long']
            

            logs.append(log)

            LANES.append({
            "type": 'river',
            "speed": int(vitesse),
            "y": position,
            "entities": logs
            })

    




    return

# ===============================================================

# Ajouter une voie de pelouse après la rivière
def add_final_grass_lane():
    final_grass_y = SCREEN_HEIGHT - (11 * LANE_HEIGHT)  # du bas vers le haut 
    LANES.append({"type": "grass_win", "speed": 0, "y": final_grass_y, "entities": []})

# Affichage de la fenêtre du jeu (en y ajoutant les voies avec les voitures et bûches de bois, la grenouille et l'affichage des vies)
def draw_window():
    # Affichage de l'image "background.img", à la position (0,0)
    GAME_WINDOW.blit(background_img, (0, 0)) # "blit" est une méthode intégrée dans pygame, qui permet d'afficher une image sur la fenêtre du jeu
    
    # Affichage des entités (voitures, bûches, etc.) à leurs positions définies dans la liste "lanes"
    for lane in LANES:
        for ent in lane["entities"]:
            GAME_WINDOW.blit(ent["image"], (ent["x"], ent["y"]))

    # Affichage de l'image de la grenouille sur la fenêtre du jeu (à sa position définie dans le dictionnaire "frog_dict_dict")
    GAME_WINDOW.blit(frog_img, (frog_dict["x"], frog_dict["y"]))

    # Affichage du nombre de vies
    font = pygame.font.SysFont(None, 36)
    lives_text = font.render(f"Lives: {frog_dict['lives']}", True, (255, 255, 255))
    GAME_WINDOW.blit(lives_text, (10, 10))

    pygame.display.update()

# Fonction qui gère le message à afficher lorsqu'on a gagné
def show_win_message():
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    GAME_WINDOW.blit(overlay, (0, 0))

    font = pygame.font.SysFont(None, 72)
    text = font.render("You Win!", True, (255, 255, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
    GAME_WINDOW.blit(text, text_rect)

    pygame.display.update()
    
# Fonction qui gère le message à afficher lorsqu'on a perdu
def show_game_over_message():
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    GAME_WINDOW.blit(overlay, (0, 0))

    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    GAME_WINDOW.blit(text, text_rect)

    pygame.display.update()
