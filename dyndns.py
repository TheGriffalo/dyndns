from requests import get 
import requests

data = {
    "username": "3jc9v5fbcss2fn5t",
    "password": "FN8edPaq2D0QPsAxx6slS;x6UTjn2n"
}

response = requests.post('https://ipv4.api.mythic-beasts.com/dns/v2/dynamic/potato.griffalo.net', data=data)

ip = get('https://api.ipify.org').text
print ('My public IP address is:', ip)

mburl = "https://ipv4.api.mythic-beasts.com/dns/v2/dynamic/potato.griffalo.net"

