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
            print ("Alarme enclenché")

def change_hour():
    hours = input("Veuillez entrer la nouvelle heure(0-23):")
    minutes = input("Veuillez entrer les minutes de la nouvelle heure(0-59):")
    seconds = input("Veuillez entrer les secondes de la nouvelle heure:")
    if verif_entry(hours, minutes, seconds) =="ok":
        print("L'heure a bien été changée")

        return datetime.strptime(hours + ":" + minutes + ":" + seconds, "%H:%M:%S")
    else: print("Une erreur d'entrée est survenue ,veuillez vérifier votre entrée et recommencer")


def main_function():
    global hour_now
    x = threading.Thread(target=prompt_hour)
    x.start()
    message="Voulez vous afficher l'heure (Y) définir une alarme(A) ou changer l'heure(H)?"
    test = input(message)
    while True:
        match test:
            case "Y":
                print(standart_date)
            case"A":
                alarm()
            case "H":
                hour_now=change_hour()
        test = input(message)

def alarm():
    hours = input("Veuillez entrer l'heure de votre alarme(0-23):")
    minutes = input("Veuillez entrer les minutes de votre alarme(0-59):")
    seconds = input("Veuillez entrer les secondes de votre alarme(0-59):")
    if verif_entry(hours, minutes, seconds) =="ok":
        global alarme
        alarme=hours+":"+minutes+":"+seconds
        print("L'alarme a bien été défini et activée")

    else:
        print("Entrée incorrecte, veuillez recommencer")
        return 0



def verif_entry(hours, minutes, seconds):
    try:
        hours = int(hours)
        if 23 >= hours > 0:
            pass
        else:
            return 0
    except ValueError:
        return 0

    try:
        minutes = int(minutes)
        if 59 >= minutes >= 0:
            pass
        else:
            return 1
    except ValueError:
        return 1

    try:
        seconds = int(seconds)
        if 59 >= seconds >= 0:
            pass
        else:
            return 1
    except ValueError:
        return 1
    else:return "ok"

main_function()
