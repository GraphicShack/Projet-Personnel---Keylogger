import psutil

def detecteur_de_keylogger():
    # Liste des processus avec nom suspect qui pourrait être un keylogger
    processus_suspicieux = [
        'keylogger',
        'logkeys',
        'xinput',
        'pynput',
        'keyboard',
        'hook',
        'logger'
    ]

    # Iterer sur les processus courants
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # verifier si les noms de processus match les noms suspects
            nom_process = proc.info['name']

            if nom_process is not None:
                nom_process = nom_process.lower()

                if any(susp_name in nom_process for susp_name in processus_suspicieux):
                    print(f"[!] Processus suspicieux détecté : {nom_process} (PID : {proc.info['pid']})")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == '__main__':
    print("[+] Scan des possibles keyloggers...")
    detecteur_de_keylogger()
    print("[+] Scan accompli avec succès !")