print('/==========\ ')
print('|R2tex Corp|')
print('\==========/')
#Import
print("|===================/")
print("|=====|Import|=====/")
print("|=================/")

print("Import de tKinter") 
import tkinter
from tkinter import *

print("Importation des Macro")
from Macro.GTA5 import *

#|=====================/
#|=====|Variable|=====/
#|===================/
pl = 1
CouleurBackgroundSombre = "#333333"
CouleurBackgroundClair = "#666666"
CouleurBackgroundSuperClair = "#8D8D8D"
White = "#FFFFFF"

#Macro
print('|==================/')
print('|=====|Macro|=====/')
print('|================/')

#Crée une fenétre

print('[Création de la fenétre]')
Fenetre = tkinter.Tk()

print("Ajoute un titre")
Fenetre.title('Macro')

print("Mise a l'échelle 400x720 Pixel")
Fenetre.geometry("400x720")
Fenetre.maxsize(400,720)
Fenetre.minsize(400,720)

print("Modification de l'icon")
Fenetre.iconbitmap("IMG/R2tex.ico")

print("Configuration de la fenétre")
Fenetre.config(
    bg = CouleurBackgroundClair,
    cursor= "arrow"
    )

while True:
#Frame
    #Menu Principale
    print("Définition du Menu principale")
    def MainMenu():
        ClearWindows()
        MainMenu_Titre.pack()
        MainMenu_Bouton_MenuGTA5.pack()
        MainMenu_Bouton_Coupe_co.pack()
    #GTA5 Menu
    print("Définition du Menu GTA5")
    def GTA5Menu():
        ClearWindows()
        GTA5Menu_Titre.pack()
        GTA5Menu_Boutton_Main.pack()
    #Remise a zéro
    def ClearWindows():
        #Main Menu
        MainMenu_Bouton_MenuGTA5.pack_forget()
        MainMenu_Titre.pack_forget()
        #Menu GTA5
        GTA5Menu_Boutton_Main.pack_forget()
        GTA5Menu_Titre.pack_forget()
        MainMenu_Bouton_Coupe_co.pack_forget()
#définition des page

    #MainMenu
    GTA5IMG = PhotoImage( file= "./IMG/gta5-200x-.png" )
    MainMenu_Bouton_MenuGTA5 = tkinter.Button (Fenetre,
        text= 'GTA 5',
        image= GTA5IMG,
        command= GTA5Menu,
        activebackground='#8D8D8D',
        background= "#666666",
        borderwidth= 5,
        overrelief= SUNKEN,
        cursor= ''
    )
    MainMenu_Titre = tkinter.Label (Fenetre,
        text='Macro',
        background= CouleurBackgroundSombre,
        font=( "Impact", 30, UNDERLINE ),
        height= 0,
        width= 30,
    )
    MainMenu_Bouton_Coupe_co = tkinter.Button (Fenetre,
        text= "Selectionner l'emplacement de votre fichier [GTA5.exe]",
        command= GTA5.CoupeCo(),
        activebackground='#8D8D8D',
        background= "#666666",
        borderwidth= 5,
        overrelief= SUNKEN,
        cursor= ''
    )

    #GTA5Menu
    GTA5Menu_Titre = tkinter.Label (Fenetre,
        text = 'GTA 5',
        background= CouleurBackgroundSombre,
        font=( "Impact", 30, UNDERLINE ),
        height= 0,
        width= 30,
    )
    GTA5Menu_Boutton_Main = tkinter.Button (Fenetre,
        text = 'Retour',
        command = MainMenu,
        background= CouleurBackgroundSuperClair,
        activebackground= CouleurBackgroundSombre,
        activeforeground= White,
        borderwidth= 2,
        overrelief= SUNKEN,
    )

    #premier lancement
    if ( pl == 1 ):
        MainMenu()
        pl = 0

#Empéche la fenétre de se fermer
    Fenetre.mainloop()