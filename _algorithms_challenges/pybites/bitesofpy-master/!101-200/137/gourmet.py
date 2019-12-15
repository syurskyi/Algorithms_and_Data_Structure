#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from itertools import product, groupby
from collections import Counter, namedtuple
import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]

WINE_LIST = {
    'red': RED_WINES,
    'white': WHITE_WINES,
    'sparkling': SPARKLING_WINES,
    'all': RED_WINES + WHITE_WINES + SPARKLING_WINES
}

Scores = namedtuple('Scores', 'wine cheese score')


def calculate_similarity(cheese, wine):
    wine_count = Counter(wine.lower())
    cheese_count = Counter(cheese.lower())
    common_letters = (wine_count & cheese_count)
    similarity = sum(common_letters.values()) / (1 + (len(wine) - len(cheese)) ** 2)
    return similarity


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    if wine_type in WINE_LIST:
        wines = WINE_LIST[wine_type]
    elif wine_type in WINE_LIST['all']:
        wines = [wine_type]
    else:
        raise ValueError('Wine not recognised')
    cheeses = CHEESES
    hi_score = Scores('', '', 0)
    for wine, cheese in product(wines, cheeses):
        similarity = calculate_similarity(cheese, wine)
        if similarity > hi_score.score:
            hi_score = Scores(wine, cheese, similarity)
    return tuple(hi_score)


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    scores = []
    for wine, cheese in product(WINE_LIST['all'], CHEESES):
        similarity = calculate_similarity(cheese, wine)
        scores.append(Scores(wine, cheese, similarity))
    scores = sorted(scores, key=lambda x: (x.wine, -x.score, x.cheese))
    res = []
    for k, g in groupby(scores, lambda x: x.wine):
        res.append((k, [rec.cheese for rec in g][:5]))
    return res
