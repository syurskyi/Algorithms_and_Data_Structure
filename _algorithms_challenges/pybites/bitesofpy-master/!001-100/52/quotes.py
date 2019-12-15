from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    return [q for q in quotes if q['id'] == qid]


def _quote_exists(existing_quote):
    """Recommended helper"""
    return any(q['quote'] == existing_quote['quote'] and q['movie'] == existing_quote['movie'] for q in quotes)


def _new_id():
    return max(q['id'] for q in quotes) + 1


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes=quotes)


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    q = _get_quote(qid)
    if len(q) == 0:
        abort(404)
    return jsonify(quotes=q)


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    quote_str = request.json.get('quote')
    movie_str = request.json.get('movie')
    if not quote_str or not movie_str:
        abort(400)
    quote = {'quote': quote_str, 'movie': movie_str}
    if _quote_exists(quote):
        abort(400)
    quote['id'] = _new_id()
    quotes.append(quote)
    return jsonify(quote=quote), 201, {'Location': f'/api/quotes/{quote["id"]}'}


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    q = _get_quote(qid)
    if len(q) == 0:
        abort(404)
    q = q[0]
    dirty = False
    quote_str = request.json.get('quote')
    if quote_str:
        q['quote'] = quote_str
        dirty = True
    movie_str = request.json.get('movie')
    if movie_str:
        q['movie'] = movie_str
        dirty = True
    if not dirty:
        abort(400)
    return jsonify(quote=q), 200


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    q = _get_quote(qid)
    if len(q) == 0:
        abort(404)
    q = q[0]
    quotes.remove(q)
    return jsonify(quotes=q), 204
