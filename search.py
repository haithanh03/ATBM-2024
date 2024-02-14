import requests

url = "https://www.virustotal.com/api/v3/search?query="
search =  input("Search something do you want: ")
url = url + search
headers = {
    "accept": "application/json",
    "x-apikey": "3762fc96e31e84606201a803687c28daf022a52f45d1e1a4f56505c412a4c923"
}

response = requests.get(url, headers=headers)

print(response.text)