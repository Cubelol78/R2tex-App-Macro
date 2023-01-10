from tkinter import *
import tkinter
from tkinter import filedialog
import tkinter as tk

class File():
    def choose_file():
            # Crée une fenêtre "Ouvrir"
            root = tk.Tk()
            root.withdraw()

            # Affiche la boîte de dialogue "Ouvrir"
            file_path = filedialog.askopenfilename()

            # Retourne l'emplacement du fichier sélectionné
            return file_path