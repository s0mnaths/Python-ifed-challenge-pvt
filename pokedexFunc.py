#! python3
# pokedexFunc.py

import requests,json

def pokeType(pokeName):
    '''Returns the type of pokemon passed in arguments

    PARAMETERS:
    -----------
    pokeName : string
        Name of the pokemon

    RETURNS:
    ----------
    typeName : string
        Type of the pokemon 
    '''

    response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokeName)
    response.raise_for_status()
    pikachuData=response.json()
    typeData=pikachuData['types'][0]
    typeName=typeData['type']['name']
    return typeName

def TypeDoubleDmg(typeName):
    '''Returns the pokemon type which gives 2x damage to the type passed in arguments

    PARAMETERS:
    -----------
    typeName : string
        Type of pokemon

    RETURNS:
    -----------
    double_damage_from: string
        Type of pokemon which gives 2x damage to pokeName
    '''
    
    response=requests.get("https://pokeapi.co/api/v2/type/"+typeName)
    pikachuData=response.json()
    damageData=pikachuData['damage_relations']
    double_damage_from=damageData['double_damage_from'][0]['name']
    return double_damage_from

def DoubleDmg5(double_damage_from):
    '''Returns the list of five pokemons of the type passed in arguments

    PARAMETERS:
    -----------
    double_damage_from : string
        Type of pokemon

    RETURNS:
    ------------
    DDF : list
        Names of five pokemon of type double_damage_from, in a list
    '''

    response=requests.get("https://pokeapi.co/api/v2/type/"+double_damage_from)
    response.raise_for_status()
    typeData=response.json()
    pikachuData=typeData['pokemon']
    DDF=[]
    for i in range(5):
        DDF.append(pikachuData[i]['pokemon']['name'])
    return DDF

def ability(pokeName):
    '''Returns the list of abilities of the pokemon passed in arguments

    PARAMETERS:
    -----------
    pokeName : string
        Name of pokemon

    RETURNS:
    ------------
    abilities : list
        All abilities of pokeName, in a list
    '''

    response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokeName)
    response.raise_for_status()
    pikachuData=response.json()
    abilitiesData=pikachuData['abilities']
    abilities=[]
    for ability in  abilitiesData:
        abilities.append(ability['ability']['name'])
    return abilities