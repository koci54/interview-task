import requests
import xmltodict
import flask
from flask import jsonify
import urllib

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# ideally, this should come from and environment variable
API_KEY="3b5b3beb"

@app.route("/", methods=['GET'])
def index():
    return "Implemented route: /api/v1/movies/<title>"

@app.route("/api/v1/movies/<title>", methods=['GET'])
def get_movie_by_title(title):
    
    # proxy the request to remote xml api
    res = remote_req(str(title))
    
    # send the req to the remote xml API and return a json
    return jsonify(xmltodict.parse(res.content))

def remote_req(title):
    return requests.get(get_url(title))
    
def get_url(title):
    
    url = "http://www.omdbapi.com/?"
    
    # query params
    url += urllib.parse.urlencode({
        "t": title,
        "r": "xml",
        "apikey": API_KEY
    })
    return url

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5001")