#Copyright (c) BlueFox
#FR : Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#Ne revendez pas ce tool, ne le créditez pas au vôtre.

import colorama
from colorama import Fore, Back, Style
import requests
import os
import time
import pyfiglet
import random
import time
from ping3 import ping
import string
import webbrowser
from pypresence import Presence
import json

colorama.init(autoreset=True)

client_id = "1305534641200959600"
RPC = Presence(client_id)
RPC.connect()

start_time = int(time.time())

api_key = "dd24a2d45cc4f7e359fd5d2df52cacfa"

def update_rpc(state, details):
    try:
        RPC.update(
            state=state,
            details=details,
            large_image="large_image_name",
            small_image="logo_bluefox2",
            start=start_time
        )
    except Exception as e:
        print(f"Erreur lors de la mise à jour du RPC : {e}")

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_banner = pyfiglet.figlet_format("BLUE FOX", font="slant")
    print(Fore.BLUE + ascii_banner)
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + " https://github.com/MrOlim7/BlueFox ".center(50, " "))
    print("\n")
    print(Fore.BLUE + Style.BRIGHT + "Utilities".center(20, " "))
    print("\b")
    print(Fore.BLUE + "[01] Réseaux Sociaux")
    print(Fore.BLUE + "[02] IP Pinger")
    print(Fore.BLUE + "[03] Password Generator")
    print(Fore.BLUE + "[04] Convertisseur de Monnaie")
    print(Fore.BLUE + "[05] IP Lookup")
    print(Fore.BLUE + "[06] IP Generator")
    print("\n")

def search_social_media(username):
    update_rpc("Recherche sur Réseaux Sociaux", f"Recherche de {username}")
    urls = {
        "YouTube": f"https://www.youtube.com/results?search_query={username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/"
    }


    for platform, url in urls.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{platform}: {url}")
            else:
                print(f"{platform}: Not found")
        except requests.RequestException as e:
            print(f"Erreur lors de l'accès à {platform}: {e}")

    
def main():
    try:
        display_menu()
        choice = input(Fore.GREEN + "Entrez votre choix: ")
        if choice == "01":
            username = input("Entrez le pseudo: ")
            search_social_media(username)
        else:
            print("Choix invalide, veuillez réessayer.")
            main()
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def ip_pinger(ip):
    update_rpc("IP Pinger", f"Ping d'une IP")
    try:
        response_time = ping(ip, timeout=2)
        if response_time is None :
            print("Pas de réponse reçue.")
        else :
            print(f"Réponse reçue de {ip}: temps de réponse {response_time} ms")
    except Exception as e:
        print(f"Erreur lors du ping de l'IP: {e}")

def generate_password(length):
    update_rpc("Générateur de Mots de Passe", f"Génération de {length} caractères")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_generator():
    try:
        length_str = input("Entrez la longueur du mot de passe : ")
        length = int(length_str)
        print("Votre mot de passe généré est :", generate_password(length))
        time.sleep(5)  # Pause de 5 secondes pour afficher le résultat
    except ValueError:
        print("Entrée invalide, veuillez entrer un nombre.")
        time.sleep(2)

def convert_currency(amount, rate):
    update_rpc("Convertisseur de Monnaie", "Conversion en cours")
    return amount * rate

def currency_converter():
    exchange_rates = {
        'EUR_TO_USD': 1.12,
        'USD_TO_EUR': 0.89
    }

    try:
        amount_str = input("Entrez le montant : ")
        amount = float(amount_str)
        direction = input("Convertir de EUR vers USD (1) ou de USD vers EUR (2) : ")

        if direction == '1':
            print("Montant converti :", convert_currency(amount, exchange_rates['EUR_TO_USD']), "USD")
        elif direction == '2':
            print("Montant converti :", convert_currency(amount, exchange_rates['USD_TO_EUR']), "EUR")
        else:
            print("Choix invalide.")
        time.sleep(5) # Pause de 5 secondes pour afficher le résultat
    except ValueError:
        print("Entrée invalide, veuillez entrer un nombre.")
        time.sleep(2)

def ip_lookup(ip):
    update_rpc("IP Lookup", f"Recherche d'infos pour {ip}")
    try :
        url = f"http://api.ipstack.com/{ip}?access_key={api_key}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            print(f"Adresse IP: {ip}")
            print(f"Pays: {data.get('country_name', 'Inconnu')}")
            print(f"Région: {data.get('region_name', 'Inconnu')}")
            print(f"Ville: {data.get('city', 'Inconnu')}")
            print(f"Code Postal: {data.get('zip', 'Inconnu')}")
            print(f"Latitude: {data.get('latitude', 'Inconnu')}")
            print(f"Longitude: {data.get('longitude', 'Inconnu')}")
        else:
            print("Impossible de récupérer les informations.")
    except Exception as e:
        print(f"Erreur lors du lookup IP: {e}")

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

webhook_url = "https://discord.com/api/webhooks/1305959414670426246/Kf4K_mIf-_DR0WNcnl3WgUifmSok25eRiw6_ApCWVvZ2T36BqRdCDMGvYYiSBbxD95-R"

def notify_discord(webhook_url, message):
    data = {
        "content": message
    }
    try :
        response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        if response.status_code != 204:
            print(f"Erreur lors de l'envoi de la notification Discord: {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification Discord: {e}")

def ip_generator():
    update_rpc("Générateur d'IP", "Génération et vérification d'IP")
    webhook_choice = input("Voulez-vous utiliser un webhook Discord ? (y/n) : ").lower()
    webhook_url = ""
    if webhook_choice == 'y':
        webhook_url = input("Entrez l'URL du webhook Discord : ")

    for _ in range(10):
        ip = generate_ip()
        print(f"Générée: {ip}")
        try :
            response_time = ping(ip, timeout=2)
            if response_time is not None:
                print(Fore.GREEN + f"IP valide trouvée: {ip}")
                if webhook_url:
                    notify_discord(webhook_url, f"IP valide trouvée: {ip}")
        except Exception as e:
            print(f"Erreur lors de la vérification de l'IP: {e}")
    time.sleep(6)
    
def easter_egg():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
    webbrowser.open(url)
    print("Easter Egg! Redirection vers", url)
    time.sleep(5)

def main():
    while True:
        try:
            update_rpc("Menu Principal", "Navigation dans les menus")
            display_menu()
            choice = input(Fore.GREEN + "Entrez votre choix: ")
            if choice == "01":
                username = input("Entrez le pseudo: ")
                search_social_media(username)
                time.sleep(6) # Pause de 5 secondes
            elif choice == "02":
                ip = input("Entrez l'adresse IP: ")
                ip_pinger(ip)
                time.sleep(6) # Pause de 2 secondes
            elif choice == "05":
                ip = input("Entrez l'adresse IP: ")
                ip_lookup(ip)
                time.sleep(5)
            elif choice == "03":
                password_generator()
            elif choice == "04":
                currency_converter()
            elif choice == "06":
                ip_generator()
            elif choice == "444":
                easter_egg()
            else:
                print("Choix invalide, veuillez réessayer.")
                time.sleep(2)
        except Exception as e:
            print(f"Une erreur s'est produite dans la boucle principale: {e}")
            time.sleep(2) # Pause de 2 secondes avant de réessayer

if __name__ == "__main__":
    main()
