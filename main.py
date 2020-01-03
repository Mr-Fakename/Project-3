# Il n'y a qu'un seul niveau. La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.
# MacGyver sera contrôlé par les touches directionnelles du clavier.
# Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.
# La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.
# MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !
# Il récupèrera un objet simplement en se déplaçant dessus.
# Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe.
# S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).
# Le programme sera standalone, c'est-à-dire qu'il pourra être exécuté sur n'importe quel ordinateur.

# from .Map import Map as ***


#
#
# def winning_conditions():
#     if item_index == 3:
#         print("Yay you win")
#         exit game
#     else:
#         print("You die")
#         exit game
#     pass

import pygame

pygame.init()

size = width, height = 800, 800
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
