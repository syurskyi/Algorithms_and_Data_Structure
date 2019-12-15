import requests
import json

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    with requests.Session() as session:
        url_format = IPINFO_URL.format(ip=ip_address)
        decode = session.get(url_format).content.decode('utf-8')
        data = json.loads(decode)
    return data['country']
