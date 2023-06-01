# img_viewer.py
import logging
import threading
import time
import PySimpleGUI as sg
from main import *
# from main import extract_top_5, input_file, output_folder, split_csv_file, status


# First the window layout in 2 columns

file_list_column = [
        [sg.Text("File "),
        # sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
        sg.Input(key="-PATH-", change_submits=True),
        sg.FileBrowse(key="-FILE-", change_submits=True)],
        [sg.Text(status, key="-STATUS-")],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an option below:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text("Enter number of rows per file"),
    sg.Input(key="-IN-")],
    [sg.Text("Select output folder path"),
    sg.Input(key="-OutputPath-", change_submits=True),
    sg.FolderBrowse(key="-OutputFolder-", change_submits=True)],
    [sg.Button("Short File Splitter", key="-HEADSPLIT-"),
    sg.Button("Large file splitter", key="-MULTISPLIT-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("File Browser", layout)


while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-HEADSPLIT-":
        status = "Loading..."
        window["-STATUS-"].update(status)
        event == "-HEADSPLIT-"
        print(values["-PATH-"])
        print("headsplit")
        status = "Splitting file"
        extract_top_5(values["-PATH-"], values["-OutputPath-"], 5)
        status = "Complete"
        window["-STATUS-"].update(status)
        time.sleep(3)
        window.close()

    elif event == "-MULTISPLIT-":
        status = "Loading..."
        window["-STATUS-"].update(status)
        print(values["-PATH-"])
        print("multisplit")
        split_csv_file(values["-PATH-"], values["-OutputPath-"], int(values["-IN-"]))
        status = "Complete"
        window["-STATUS-"].update(status)
        time.sleep(3)
        window.close()
