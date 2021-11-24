from tkinter import *
from tkinter import ttk
from tkinter import filedialog as FileDialog

class op1:
    def LeerArchivo(Ruta,La1,Ruta2):
        #Utilizando fliedialog de tkinter para abrir un archivo
        ruta=FileDialog.askopenfilename(title="Abrir un fichero")
        Ruta.configure(text=ruta)
        Ruta2.configure(text=ruta)
        La1.configure(text='Ruta a utilizar:')