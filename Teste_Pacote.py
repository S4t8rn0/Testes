import json
pacot= list()

with open ('Projeto\Oi.json', 'r', encoding= 'utf-8') as openfile:
    pacot= json.load(openfile)

import PySimpleGUI as sg

layout= [
    [sg.Text('Nome'), sg.InputText()],
    [sg.Checkbox('Pequeno', key= 'Peq'), sg.Checkbox('Medio', key= 'Medio')],
    [sg.Button('Confirmar'), sg.Button('Cancel')]
]
window= sg.Window('Pacotes', layout)

while True:
    event, values= window.read()
    if event == 'Confirmar':
        pacot= str (print(f'O pacote {values [1] or values [2]} foi selecionado. Aproveite!'))
        pacot(dict(Nome= values[0], Pacotes= values['Pequeno'] or values['Medio']))
        with open ('Projeto\Oi.json', 'w', encoding= 'utf-8') as openfile:
            json.dump(pacot, openfile, ensure_ascii= False, indent='\t')

windows.close()