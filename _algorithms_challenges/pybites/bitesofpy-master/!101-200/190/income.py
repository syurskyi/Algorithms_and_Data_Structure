from pathlib import Path
from collections import defaultdict
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    tree = ET.parse(xml)
    root = tree.getroot()
    namespaces = {'wb': 'http://www.worldbank.org'}

    xpath = f".//wb:country"
    country_list = defaultdict(list)
    for x in root.findall(xpath, namespaces):
        country_list[x.find('wb:incomeLevel', namespaces).text].append(x.find('wb:name', namespaces).text)

    return country_list
