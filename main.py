from datetime import datetime, timedelta
import time
import threading

starttime = time.time()
alarme = ""
hour_now = datetime.now()


def prompt_hour():
    global hour_now
    while True:
        time.sleep(1 - ((time.time() - starttime) % 1))
        hour_now = hour_now + timedelta(seconds=1)
        global standart_date
        standart_date = hour_now.strftime("%H:%M:%S")
        if alarme == standart_date:
            print("Alarme enclenché")


def change_hour(hour):
    if verif_entry((hour[0], hour[1], hour[2])) == "ok":
        print("L'heure a bien été changée")

        return datetime.strptime(hour[0] + ":" + hour[1] + ":" + hour[2], "%H:%M:%S")
    else:
        print("Une erreur d'entrée est survenue ,veuillez vérifier votre entrée et recommencer")


def alarm(hour):
    if verif_entry(hour) == "ok":
        global alarme
        alarme = hour[0] + ":" + hour[1] + ":" + hour[2]
        print("L'alarme a bien été défini et activée")

    else:
        print("Entrée incorrecte, veuillez recommencer")
        return 0


def verif_entry(hour):
    try:
        hours = int(hour[0])
        if 23 >= hours > 0:
            pass
        else:
            return 0
    except ValueError:
        return 0

    try:
        minutes = int(hour[1])
        if 59 >= minutes >= 0:
            pass
        else:
            return 1
    except ValueError:
        return 1

    try:
        seconds = int(hour[2])
        if 59 >= seconds >= 0:
            pass
        else:
            return 1
    except ValueError:
        return 1
    else:
        return "ok"


#Démmarage de l'horloge sur un thread séparer du reste du programme
x = threading.Thread(target=prompt_hour)
x.start()

message = "Voulez vous afficher l'heure (Y) définir une alarme(A) ou changer l'heure(H)?"
test = input(message)
while True:
    match test:
        case "Y":
            print(standart_date)

        case "A":
            hours = input("Veuillez entrer l'heure de l'alarme(0-23):")
            minutes = input("Veuillez entrer les minutes de l'alarme(0-59):")
            seconds = input("Veuillez entrer les secondes l'alarme:")
            alarm((hours, minutes, seconds))

        case "H":
            hours = input("Veuillez entrer la nouvelle heure(0-23):")
            minutes = input("Veuillez entrer les minutes de la nouvelle heure(0-59):")
            seconds = input("Veuillez entrer les secondes de la nouvelle heure:")
            hour_now = change_hour((hours, minutes, seconds))

    test = input(message)