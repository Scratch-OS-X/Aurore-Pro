import datetime as dt
import json
import math
import urllib.request

VERSION_ACTUELLE = "1.6"
REPO_GITHUB = "Scratch-OS-X/Aurore-Pro"


def maj():
    url = f"https://api.github.com/repos/{REPO_GITHUB}/releases/latest"
    headers = {"User-Agent": "Aurore-Pro-App"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=3) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                derniere_version = data["tag_name"].lstrip("v")

                if derniere_version != VERSION_ACTUELLE:
                    print(
                        f"\033[93m⚠️  [MISE À JOUR] Une nouvelle version ({derniere_version}) est disponible !"
                    )
                    print(
                        f"Tapez 'git pull origin main' dans ton terminal pour la récupérer.\033[0m\n"
                    )
                else:
                    return True
    except Exception:
        pass
    return False


maj()

print(f"\nAurore Pro Py [BÊTA]")
print("Tape 'help' pour une liste des commandes.")

while True:
    aurore = input("\n>>> ").strip()
    print("\n")

    if aurore == "help":
        print("Tape 'quit' pour quitter")
        print("Tape 'time' pour obtenir la date et l'heure actuelle")
        print("Tape 'version' (ou 'v') pour obtenir le numéro de version")
        print("Tape 'update' (ou 'maj') pour vérifier les mises à jour")
        print(
            "Tape '+' pour une addition, '-' pour une soustraction, '*' (ou 'x') pour une multiplication ou '/' (ou ':' ou '÷') pour une division"
        )

    elif aurore == "quit":
        break

    elif aurore in ["version", "v"]:
        print(f"Aurore Pro Py [v. {VERSION_ACTUELLE} // BÊTA]")

    elif aurore in ["update", "maj"]:
        print("Vérification des mises à jour...")
        est_a_jour = maj()
        if est_a_jour:
            print("\033[92mVous utilisez déjà la dernière version !\033[0m")

    elif aurore == "time":
        now = dt.datetime.now()
        print(
            f"Nous sommes le {now.strftime('%d/%m/%Y')} et il est {now.strftime('%H:%M:%S')}"
        )

    elif aurore == "+":
        nb1 = input("Nombre 1 >>> ")
        nb2 = input("Nombre 2 >>> ")
        result = float(nb1) + float(nb2)
        if str(result).endswith(".0"):
            result = int(result)
        print(f"{nb1} + {nb2} = {result}")

    elif aurore == "-":
        nb1 = input("Nombre 1 >>> ")
        nb2 = input("Nombre 2 >>> ")
        result = float(nb1) - float(nb2)
        if str(result).endswith(".0"):
            result = int(result)
        print(f"{nb1} - {nb2} = {result}")

    elif aurore in ["*", "x"]:
        nb1 = input("Nombre 1 >>> ")
        nb2 = input("Nombre 2 >>> ")
        result = float(nb1) * float(nb2)
        if str(result).endswith(".0"):
            result = int(result)
        print(f"{nb1} * {nb2} = {result}")

    elif aurore in ["/", ":", "÷"]:
        nb1 = input("Nombre 1 >>> ")
        nb2 = input("Nombre 2 >>> ")
        if float(nb2) != 0:
            result = float(nb1) / float(nb2)
            if str(result).endswith(".0"):
                result = int(result)
            print(f"{nb1} ÷ {nb2} = {result}")
        else:
            print("\033[91m Erreur: Division par zéro impossible \033[0m")

    else:
        print("\033[91m Indisponible \033[0m")
