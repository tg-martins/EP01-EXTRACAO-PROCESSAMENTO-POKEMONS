import pandas as pd
import json


def extract_name_from_url(url):
    url_items = url.split('/')
    if len(url_items) > 0:
        name = url_items[len(url_items) - 1].split('.')
        if len(name) > 0:
            return name[0]
    raise Exception('name not found')


pokemons = []

with open('pokemons.json') as file:
    for pokemon_json in json.load(file):
        pokemon = {
            'number': pokemon_json['number'].replace('#', ''),
            'name': pokemon_json['name'],
            'height': pokemon_json['height'],
            'weight': pokemon_json['weight'],
            'types': '',
            'next_evolution': '',
            'damage_normal': 0,
            'damage_fire': 0,
            'damage_water': 0,
            'damage_electric': 0,
            'damage_grass': 0,
            'damage_ice': 0,
            'damage_fighting': 0,
            'damage_poison': 0,
            'damage_ground': 0,
            'damage_flying': 0,
            'damage_psychict': 0,
            'damage_bug': 0,
            'damage_rock': 0,
            'damage_ghost': 0,
            'damage_dragon': 0,
        }

        name_types = []

        for type_url in pokemon_json['types']:
            try:
                name_types.append(extract_name_from_url(type_url))
            except:
                pass

        pokemon['types'] = str.join(';', name_types)

        for damage_url, damage_value in pokemon_json['damage_takens'].items():
            try:
                pokemon[f'damage_{extract_name_from_url(damage_url)}'] = damage_value.replace(
                    '*', '')
            except:
                pass

        try:
            pokemon['next_evolution'] = extract_name_from_url(
                pokemon_json['next_evolution'])
        except:
            pass

        pokemons.append(pokemon)

df = pd.DataFrame(pokemons)
df.to_csv('pokemons.csv', index=False, header=False)
