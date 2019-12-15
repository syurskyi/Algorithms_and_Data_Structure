import json

from quotes import app

API_ENDPOINT = 'http://127.0.0.1:5000/api/quotes'

client = app.test_client()
client.testing = True


def test_get_quotes():
    response = client.get(API_ENDPOINT)
    assert response.status_code == 200

    data = json.loads(response.get_data())
    quotes = data['quotes']
    assert len(quotes) == 3

    expected = {'id': 1, 'movie': 'The Godfather',
                'quote': "I'm gonna make him an offer he can't refuse."}
    assert quotes[0] == expected


def test_get_existing_quote():
    response = client.get(API_ENDPOINT + '/2')
    assert response.status_code == 200

    data = json.loads(response.get_data())
    quotes = data['quotes']
    assert len(quotes) == 1

    expected = {'id': 2, 'movie': 'Predator', 'quote': "Get to the choppa!"}
    assert quotes[0] == expected


def test_get_not_existing_quote():
    response = client.get(API_ENDPOINT + '/4')
    assert response.status_code == 404


def test_create_quote():
    new_quote = dict(quote='You talking to me?',
                     movie='Taxi driver')
    response = client.post(API_ENDPOINT,
                           data=json.dumps(new_quote),
                           content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.get_data())
    new_quote = data['quote']
    assert new_quote['id'] == 4
    assert new_quote['quote'] == 'You talking to me?'
    assert new_quote['movie'] == 'Taxi driver'


def test_create_quote_missing_data():
    new_quote = {}
    response = client.post(API_ENDPOINT,
                           data=json.dumps(new_quote),
                           content_type='application/json')
    assert response.status_code == 400


def test_create_quote_imcomplete_data():
    new_quote = dict(quote='You talking to me?')
    response = client.post(API_ENDPOINT,
                           data=json.dumps(new_quote),
                           content_type='application/json')
    assert response.status_code == 400


def test_create_existing_quote():
    new_quote = dict(quote='You talking to me?',
                     movie='Taxi driver')
    response = client.post(API_ENDPOINT,
                           data=json.dumps(new_quote),
                           content_type='application/json')
    assert response.status_code == 400


def test_update_quote():
    update_quote = dict(quote='You talking to me?!',
                        movie='Taxi driver (1976)')
    response = client.put(API_ENDPOINT + '/4',
                          data=json.dumps(update_quote),
                          content_type='application/json')
    assert response.status_code == 200

    data = json.loads(response.get_data())
    updated_quote = data['quote']
    assert updated_quote['id'] == 4
    assert updated_quote['quote'] == 'You talking to me?!'
    assert updated_quote['movie'] == 'Taxi driver (1976)'


def test_update_no_data():
    update_quote = {}
    response = client.put(API_ENDPOINT + '/4',
                          data=json.dumps(update_quote),
                          content_type='application/json')
    assert response.status_code == 400


def test_update_not_existing_quote():
    update_quote = dict(quote='You talking to me?!')
    response = client.put(API_ENDPOINT + '/5',
                          data=json.dumps(update_quote),
                          content_type='application/json')
    assert response.status_code == 404


def test_update_no_changes():
    update_quote = dict(quote='Get to the choppa!',
                        movie='Predator')
    response = client.put(API_ENDPOINT + '/2',
                          data=json.dumps(update_quote),
                          content_type='application/json')
    assert response.status_code == 200

    data = json.loads(response.get_data())
    updated_quote = data['quote']
    assert updated_quote['id'] == 2
    assert updated_quote['quote'] == 'Get to the choppa!'
    assert updated_quote['movie'] == 'Predator'


def test_delete_existing_quote():
    response = client.delete(API_ENDPOINT + '/2')
    assert response.status_code == 204

    # number quotes from 4 to 3
    response = client.get(API_ENDPOINT)
    data = json.loads(response.get_data())
    quotes = data['quotes']
    assert len(quotes) == 3


def test_delete_not_existing_quote():
    response = client.delete(API_ENDPOINT + '/5')
    assert response.status_code == 404