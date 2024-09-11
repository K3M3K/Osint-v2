import subprocess
import random
import os
import re
import time
import sys
import whois
import requests
from bs4 import BeautifulSoup
import socket
import urllib.parse
import ssl
import netifaces
import whois
from colorama import Fore, Style
from requests.exceptions import RequestException



def osint_tools_menu():
    print("Menu:")
    print(f"{Fore.GREEN}1. Osint Tools{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. Exit{Style.RESET_ALL}")

def create_banner():
    banner = f'''
{Fore.RED}    
 ███▄ ▄███▓ ██▀███        ▒█████   █     █░ ██▓    
▓██▒▀█▀ ██▒▓██ ▒ ██▒     ▒██▒  ██▒▓█░ █ ░█░▓██▒    
▓██    ▓██░▓██ ░▄█ ▒     ▒██░  ██▒▒█░ █ ░█ ▒██░    
▒██    ▒██ ▒██▀▀█▄       ▒██   ██░░█░ █ ░█ ▒██░    
▒██▒   ░██▒░██▓ ▒██▒ ██▓ ░ ████▓▒░░░██▒██▓ ░██████▒
░ ▒░   ░  ░░ ▒▓ ░▒▓░ ▒▓▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ░ ▒░▓  ░ 
░  ░      ░  ░▒ ░ ▒░ ░▒    ░ ▒ ▒░   ▒ ░ ░  ░ ░ ▒  ░
░      ░     ░░   ░  ░   ░ ░ ░ ▒    ░   ░    ░ ░   
       ░      ░       ░      ░ ░      ░        ░  ░ 
{Style.RESET_ALL} 
Osint Tools Script | This code was created with MR.0WL|
Author : MR.0WL
''' 
    return banner

def call_osint():
    try:
        osint_tools()
    except Exception as e:
        print(f"{Fore.RED}Failed to run osint tools: {e}{Style.RESET_ALL}")

def osint_tools():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(create_banner())
        osint_tools_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Launching osint tools...")
            break
        elif choice == "2":
            print("Exiting program...")
            sys.exit()  
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    call_osint()



def create_banner():
    banner = f'''
{Fore.RED}    
 ███▄ ▄███▓ ██▀███        ▒█████   █     █░ ██▓    
▓██▒▀█▀ ██▒▓██ ▒ ██▒     ▒██▒  ██▒▓█░ █ ░█░▓██▒    
▓██    ▓██░▓██ ░▄█ ▒     ▒██░  ██▒▒█░ █ ░█ ▒██░    
▒██    ▒██ ▒██▀▀█▄       ▒██   ██░░█░ █ ░█ ▒██░    
▒██▒   ░██▒░██▓ ▒██▒ ██▓ ░ ████▓▒░░░██▒██▓ ░██████▒
░ ▒░   ░  ░░ ▒▓ ░▒▓░ ▒▓▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ░ ▒░▓  ░ 
░  ░      ░  ░▒ ░ ▒░ ░▒    ░ ▒ ▒░   ▒ ░ ░  ░ ░ ▒  ░
░      ░     ░░   ░  ░   ░ ░ ░ ▒    ░   ░    ░ ░   
       ░      ░       ░      ░ ░      ░        ░  ░ 
{Style.RESET_ALL} 
Osint Tools Script | This code was created with MR.0WL|
Author : MR.0WL
'''
    return banner
def clean_and_format_url(url):
    url_components = urllib.parse.urlparse(url)
    cleaned_url = urllib.parse.urlunparse(url_components)
    return cleaned_url

def get_ssl_info(domain_name):
    context = ssl.create_default_context()
    with socket.create_connection((domain_name, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain_name) as ssock:
            return ssock.version(), ssock.cipher()

def check_security(domain_name):
    try:
        response = requests.get("https://" + domain_name)
        if response.status_code == 200:
            print("Security Information:")
            print("SSL/TLS Protocol:", response.connection.version)
            print("SSL Certificate:", response.connection.cipher())
        else:
            print("Security Information: Unable to retrieve security details")
    except Exception as e:
        print("Security Information: Unable to retrieve security details")

def fetch_full_title(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            if "instagram.com" in url:
                title_tag = soup.find("meta", property="og:title")
                title = title_tag["content"] if title_tag else soup.title.string if soup.title else "No title found"
            elif "youtube.com" in url:
                title_tag = soup.find("meta", property="og:title")
                title = title_tag["content"] if title_tag else soup.title.string if soup.title else "No title found"
            else:
                title = soup.title.string if soup.title else "No title found"
            return title.strip()
        else:
            return "No title found"
    except Exception as e:
        return "No title found"
    
def extract_phone_numbers(text):
    phone_pattern = re.compile(r'\+?\d[\d -]{8,12}\d', re.IGNORECASE)
    phone_numbers = phone_pattern.findall(text)
    return phone_numbers

def extract_addresses(text):
    address_pattern = re.compile(r'\d{1,5}\s\w+(\s\w+)*,?\s\w+(\s\w+)*', re.IGNORECASE)
    addresses = address_pattern.findall(text)
    return [address[0] for address in addresses]

def search_google(query, num_results=30, offset=0):
    url = "https://www.google.com/search"
    params = {"q": query, "num": num_results, "start": offset}
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    ]

    headers = {"User-Agent": random.choice(user_agents)}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to make request: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for g in soup.find_all('div', class_='g'):
        title_tag = g.find('h3')
        title = title_tag.text if title_tag else "No title"
        link_tag = g.find('a')
        link = link_tag.get('href', 'No link') if link_tag else "No link"
        snippet_tag = g.find('span', class_='aCOpRe')
        snippet = snippet_tag.text if snippet_tag else ""

        phone_numbers = extract_phone_numbers(snippet)
        addresses = extract_addresses(snippet)

        results.append({
            "title": title,
            "link": link,
            "snippet": snippet,
            "phone_numbers": phone_numbers,
            "addresses": addresses
        })
    
    time.sleep(2)  # Add delay to avoid rate limiting
    return results

def search_by_name():
    offset = 0
    max_results = 30  # Maximum number of results to fetch

    popular_indonesian_websites = [
        "kompas.com", "detik.com", "tribunnews.com", "cnnindonesia.com", "tempo.co",
        "suara.com", "merdeka.com", "liputan6.com", "kumparan.com", "inews.id",
        "bukalapak.com", "tokopedia.com", "shopee.co.id", "lazada.co.id", "blibli.com",
        "kaskus.co.id", "kompasiana.com", "hipwee.com", "medium.com/@id", "blogger.com",
        "indonesia.go.id", "kemdikbud.go.id", "setneg.go.id", "brilio.net", "alodokter.com",
        "sehatq.com", "traveloka.com", "tiket.com", "klikdokter.com", "ruangguru.com"
    ]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_banner())
        print("\nOptions:")
        print(f"{Fore.GREEN}[1] Continue Search by Name{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[2] Return to main menu{Style.RESET_ALL}")

        choice = input("Choose an option: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())
            query = input("\nInput name victim: ").strip()
            if not query:
                print("Query cannot be empty. Please enter a valid query.")
                input("Press Enter to continue...")
                continue

            print(f"[~] Searching {query}")

            results = []
            try:
                while offset < max_results:
                    partial_results = search_google(query, offset=offset)
                    if not partial_results:
                        break
                    results.extend(partial_results)
                    offset += len(partial_results)
                    time.sleep(2)  # Slow down requests to prevent being blocked

                if results:
                    for item in results:
                        cleaned_url = clean_and_format_url(item.get('link', ''))
                        try:
                            full_title = fetch_full_title(cleaned_url)
                        except Exception as e:
                            full_title = f"Error fetching title: {e}"

                        print(f"[+] Url detected: {cleaned_url}")
                        print(f"[?] Title: {full_title}")

                        # Extract and display phone numbers and addresses
                        text_content = item.get('snippet', '')  # Or fetch full page content if needed
                        phone_numbers = extract_phone_numbers(text_content)
                        addresses = extract_addresses(text_content)

                        if phone_numbers:
                            print("Phone Numbers Found:")
                            for number in phone_numbers:
                                print(f" - {number}")

                        if addresses:
                            print("Addresses Found:")
                            for address in addresses:
                                print(f" - {address}")

                        # Check if URL belongs to popular Indonesian websites
                        if any(website in cleaned_url for website in popular_indonesian_websites):
                            print(f"--- Text and link are similar: {cleaned_url}")

                        if not text_content:
                            print("--- No data found")
                        else:
                            print(f"Snippet: {text_content}")

                        time.sleep(0.5)  # Slow down displaying results
                else:
                    print("--- No data found")

                input("Press Enter to continue...")
            except KeyboardInterrupt:
                print("\nSearch stopped by user.")
                input("Press Enter to continue...")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                input("Press Enter to continue...")
        elif choice == '2':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

            
def search_social_media():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_banner())
        print("\nOptions:")
        print(f"{Fore.GREEN}[1] Continue Search Social Media{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[2] Return to main menu{Style.RESET_ALL}")

        choice = input("Choose an option: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner()) 
            query = input("\nSearch Social Media: ")
            print("Searching... ", end="", flush=True)
            animation = "|/-\\"
            idx = 0

            try:
                results = search_google(query)
                if results:
                    print("\nResults:")
                    for i, item in enumerate(results, start=1):
                        print(f"\nResult #{i}:")
                        print(f"Title: {item['title']}")
                        print(f"Link: {item['link']}")
                        print(f"Snippet: {item['snippet']}")
                        time.sleep(1)
                else:
                    print("No results found for social media accounts.")

                input("Press Enter to continue...")
            except KeyboardInterrupt:
                print("\nSearch stopped by user.")
                input("Press Enter to continue...")
        elif choice == '2':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
            


def search_with_operator():
    offset = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_banner())
        print("\nOptions:")
        print(f"{Fore.GREEN}[1] Search for admin login pages{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[2] Search for backend interfaces{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[3] Search for web APIs{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[4] Search for admin tools{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[5] Return to main menu{Style.RESET_ALL}")
        choice = input("Choose an option: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())
            print("Searching for admin login pages...")
            site = input("Enter the website domain (e.g., example.com): ").strip()
            if not site:
                print("Website domain cannot be empty. Please enter a valid domain.")
                input("Press Enter to return to the menu...")
                continue
            query = f"site:{site} login OR admin"
            print("Searching...")
            try:
                results = search_google(query, offset=offset)
                display_results(results)
            except KeyboardInterrupt:
                print("\nSearch stopped by user.")
            time.sleep(2)  # Delay the next search to slow down the process

        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())
            print("Searching for backend interfaces...")
            site = input("Enter the website domain (e.g., example.com): ").strip()
            if not site:
                print("Website domain cannot be empty. Please enter a valid domain.")
                input("Press Enter to return to the menu...")
                continue
            query = f"site:{site} backend OR controlpanel OR admin.php"
            print("Searching...")
            try:
                results = search_google(query, offset=offset)
                display_results(results)
            except KeyboardInterrupt:
                print("\nSearch stopped by user.")
            time.sleep(2)  # Delay the next search to slow down the process

        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())
            print("Searching for web APIs...")
            site = input("Enter the website domain (e.g., example.com): ").strip()
            if not site:
                print("Website domain cannot be empty. Please enter a valid domain.")
                input("Press Enter to return to the menu...")
                continue
            query = f"site:{site} API"
            print("Searching...")
            try:
                results = search_google(query, offset=offset)
                display_results(results)
            except KeyboardInterrupt:
                print("\nSearch stopped by user.")
            time.sleep(2)  # Delay the next search to slow down the process

        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())
            print("Searching for admin tools...")
            query = "admin/tools OR filemanager"
            print("Searching...")
            try:
                results = search_google(query, offset=offset)
                display_results(results)
            except KeyboardInterrupt:
                print("\nSearch stopped by user.")
            time.sleep(2)  # Delay the next search to slow down the process

        elif choice == '5':
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")

def display_results(results):
    if results:
        print("\nResults:")
        for i, item in enumerate(results, start=1):
            print(f"\nResult #{i}:")
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            print(f"Snippet: {item['snippet']}")
            time.sleep(1)  # Introduce delay between each result
        print("\nNo more results.")
        input("Press Enter to return to the menu...")
    else:
        print("No results found.")

                        
def dns_lookup():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_banner())
        print("\nOptions:")
        print(f"{Fore.GREEN}[1] Continue DNS Look Up{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[2] Return to main menu{Style.RESET_ALL}")

        choice = input("Choose an option: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())
            domain_name = input("\nEnter domain name to lookup: ")

            if not domain_name.strip():
                print("\nDomain name cannot be empty. Please enter a valid domain name.")
                input("\nPress Enter to continue...")
                continue

            print("Performing DNS lookup... ", end="", flush=True)

            try:
                # Resolving DNS Name to IP Address
                ip_address = socket.gethostbyname(domain_name)
                print(f"\nDNS lookup for {domain_name}:\nIP Address: {ip_address}")

                # WHOIS Lookup
                domain_info = whois.whois(domain_name)

                # Mendapatkan informasi registrar dan expiration date dari hasil WHOIS lookup
                provider = domain_info.get('registrar', 'Unknown')
                print(f"Provider: {provider}")
                expiration_date = domain_info.get('expiration_date', 'Not available')
                print(f"Expiration Date: {expiration_date}")

                # Reverse DNS Lookup
                try:
                    reverse_dns = socket.gethostbyaddr(ip_address)
                    print(f"Reverse DNS Lookup: {reverse_dns[0]}")
                except socket.herror:
                    print("Reverse DNS Lookup: Not available")

                # DNS Record Lookup
                dns_records = socket.getaddrinfo(domain_name, None)
                print("\nDNS Records:")
                for record in dns_records:
                    print(record)

                # Additional Information
                print("\nAdditional Information:")
                print(f"Local IP Address: {socket.gethostbyname(socket.gethostname())}")
                print("Server IP Address:", socket.gethostbyname(socket.gethostname()))

                interfaces = netifaces.interfaces()
                for interface in interfaces:
                    if interface != "lo":
                        addresses = netifaces.ifaddresses(interface)
                        if netifaces.AF_INET in addresses:
                            print("Network Address:", addresses[netifaces.AF_INET][0]['addr'])
                            break
                print("Network Type:", netifaces.gateways()['default'][netifaces.AF_INET][1])

            except socket.gaierror as e:
                print(f"\nDNS lookup failed for {domain_name}: {e}")
            except whois.parser.PywhoisError as e:
                print(f"\nFailed to retrieve WHOIS information for {domain_name}: {e}")
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            print("Returning to recognition menu...")
            break
        else:
            print("Invalid choice. Please try again.")
            

                        
def home_menu():
    print(create_banner())
    print("\nMenu:")
    print(f"{Fore.GREEN}[1] Search by Name{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[2] Search Sosial Media{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[3] WEB Analyst{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[4] DNS Look Up{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[5] Back to menu{Style.RESET_ALL}")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        home_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            search_by_name()
        elif choice == "2":
            search_social_media()
        elif choice == "3":
            search_with_operator()
        elif choice == "4":
            dns_lookup()
        elif choice == "5":
            print("Returning to main menu")
            osint_tools()  
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")


def osint_tools_menu():
    print("Menu:")
    print(f"{Fore.GREEN}1. Osint Tools{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. Exit{Style.RESET_ALL}")

def call_osint():
    try:
        osint_tools()
    except Exception as e:
        print(f"{Fore.RED}Failed to run osint tools: {e}{Style.RESET_ALL}")

def osint_tools():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print(create_banner())
        osint_tools_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Launching osint tools...")
            break
        elif choice == "2":
            print("Exiting program...")
            sys.exit() 
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
