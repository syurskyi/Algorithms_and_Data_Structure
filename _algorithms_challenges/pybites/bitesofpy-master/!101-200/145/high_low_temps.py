import csv
import os
import re
import urllib.request
from collections import namedtuple
from datetime import datetime

import pandas as pd

DATA_FILE = "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")

TMP = '/tmp'
LOCAL_FILE = os.path.join('/tmp', 'weather-ann-arbor.csv')
if not os.path.isfile(LOCAL_FILE):
    urllib.request.urlretrieve(DATA_FILE, LOCAL_FILE)


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    with open(LOCAL_FILE) as f:
        the_data = sorted([{
            'id': x['ID'],
            'date': datetime.strptime(x['Date'], '%Y-%m-%d').date(),
            'element': x['Element'],
            'value': int(x['Data_Value'])
        } for x in csv.DictReader(f) if not re.match(r'\d{4}-02-29', x['Date'])],
            key=lambda x: (x['id'] + x['date'].strftime('%m%d%Y')))
    dataset = [{'id': x['id'],
                'monthday': x['date'].strftime('%m%d'),
                'year': x['date'].year,
                'element': x['element'],
                'value': x['value']
                } for x in the_data]

    data_before_2015_left = pd.DataFrame(x for x in dataset if x['year'] < 2015 and x['element'] == 'TMIN').drop(
        ['element', 'year'], axis=1).set_index(['id', 'monthday']).groupby(
        ['id', 'monthday']).min(level='monthday').rename(columns={'value': 'mina'})

    data_before_2015_right = pd.DataFrame(x for x in dataset if x['year'] < 2015 and x['element'] == 'TMAX').drop(
        ['element', 'year'], axis=1).set_index(['id', 'monthday']).groupby(
        ['id', 'monthday']).max(level='monthday').rename(columns={'value': 'maxa'})

    early_dataset = data_before_2015_left.join(data_before_2015_right, lsuffix='_l', rsuffix='_r')

    data_for_2015_left = pd.DataFrame(x for x in dataset if x['year'] == 2015 and x['element'] == 'TMIN').drop(
        ['element', 'year'], axis=1).set_index(['id', 'monthday']).groupby(
        ['id', 'monthday']).max(level='monthday').rename(columns={'value': 'minb'})

    data_for_2015_right = pd.DataFrame(x for x in dataset if x['year'] == 2015 and x['element'] == 'TMAX').drop(
        ['element', 'year'], axis=1).set_index(['id', 'monthday']).groupby(
        ['id', 'monthday']).max(level='monthday').rename(columns={'value': 'maxb'})

    late_dataset = data_for_2015_left.join(data_for_2015_right)

    compare_set = early_dataset.join(late_dataset)

    result = {'min': [], 'max': []}
    for row in compare_set.itertuples():
        if row.mina > row.minb:
            result['min'].append(
                STATION(row.Index[0], datetime.strptime(f'2015{row.Index[1]}', '%Y%m%d').date(), row.minb / 10.0))
        if row.maxa < row.maxb:
            result['max'].append(
                STATION(row.Index[0], datetime.strptime(f'2015{row.Index[1]}', '%Y%m%d').date(), row.maxb / 10.0))

    return max(result['max'], key=lambda x: x.Value), min(result['min'], key=lambda x: x.Value)
