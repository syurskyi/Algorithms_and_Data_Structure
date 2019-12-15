import json

import pytest

from Previous.jsonify import convert_to_json


@pytest.fixture(scope="module")
def output():
    return convert_to_json()


def test_return_type(output):
    assert type(output) == str


def test_extracted_data_is_correct(output):
    data = json.loads(output)
    assert type(data) == list
    assert len(data) == 10
    for row in [{'id': '1', 'first_name': 'Junie', 'last_name': 'Kybert',
                 'email': 'jkybert0@army.mil'},
                {'id': '2', 'first_name': 'Sid', 'last_name': 'Churching',
                 'email': 'schurching1@tumblr.com'},
                {'id': '3', 'first_name': 'Cherry', 'last_name': 'Dudbridge',
                 'email': 'cdudbridge2@nifty.com'},
                {'id': '4', 'first_name': 'Merrilee', 'last_name': 'Kleiser',
                 'email': 'mkleiser3@reference.com'},
                {'id': '5', 'first_name': 'Umeko', 'last_name': 'Cray',
                 'email': 'ucray4@foxnews.com'},
                {'id': '6', 'first_name': 'Jenifer',
                 'last_name': 'Dale', 'email': 'jdale@hubpages.com'},
                {'id': '7', 'first_name': 'Deeanne', 'last_name': 'Gabbett',
                 'email': 'dgabbett6@ucoz.com'},
                {'id': '8', 'first_name': 'Hymie', 'last_name': 'Valentin',
                 'email': 'hvalentin7@blogs.com'},
                {'id': '9', 'first_name': 'Alphonso', 'last_name':
                 'Berwick', 'email': 'aberwick8@symantec.com'},
                {'id': '10', 'first_name': 'Wyn', 'last_name': 'Serginson',
                 'email': 'wserginson9@naver.com'}]:
        assert row in data, f'{row} not in output of convert_to_json'