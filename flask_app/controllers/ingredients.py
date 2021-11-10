import requests
from flask import flash
from flask_app import app
from flask import render_template, redirect, request, session, jsonify
# from flask_app.models.ingredient import ingredient
import os

# os.environ.get("FLASK_APP_API_KEY")

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route('/search', methods=['POST'])
def search():
    # print(request.form['item'])
    url= 'https://www.bon-api.com/api/v1/ingredient/alternatives'
    headers= {
        'authorization': f'Token {os.environ.get("FLASK_APP_API_KEY")}',
        'content-type': 'application/json'
    }
    print(request.form['item'])
    payload= {
        "ingredients": [f'{request.form["item"]}']
    }
    # 'ingredients': [f'{request.form["amount"]}{request.form["measurement"]} {request.form["item"]}']
    # now we inject the query into our string
    r = requests.post(url, headers=headers, data=payload)
    # we must keep in line with JSON format.
    # requests has a method to convert the data coming back into JSON.
    print(r.status_code)
    print(r.text)
    return jsonify( r.json() )