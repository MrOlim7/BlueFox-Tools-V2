import colorama
from colorama import Fore, Back, Style
import requests

colorama.init(autoreset=True)

def display_menu():
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + " *Blue Fox* ".center(50, " "))
    print("\n")
    print(Fore.BLUE + "[01] Réseaux Sociaux")
    print("\n")

def search_social_media(username):
    urls = {
        "YouTube": f"https://www.youtube.com/results?search_query={username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}"
    }

    for platform, url in urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{platform}: {url}")
        else:
            print(f"{platform}: Not found")

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

if __name__ == "__main__":
    main()
