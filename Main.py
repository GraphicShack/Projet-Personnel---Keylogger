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

#--------------------------------------------------------------------------------
# pynput

#--------------------------------------------------------------------------------
