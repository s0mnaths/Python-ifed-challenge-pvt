import PySimpleGUI as sg
from pokedexFunc import pokeType,ability,TypeDoubleDmg,DoubleDmg5 

sg.theme('DarkBlue')
layout = [[sg.Text("Enter Pokemon Name: ")],
          [sg.Input(size=(35,1),key='-INPUT-')],
          [sg.Text(size=(35,3), key='-Type-')],
          [sg.Text(size=(35,2), key='-DDF-')],
          [sg.Text(size=(35,7), key='-DDP-')],
          [sg.Text(size=(35,8), key='-ABILITIES-')],
          [sg.Button('Get Details'), sg.Button('Quit')]]

window = sg.Window('POKEDEX', layout, alpha_channel=0.95)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    typeName=pokeType(values['-INPUT-'].lower())
    double_damage_from=TypeDoubleDmg(typeName)
    DoubleDamagePoksList=DoubleDmg5(double_damage_from)
    doubleDamagePoks='\n--> '.join([str(i).upper() for i in DoubleDamagePoksList])
    abilitiesList=ability(values['-INPUT-'].lower())
    abilities='\n--> '.join([str(i).upper() for i in abilitiesList])

    window['-Type-'].update('\nType: '+typeName.upper())
    window['-DDF-'].update('Double Damage from type: '+double_damage_from.upper())
    window['-DDP-'].update(f'Double Damage from pokemons:\n--> {doubleDamagePoks}')
    window['-ABILITIES-'].update(f'Abilities:\n--> {abilities}')


window.close()