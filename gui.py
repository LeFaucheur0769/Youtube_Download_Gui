import PySimpleGUI as sg
import download
import os.path


# First the window layout in 2 columns
def gui():

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Youtube video downloader')],
                [sg.Text('Paste the url here : '), sg.Multiline(size=(30, 5), key='textbox')],# identify the multiline via key option
                [sg.Button('Ok'), sg.Button('Close Window')]    ]

    # Create the Window
    window = sg.Window('Test', layout).Finalize()
    #window.Maximize()
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Close Window'): # if user closes window or clicks cancel
            break
        return((values['textbox']).split())  # get the content of multiline via its unique key
    window.close()