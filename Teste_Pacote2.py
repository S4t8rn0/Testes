import json

pacot= list()

with open('Projeto\Uii.json' , 'r' , encoding= 'utf-8') as openfile:
    pacot= json.load(openfile)

import PySimpleGUI as sg

layout= [
    [sg.Text('Pacotes')],
    [sg.Text('Nome'), sg.InputText(k='nome')],
    [sg.Text('Temos os seguintes tamanhos dos pacotes:')],
    [sg.Text('M- 6 sessões/aplicações')],
    [sg.Text('G- 9 sessões/aplicações')],
    [sg.Checkbox('M', key= 'Medio'), sg.Checkbox('G', key= 'Grande')],
    [sg.Button('Confirmar'), sg.Button('Cancel')]
    ]
window= sg.Window('Pacotes')
    
while True:
    event, values= window.read()

    if event == 'Confirmar':
        pacot.append(dict(Pacote= values['Medio'] or values['Grande'], Paciente= values[0]))

        with open('Uii.json', 'w', encoding= 'utf-8') as openfile:
            json.dump(pacot, openfile, ensure_ascii= False, indent= '\t')

        sg.popup ('Seu pacote foi selecionado. Agora é só aproveita-ló.')
        break

    
    #JANELA7: Windows close.
    if  event== sg.WINDOW_CLOSED or 'Cancel':
        sg.popup_yes_no('Tem certeza que deseja fechar?')
        if event == 'yes':
            print('Ok')
            break
        if event == 'no':
            layout()