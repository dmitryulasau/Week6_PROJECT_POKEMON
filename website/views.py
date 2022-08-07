from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import User, Pokemon
from . import db
import requests

views = Blueprint('views', __name__)

# GETTING POKEMON INFO
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name')
        
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
        print(response)

        if not response.ok:
            flash("Please enter a valid name or number (1-905)", category='error')
            return render_template('home.html')
        if not response.json():
            flash("An Unexpected Error Occurred", category='warning ')
            return render_template('home.html')

        data = response.json()
        pokemon_info = []
        pokemon_dict = {}
        pokemon_dict = {
            'name': data['name'],
            'ability': data['abilities'][0]['ability']['name'],
            'defense': data['stats'][2]['base_stat'],
            'attack': data['stats'][1]['base_stat'],
            'hp': data['stats'][0]['base_stat'],
            'image': data['sprites']['other']['official-artwork']['front_default'],
            'gif': data['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
        }
 
        pokemon_info.append(pokemon_dict)
        
        return render_template('home.html', info=pokemon_info, user=current_user)

    return render_template("home.html", user=current_user)


# @views.route('/register', methods=['GET', 'POST'])
# def pokemon_add():
#     if request.method == 'POST':

