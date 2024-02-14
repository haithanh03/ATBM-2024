import os
import requests

def get_report_given_domain(domain):
    base_url = 'https://www.virustotal.com/api/v3/domains/'
    headers = {'x-apikey' : os.environ['3762fc96e31e84606201a803687c28daf022a52f45d1e1a4f56505c412a4c923']}
    #domain = input("Enter the domain: ")
    formatted_url = f'{base_url}/{domain}'
    response = requests.get(formatted_url, headers=headers)
    