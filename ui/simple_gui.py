import random

import PySimpleGUI as sg

sg.theme('HotDogStand')  # Add a touch of color
# All the stuff inside your window.
operators = ["+", "-", "*", "/"]
layout = [[sg.Text("adding values")],
          [sg.Text('Enter first VALUE'), sg.InputText(key="a", enable_events=True), sg.Text('Enter second VALUE'),
           sg.InputText(key="b")],
          [sg.Text('Result'), sg.Text("", key="result")],
          [sg.Button('Ok'), sg.Button('Cancel'),
           sg.Combo(values=["+", "-"], default_value="+", key="combo", enable_events=True)]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == "Ok":
        operator = values['combo']
        window['result'].update(eval(f"{values['a']} {operator} {values['b']}"))
        print('Output is:', float(values["a"]) + float(values["b"]))

window.close()
