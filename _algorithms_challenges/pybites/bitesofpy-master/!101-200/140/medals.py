from os import path
from urllib.request import urlretrieve
import pandas as pd
from itertools import chain

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def load_data(data):
    dt_file = path.join('/tmp', data.split('/')[-1])
    if not path.isfile(dt_file):
        urlretrieve(data, dt_file)
    with open(dt_file, 'r') as f:
        return pd.read_csv(f)


def athletes_most_medals(data=data):
    csv = load_data(data)
    df = csv.groupby(['Gender', 'Athlete'])['Medal'].count()
    male = df.loc['Men'].nlargest(1)
    female = df.loc['Women'].nlargest(1)
    return {r[0]: r[1] for r in chain(male.items(),female.items())}
