import subprocess
import requests
import socket
import platform
import concurrent.futures
from pypresence import Presence
import re
import os
import time
from pystyle import Colors, Colorate, Center
import whois as python_whois
import tkinter as tk 
from tkinter import messagebox

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
            small_image="logo_bluefox2",
            start=start_time
        )
    except Exception as e:
        print(f"Erreur lors de la mise à jour du RPC : {e}")

def ping_ip(ip_address):
    update_rpc("Ping d'une IP", f"Recherche de {ip_address}")
    try:
        result = subprocess.run(['ping', ip_address], capture_output=True, text=True, timeout=10)
        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nPINGING {ip_address}\n{'=' * 60}"))
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print(Colorate.Horizontal(Colors.blue_to_red, "Timeout expired. No response received."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))

def get_ip_information(ip_address):
    update_rpc("IP Lookup", f"Recherche d'infos pour {ip_address}")
    try:
        api_key = 'bf609e0ae94346a69905706a764efce5'
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}").json()
        
        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nIP Information\n{'=' * 60}"))

        ip_info = {
            "IP Address": response.get("ip"),
            "Continent": f"{response.get('continent_name')} ({response.get('continent_code')})",
            "Country": f"{response.get('country_name')} ({response.get('country_code3')})",
            "Region": response.get("state_prov"),
            "City": response.get("city"),
            "Postal Code": response.get("zipcode") if response.get("zipcode") else "Not available",
            "Latitude": response.get("latitude"),
            "Longitude": response.get("longitude"),
            "Time Zone": format_timezone(response.get('time_zone')),
            "ISP": response.get("isp"),
            "Organization": response.get("organization"),
            "Domain": response.get("domain") if response.get("domain") else "Not available",
            "ASN": response.get("asn"),
            "Altitude": response.get("altitude") if response.get("altitude") else "Not available",
            "Threat Level": response.get("threat").get("is_tor") if response.get("threat") else "Not available"
        }

        for key, value in ip_info.items():
            if value:
                print(Colorate.Horizontal(Colors.blue_to_red, f"{key}: {value}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))
        time.sleep(5)

def format_timezone(timezone_info):
    if timezone_info:
        return f"{timezone_info.get('name')} (UTC{timezone_info.get('offset')})"
    else:
        return ""

def traceroute_ip(ip_address, max_hops=30, timeout=5):
    update_rpc("En train de tracer une IP", f"Recherche de {ip_address}")
    try:
        if platform.system().lower() == "windows":
            command = ['tracert', '-h', str(max_hops), '-w', str(timeout * 1000), ip_address]
        else:
            command = ['traceroute', '-m', str(max_hops), '-w', str(timeout), ip_address]
        
        result = subprocess.run(command, capture_output=True, text=True)

        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nTRACEROUTE {ip_address}\n{'=' * 60}"))
        print(result.stdout)

    except subprocess.CalledProcessError as cpe:
        print(Colorate.Horizontal(Colors.blue_to_red, f"Command failed with error: {cpe}"))
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.blue_to_red, "Traceroute command not found. Please ensure it is installed on your system."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))

def reverse_dns_lookup(ip_address, dns_server=None):
    try:
        command = ['nslookup', ip_address]
        if dns_server:
            command.append(dns_server)
        
        result = subprocess.run(command, capture_output=True, text=True)

        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nREVERSE DNS LOOKUP {ip_address}\n{'=' * 60}"))
        print(result.stdout)

    except subprocess.CalledProcessError as cpe:
        print(Colorate.Horizontal(Colors.blue_to_red, f"Command failed with error: {cpe}"))
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.blue_to_red, "nslookup command not found. Please ensure it is installed on your system."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))

def scan_port(ip_address, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip_address, port))
        sock.close()
        return port if result == 0 else None
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"Error scanning port {port}: {e}"))
        return None

def port_scan(ip_address, start_port=1, end_port=1024, timeout=1, max_workers=100):
    open_ports = []
    print(Colorate.Horizontal(Colors.blue_to_red, f"Scanning ports on {ip_address} from {start_port} to {end_port}... This may take a while."))
    
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(scan_port, ip_address, port, timeout): port for port in range(start_port, end_port + 1)}
            for future in concurrent.futures.as_completed(futures):
                port = futures[future]
                if future.result():
                    open_ports.append(port)
                    print(Colorate.Horizontal(Colors.blue_to_red, f"Port {port} is open"))
        
        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nOPEN PORTS ON {ip_address}\n{'=' * 60}"))
        print(Colorate.Horizontal(Colors.blue_to_red, f"Open ports: {open_ports}"))
    
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred during port scanning: {e}"))


def whois_lookup(ip_address):

    try:
        if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip_address):
            print(Colorate.Horizontal(Colors.blue_to_red, "Invalid IP address format."))
            return

        result = whois.whois(ip_address)

        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nWHOIS LOOKUP {ip_address}\n{'=' * 60}"))
        
        if result:
            for key, value in result.items():
                if value:
                    if isinstance(value, list):
                        for item in value:
                            print(Colorate.Horizontal(Colors.blue_to_red, f"{key}: {item}"))
                    else:
                        print(Colorate.Horizontal(Colors.blue_to_red, f"{key}: {value}"))
        else:
            print(Colorate.Horizontal(Colors.blue_to_red, "No WHOIS information found for the IP address."))

    except whois.parser.PywhoisError as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"WHOIS lookup failed: {e}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))

def blacklist_check(ip_address):
    try:
        response = requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}", headers={
            'Key': '173b1074344847a7968aeee29091c3bea4db13e52eeb78e9f921ba1fe043468bf9d965d63666d411', 
            'Accept': 'application/json'
        }).json()
        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nBLACKLIST CHECK {ip_address}\n{'=' * 60}"))
        print(Colorate.Horizontal(Colors.blue_to_red, str(response)))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))

def dns_records(ip_address):
    try:
        import dns.resolver
        record_types = ['A', 'MX', 'NS', 'TXT']
        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nDNS RECORDS {ip_address}\n{'=' * 60}"))

        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(ip_address, record_type)
                for rdata in answers:
                    print(Colorate.Horizontal(Colors.blue_to_red, f"{record_type} record: {rdata}"))
            except dns.resolver.NoAnswer:
                print(Colorate.Horizontal(Colors.blue_to_red, f"No {record_type} record found for {ip_address}"))
            except dns.resolver.NXDOMAIN:
                print(Colorate.Horizontal(Colors.blue_to_red, f"{ip_address} does not exist."))
                break
            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))

def asn_info(ip_address):
    """
    Obtient des informations sur le système autonome (ASN) associé à une adresse IP donnée.
    
    Args:
        ip_address (str): L'adresse IP cible.
    """
    try:
        response = requests.get(f"https://api.iptoasn.com/v1/as/ip/{ip_address}").json()

        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nASN INFORMATION {ip_address}\n{'=' * 60}"))
        asn_info_to_display = {
            "IP Range": response.get("announced"),
            "ASN": response.get("as_number"),
            "ASN Organization": response.get("as_description"),
            "Country": response.get("country_code"),
            "Created": response.get("allocated") if response.get("allocated") else "Unknown",
            "Last Updated": response.get("updated") if response.get("updated") else "Unknown",
        }

        for key, value in asn_info_to_display.items():
            print(Colorate.Horizontal(Colors.blue_to_red, f"{key}: {value}"))

    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"Error fetching ASN information: {e}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))

def get_ip_info():
   hostname = socket.gethostname()
   local_ip = socket.gethostbyname(hostname)
   system = platform.system()

   if system == "Windows":
       ip_config_command = "ipconfig"
   else :
        ip_config_command = "ifconfig"

   ip_info = os.popen(ip_config_command).read()
   return f"Hostname: {hostname}\nLocal IP: {local_ip}\n\n{ip_info}"

def show_ip_info():
    ip_info = get_ip_info()
    print("Informations IP", ip_info)
    time.sleep(8)

def check_value():
    if int(entry.get()) == 20:
       show_message()
    elif int(entry.get()) == 11:
       show_ip_info()

def delayed_restart(): 
    time.sleep(5) 
    root.destroy() 
    main()


def main():
    update_rpc("Menu Principal", "Navigation dans les menus")
    ascii_art = """

░▒▓███████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░        ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░░▒▓████████▓▒░      ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                             
       ----------------------[BlueFox Tools]--------------------
                                                                         
        01) Ping IP                  06) IP Lookup                      
        02) IP Information           07) Blacklist Check                                                  
        03) IP Trace                 08) DNS Records                    
        04) Reverse DNS Lookup       09) ASN Information
        05) Scan Port                20) IP Config

    """
    colored_ascii = Colorate.Horizontal(Colors.blue_to_red, ascii_art)
    print(Center.XCenter(colored_ascii))
    
    while True:
        option = input(Colorate.Horizontal(Colors.blue_to_red, "\nEnter your choice: "))

        if option == "01":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address to ping: "))
            ping_ip(ip_address)
        elif option == "02":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address to get information: "))
            get_ip_information(ip_address)
        elif option == "03":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address for traceroute: "))
            traceroute_ip(ip_address)
        elif option == "04":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address for reverse DNS lookup: "))
            reverse_dns_lookup(ip_address)
        elif option == "05":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address for port scan: "))
            port_scan(ip_address)
        elif option == "06":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address for whois lookup: "))
            whois_lookup(ip_address)
        elif option == "07":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address for blacklist check: "))
            blacklist_check(ip_address)
        elif option == "08":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address for DNS records: "))
            dns_records(ip_address)
        elif option == "09":
            ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address for ASN information: "))
            asn_info(ip_address)
        elif option == "10":
            print(Colorate.Horizontal(Colors.blue_to_red, "Exiting program..."))
        elif option == "20":
            print(Colorate.Horizontal(Colors.blue_to_red, "Your IP"))
            show_ip_info()

            break
        else:
            print(Colorate.Horizontal(Colors.blue_to_red, "Invalid option. Please choose a number from 1 to 10."))
        
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()