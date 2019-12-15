import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


@dataclass
class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """
    id_name: str
    name: str
    max_level: int
    description: str
    items: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = self.name.replace('_', ' ')

    def __repr__(self):
        return f'{self.name} ({self.max_level}): {self.description}'


@dataclass()
class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """
    name: str
    enchantments: List[str] = field(default_factory=list)

    # def __post_init__(self):
    #     self.name = self.name.replace('_',' ').title()

    def __repr__(self):
        en = [f'  [{chant.max_level}] {chant.id_name}'
              for chant in sorted(self.enchantments, key=lambda x : x.id_name)]
        return f'{self.name.replace("_"," ").title()}: \n' + '\n'.join(en)


# Lookup values of the first five roman numerals
LEVEL_TRANSLATE = {'I': 1,
                   'II': 2,
                   'III': 3,
                   'IV': 4,
                   'V': 5}


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    res = dict()
    for row in soup.select('table#minecraft_items > tr'):
        data_items = row.find_all('td')
        if data_items is None or len(data_items) == 0:
            continue
        enchant, maxlevel, descr, id, item, version = data_items
        id_name = enchant.em.text
        name = enchant.a.text
        max_level = LEVEL_TRANSLATE[maxlevel.text.strip()]
        description = descr.text
        item_url = item.img.attrs.get('data-src')
        items = re.sub(r'.*/(?:enchanted_)?(?:iron_)?([^/]+?)(?:_sm)?\.png', r'\1', item_url)
        items = items.replace('fishing_rod', 'FISHING=ROD')
        items = list(map(lambda s: s.replace('FISHING=ROD', 'fishing_rod'), items.split('_')))

        res[id_name] = Enchantment(id_name,
                                   name,
                                   max_level,
                                   description,
                                   items
                                   )

    return res


def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    res = dict()
    for enchantment in data.values():
        for i in enchantment.items:
            if i in res.keys():
                res[i].enchantments.append(enchantment)
            else:
                res[i] = Item(i, [enchantment])
    return dict(sorted(res.items(), key=lambda t: t[0]))


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
