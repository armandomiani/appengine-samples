from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def main():
    return jsonify(data={
        'host': request.host,
        'httpResponse': __fetch_get_request()
    })


def __fetch_get_request():
    import json
    import requests    
    from requests_toolbelt.adapters import appengine
    appengine.monkeypatch()

    response = requests.get('https://api.openbrewerydb.org/breweries/5494')
    return json.loads(response.text)   