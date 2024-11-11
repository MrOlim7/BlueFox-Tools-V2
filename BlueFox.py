import colorama
from colorama import Fore, Back, Style
import requests
import os
import time
import pyfiglet
import random
import time
from scapy.all import sr1, IP, ICMP
import string
from pypresence import Presence

colorama.init(autoreset=True)

client_id = "1305534641200959600"
RPC = Presence(client_id)
RPC.connect()

start_time = int(time.time())

def update_rpc(state, details):
    try:
        RPC.update(
            state=state,
            details=details,
            large_image="large_image_name",
            small_image="logo_bluefox",
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
    print(Fore.BLUE + "[01] Réseaux Sociaux")
    print(Fore.BLUE + "[02] IP Pinger")
    print(Fore.BLUE + "[03] Password Generator")
    print(Fore.BLUE + "[04] Convertisseur de Monnaie")
    print("\n")

def search_social_media(username):
    update_rpc("Recherche sur Réseaux Sociaux", f"Recherche de {username}")
    urls = {
        "YouTube": f"https://www.youtube.com/results?search_query={username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}"
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
    update_rpc("IP Pinger", f"Ping de {ip}")
    try:
        print(f"Scanning IP: {ip}")
        packet = IP(dst=ip)/ICMP()
        response = sr1(packet, timeout=2, verbose=False)
        if response is None:
            print("No response received.")
        else:
            print(f"Response received from: {response.src}")
            print(f"Response time: {response.time - packet.sent_time}s")
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

def main():
    while True:
        try:
            update_rpc("Menu Principal", "Navigation dans les menus")
            display_menu()
            choice = input(Fore.GREEN + "Entrez votre choix: ")
            if choice == "01":
                username = input("Entrez le pseudo: ")
                search_social_media(username)
                time.sleep(5) # Pause de 5 secondes
            elif choice == "02":
                time.sleep(2) # Pause de 2 secondes
            elif choice == "03":
                password_generator()
            elif choice == "04":
                currency_converter()
            else:
                print("Choix invalide, veuillez réessayer.")
                time.sleep(2) # Pause de 2 secondes avant de réafficher le menu
        except Exception as e:
            print(f"Une erreur s'est produite dans la boucle principale: {e}")
            time.sleep(2) # Pause de 2 secondes avant de réessayer

if __name__ == "__main__":
    main()
