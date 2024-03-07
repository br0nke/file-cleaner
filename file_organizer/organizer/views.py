from django.shortcuts import render
import tkinter
import PySimpleGUI as sg
from .utils import organize_files

def file_organizer(request):
    layout = [
        [sg.Text("Select a folder to organize:")],
        [sg.Input(), sg.FolderBrowse()],
        [sg.Button("Organize")],
    ]

    window = sg.Window("File Organizer", layout)
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # Handle window closing
        window.close()
        return render(request, 'organizer/index.html')

    if event == 'Organize' and values[0]:
        selected_folder = values[0]
        # Call your file organization function (explained in step 3)
        organize_files(selected_folder)
        window.close()
        return render(request, 'organizer/success.html', {'folder': selected_folder})

    window.close()
    return render(request, 'organizer/index.html')
