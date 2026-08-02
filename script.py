import math
import datetime as dt

print("\nAurore Pro Py [BÊTA]")
print("Tape 'help' pour une liste des commandes.")

while True:
    aurore = input("\n>>> ")
    print("\n")

    if aurore == "help":
        print("Tape 'quit' pour quitter")
        print("Tape 'time' pour obtenir la date et l'heure actuelle")
        print("Tape 'version' (ou 'v') pour obtenir le numéro de version")
        print("Tape '+' pour une addition, '-' pour une soustraction, '*' (ou 'x') pour unr multiplication ou '/' (ou ':' ou '÷') pour unr division")

    elif aurore == "quit":
        break

    elif aurore == "version" or aurore == "v" :
        print("Aurore Pro Py [v. 1.3 // BÊTA]")

    elif aurore == "time":
        now = dt.datetime.now()
        print(f"Nous sommes le {now.strftime('%d/%m/%Y')} et il est {now.strftime('%H:%M:%S')}")

    elif aurore == "+" :
      nb1 = input("Nombre 1 >>> ")
      nb2 = input("Nombre 2 >>> ")
      result = float(nb1) + float(nb2)
      if str(result).endswith(".0"):
        result = int(result)
      print(f"""{nb1} + {nb2} = {result}""")

    elif aurore == "-" :
      nb1 = input("Nombre 1 >>> ")
      nb2 = input("Nombre 2 >>> ")
      result = float(nb1) - float(nb2)
      if str(result).endswith(".0"):
        result = int(result)
      print(f"""{nb1} - {nb2} = {result}""")

    elif aurore == "*" or aurore == "x" :
      nb1 = input("Nombre 1 >>> ")
      nb2 = input("Nombre 2 >>> ")
      result = float(nb1) * float(nb2)
      if str(result).endswith(".0"):
        result = int(result)
      print(f"""{nb1} * {nb2} = {result}""")

    elif aurore == "/" or aurore == ":" or aurore == "÷" :
      nb1 = input("Nombre 1 >>> ")
      nb2 = input("Nombre 2 >>> ")
      if float(nb2) != 0:
        result = float(nb1) / float(nb2)
        if str(result).endswith(".0"):
          result = int(result)
        print(f"""{nb1} ÷ {nb2} = {result}""")
      else:
        print("\033[91m Erreur: Division par zéro impossible \033[0m")
 
    else:
      print("\033[91m Indisponible \033[0m")
