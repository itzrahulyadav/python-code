from flask import Flask
import requests,jsonify

app = Flask(__name__)

@app.route("/")
def get_data():
     response = requests.get('https://v2.jokeapi.dev/joke/Any')
     if response.status_code == 200:
        data = response.json()
        return data['setup'] + " " + data['delivery']
     else:
        return "Joke not found"

if __name__ == '__main__':
    app.run()

