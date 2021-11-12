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

# Retrieves Substitutes
@app.route('/search', methods=['POST'])
def search():
    # print(request.form['item'])
    url= f'https://api.spoonacular.com/food/ingredients/substitutes?apiKey={os.environ.get("FLASK_APP_API_KEY")}&ingredientName={request.form["item"]}'
    headers= {
        'Content-Type': 'application/json'
    }
    print(request.form['item'])
    # now we inject the query into our string
    r = requests.get(url, headers=headers)
    # we must keep in line with JSON format.
    # requests has a method to convert the data coming back into JSON.
    print(r.status_code)
    print(r.text)
    return jsonify( r.json() )

# Retrieves Autocomplete in Searchbar
@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    # print(request.form['item'])
    url= f'https://api.spoonacular.com/food/products/suggest?apiKey={os.environ.get("FLASK_APP_API_KEY")}&query={request.form["item"]}&number=5'
    headers= {
        'Content-Type': 'application/json'
    }
    print(request.form['item'])
    # now we inject the query into our string
    r = requests.get(url, headers=headers)
    # we must keep in line with JSON format.
    # requests has a method to convert the data coming back into JSON.
    print(r.status_code)
    print(r.text)
    return jsonify( r.json() )