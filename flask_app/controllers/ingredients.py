import requests
from flask import flash
from flask_app import app
from flask import render_template, redirect, request, session, jsonify
from flask_app.models.ingredient import ingredient
import os

@app.route('/get_data')
def get_data():
    # jsonify will serialize data into JSON format.
    return jsonify(message="Hello World")
