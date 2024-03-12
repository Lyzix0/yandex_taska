import requests
from flask import make_response, jsonify

from main import app


assert requests.get('http://127.0.0.1:8080/api/v2/users/1').json()
assert requests.get('http://127.0.0.1:8080/api/v2/users').json()

assert requests.post('http://127.0.0.1:8080/api/v2/users',
                     json={'surname': 'maxim', 'name': 'bebra', 'password': '121223'}).json()
