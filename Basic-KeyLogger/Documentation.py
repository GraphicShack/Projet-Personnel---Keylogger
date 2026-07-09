#--------------------------------------------------------------------------------
# But du projet :
#----------------
# Enregistrer les frappes du clavier dans un fichier texte
# Apprendre la gestion des fichiers en Python - Comment lire, écrire et "append" a un fichier texte
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#lecture et écriture d'un fichier en python
# open('nomduficher', 'MODE') ou MODE peut être :
# 'r' : lecture seule (read)
# 'w' : écriture seule (write) - écrase le fichier s'il existe
# 'a' : écriture seule (append) - ajoute à la fin du fichier si le fichier existe
# 'r+' : lecture et écriture (read and write)
#---------------- Exemple ----------------
#f = open('Log.txt', 'w')
#f.write("Je suis full cool")
#f.close()
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Listener (Écoute les frappes du clavier)
# Utilisation de "with" keyword pour relacher automatiquement les ressources après utilisation
#---------------- Exemple ----------------
#with open('Log.txt', 'a') as f:
#    f.write("\nJe suis full cool")
#--------------------------------------------------------------------------------

#                                  *Packages*

#--------------------------------------------------------------------------------
#Pynput
#---------------- Controller la souris  ----------------

#       from pynput.mouse import Controller
#       def controlSouris():
#           souris = Controller()
#           souris.position = (1000,1000) // (Horizontal, Vertical) Depuis haut gauche de l'écran
#       controlSouris()

#---------------- Trouver la position de la souris ----------------

#       from pynput.mouse import Listener
#
#       def ecrireAuFichier(x,y):
#           print('position de la souris [0]'.format((x,y)))

#       with Listener(on_move=ecrireAuFichier) as L:
#       L.join()
#
#

#---------------- Controller le clavier ----------------

#       from pynput.keyboard import Controller
#       def controlClavier():
#           clavier = Controller()
#           clavier.type("Test")
#       controlClavier()

#---------------- Écouter le clavier ----------------

#       from pynput.keyboard import Listener

#       def ecrireAuFichier(touche):
#           Touche = str(touche)
#           with open("log.txt", "a") as fichier:
#               fichier.write(Touche)

#       with Listener(on_press=ecrireAuFichier) as L:
#           L.join()
#--------------------------------------------------------------------------------


