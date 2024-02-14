import requests
import colorama 
from time import sleep 
import sys

colorama.init()
def type(words: str):
    for char in words:
        sleep(0.5)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    

domain = input("Enter the domain: ")
url = "https://www.virustotal.com/api/v3/domains/" + domain

headers = {
    "accept": "application/json",
    "x-apikey": "3762fc96e31e84606201a803687c28daf022a52f45d1e1a4f56505c412a4c923"
}

response = requests.get(url, headers=headers)

# Chuyển đổi văn bản JSON thành đối tượng Python
data = response.json()

# Truy cập vào phần tử "attributes"
attributes = data["data"]["attributes"]

# In ra phần "attributes"
print("Thông tin về url vừa tìm kiếm!")
#type((colorama.Fore.WHITE + "Reputation: ", colorama.Fore.YELLOW + str(attributes['reputation'])))
type((colorama.Fore.WHITE+ colorama.Style.BRIGHT + "Reputation: ", colorama.Fore.YELLOW + str(attributes['reputation'])))
type((colorama.Fore.WHITE+ colorama.Style.BRIGHT + "Last DNS records date: ", colorama.Fore.YELLOW + str(attributes['last_dns_records_date'])))
type((colorama.Fore.WHITE+ colorama.Style.BRIGHT + "Whois date: ", colorama.Fore.YELLOW + str(attributes['whois_date'])))
type((colorama.Fore.WHITE+ colorama.Style.BRIGHT + "Creation date: ", colorama.Fore.YELLOW + str(attributes['creation_date'])))
type((colorama.Fore.WHITE+ colorama.Style.BRIGHT + "Registrar: ", colorama.Fore.YELLOW + str(attributes['registrar'])))
type((colorama.Fore.WHITE+ colorama.Style.BRIGHT + "Last analysis date: ", colorama.Fore.YELLOW + str(attributes['last_analysis_date'])))
type((colorama.Fore.WHITE+ colorama.Style.BRIGHT + "Last analysis stats: ", colorama.Fore.YELLOW + str(attributes['last_analysis_stats'])))