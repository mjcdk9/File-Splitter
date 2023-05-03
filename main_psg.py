# img_viewer.py
import logging
import threading
import time
import PySimpleGUI as sg
from main import *
# from main import extract_top_5, input_file, output_folder, split_csv_file, status



def thread_function(name):
    print("thread start")
    logging.info("Thread %s: starting", name)
    extract_top_5(values["-PATH-"], output_folder, 5)
    print("thread stop")
    time.sleep(2)
    logging.info("Thread %s: finishing", name)










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
    [sg.Button("Short File Splitter", key="-HEADSPLIT-"),
    sg.Button("Large file splitter", key="-MULTISPLIT-")],
    # [sg.Input(key="-Number of rows per file-")],

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
    # print(values["-Path-"])
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-HEADSPLIT-":
        status = "Loading..."
        window["-STATUS-"].update(status)
        event == "-HEADSPLIT-"
        print(values["-PATH-"])
        print("headsplit")
        x = threading.Thread(target=thread_function, args=(1,))
        x.start()
        # extract_top_5(values["-PATH-"], output_folder, 5)
        status = "Complete"
        window["-STATUS-"].update(status)

    elif event == "-MULTISPLIT-":
        status = "Loading..."
        window["-STATUS-"].update(status)
        print(values["-PATH-"])
        print("multisplit")
        split_csv_file(values["-PATH-"], output_folder, 50)
        status = "Complete"
        window["-STATUS-"].update(status)
