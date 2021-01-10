import requests,json

def ability(pokeName):
    response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokeName)
    response.raise_for_status()
    pikachuData=response.json()
    abilitiesData=pikachuData['abilities']
    abilities=[]
    for ability in  abilitiesData:
        abilities.append(ability['ability']['name'])
    return abilities
