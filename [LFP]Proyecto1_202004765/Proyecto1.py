from os import system
from tkinter import *
from tkinter import ttk
import sched, time

from P1_OP1 import op1
from P1_OP2 import op2
from P1_OP3 import op3
 
class app():
    def __init__(self):
        root = Tk()

        root.title("Bitxelart")
        root.iconbitmap("favicon.ico")
        root.resizable(False,False)
        root.geometry("1000x635")
        root.configure(bg="#EFE95B")

        tabControl = ttk.Notebook(root)

        #********************************************* CARGAR ARCHIVO *********************************************
        tab1 = Frame(tabControl)
        tab1.config(bg="#EFE95B", width=1000, height=570)
        #Ruta
        Ruta = Label(tab1, text="", wraplength=890)
        Ruta.place(x=100,y=300)
        Ruta.configure(font=("Comic Sans MS", 16, "italic"),bg="#EFE95B")
        #Info
        Info = Label(tab1, text="Presione el boton y busque el archivo con extension .pxla que desea utilizar")
        Info.place(x=100,y=75)
        Info.configure(font=("Comic Sans MS", 16, "italic"),bg="#EFE95B")
        #Label 1
        La1 = Label(tab1, text="")
        La1.place(x=100,y=270)
        La1.configure(font=("Comic Sans MS", 16, "italic"),bg="#EFE95B")
        #Boton
        botonSeleccionar = Button(tab1, text="Cargar Archivo", command=lambda:op1.LeerArchivo(Ruta,La1,Ruta2))
        botonSeleccionar.place(x=400,y=150)
        botonSeleccionar.configure(font=("Comic Sans MS", 16, "italic"), background='#CB9F20')
        tabControl.add(tab1, text = 'Cargar Archivo')


        #********************************************* ANALIZAR ARCHIVO *********************************************
        tab2 = Frame(tabControl)
        tab2.config(bg="#EFE95B", width=1000, height=570)
        #Label 2
        La2 = Label(tab2, text="Ruta del archivo a analizar")
        La2.place(x=100,y=50)
        La2.configure(font=("Comic Sans MS", 16, "italic"),bg="#EFE95B")
        #Ruta 2
        Ruta2 = Label(tab2, text="", wraplength=890)
        Ruta2.place(x=100,y=90)
        Ruta2.configure(font=("Comic Sans MS", 16, "italic"),bg="#EFE95B")
        #Boton Analizar
        botonAnalizar = Button(tab2, text="Analizar Archivo", command=lambda:op2.AnalizarArchivo(Ruta2,myframe2,LTitulo1,LTitulo,img0,img1,img2,img3))
        botonAnalizar.place(x=400,y=200)
        botonAnalizar.configure(font=("Comic Sans MS", 16, "italic"), background='#CB9F20')
        tabControl.add(tab2, text = 'Analizar Archivo')


        #********************************************* Ver Reportes *********************************************
        tab3 = Frame(tabControl)
        tab3.config(bg="#EFE95B", width=1000, height=570)

        FDatos = Frame(tab3)
        FDatos.config(bg="#CFFA8C", width=976, height=160)
        FDatos.place(x=12,y=12)


        Label(FDatos, text='Reporte de tokens:',font=("Comic Sans MS", 16, "italic"),bg="#CFFA8C").place(x=12,y=17)
        Button(FDatos,text="Abrir",font=("Comic Sans MS", 16, "italic"),bg="#CB9F20",command=lambda:system('Lista_de_Tokens.html')).place(x=230,y=12)
        Label(FDatos, text='Reporte de errores:',font=("Comic Sans MS", 16, "italic"),bg="#CFFA8C").place(x=12,y=80)
        Button(FDatos,text="Abrir",font=("Comic Sans MS", 16, "italic"),bg="#CB9F20",command=lambda:system('Lista_de_Errores.html')).place(x=230,y=75)


        tabControl.add(tab3, text = 'Ver Reportes')

        #********************************************* Seleccionar Imagen *********************************************
        tab4 = Frame(tabControl)
        tab4.config(bg="#EFE95B", width=1000, height=570)

        #Label Titulo Imagen seleccionada
        LTitulo1 = Label(tab4, text="No se ha seleccionado una imagen", wraplength=500)
        LTitulo1.place(x=25,y=12)
        LTitulo1.configure(font=("Comic Sans MS", 16, "italic"),bg="#EFE95B")

        wrapper2 = LabelFrame(tab4, width=100, height=100)

        mycanvas2 = Canvas(wrapper2)
        mycanvas2.pack(side=LEFT, fill="y")

        yscrollbar = ttk.Scrollbar(wrapper2, orient="vertical", command=mycanvas2.yview)
        yscrollbar.pack(side=RIGHT, fill="y")

        botonAAA = Button(tab4, text="Seleccionar", command=lambda:self.act(LTitulo,img0,img1,img2,img3),font=("Comic Sans MS", 16, "italic"), background='#CB9F20')
        botonAAA.place(x=700,y=400)

        mycanvas2.configure(yscrollcommand=yscrollbar.set)
        mycanvas2.bind('<Configure>', lambda e: mycanvas2.configure(scrollregion = mycanvas2.bbox('all')))

        myframe2 = Frame(mycanvas2)
        myframe2.config(bg="#CFFA8C", width=1000, height=570)
        mycanvas2.create_window((0,0), window=myframe2, anchor="nw")
        mycanvas2.config(bg="#CFFA8C", width=400, height=400)
        wrapper2.place(x=250, y=100)
            

        #Button(tab4,text="Seleccionar",command=lambda: op3.selImagen(LTitulo,myframe2),font=("Comic Sans MS", 16, "italic"),bg="#CB9F20").place(x=700,y=500)

        tabControl.add(tab4, text = 'Seleccionar Imagen')

        #********************************************* Ver Imagen *********************************************
        tab5 = Frame(tabControl)
        tab5.config(bg="#EFE95B", width=1000, height=570)
        tabimg = Canvas(tab5,width=700,height=550, bg="black")



        #Label Titulo Imagen seleccionada
        LTitulo = Label(tab5, text="", wraplength=258)
        LTitulo.place(x=12,y=12)
        LTitulo.configure(font=("Comic Sans MS", 16, "italic"),bg="#EFE95B")

        titulo=LTitulo.cget("text")
        try:
            img0=PhotoImage(file=titulo+'.png')
        except:
            img0=PhotoImage(file='..png')
        try:
            img1=PhotoImage(file=titulo+'[MX].png')
        except:
            img1=PhotoImage(file='..png')
        try:
            img2=PhotoImage(file=titulo+'[MY].png')
        except:
            img2=PhotoImage(file='..png')
        try:
            img3=PhotoImage(file=titulo+'[MXY].png')
        except:
            img3=PhotoImage(file='..png')
        


        #Boton Normal
        botonMO = Button(tab5, text="Original",font=("Comic Sans MS", 16, "italic"), background='#CB9F20', command=lambda:op3.Original(tabimg,img0),width=14)
        botonMO.place(x=50,y=175)
        #Boton MX
        botonMX = Button(tab5, text="MIRRORX", command=lambda:op3.MX(tabimg,img1),font=("Comic Sans MS", 16, "italic"), background='#CB9F20',width=14)
        botonMX.place(x=50,y=250)
        #Boton MY
        botonMY = Button(tab5, text="MIRRORY", command=lambda:op3.MY(tabimg,img2),font=("Comic Sans MS", 16, "italic"), background='#CB9F20',width=14)
        botonMY.place(x=50,y=325)
        #Boton MX
        botonMD = Button(tab5, text="DOUBLEMIRROR", command=lambda:op3.MXY(tabimg,img3),font=("Comic Sans MS", 16, "italic"), background='#CB9F20')
        botonMD.place(x=50,y=400)


        tabControl.add(tab5, text = 'Ver Imagen')
        tabControl.place(x=0,y=0)
        tabimg.place(x=290,y=12)
        #Boton Salir
        botonSeleccionar = Button(root, text="Salir", command=lambda:exit())
        botonSeleccionar.place(x=950,y=600)
        botonSeleccionar.configure(font=("Comic Sans MS", 10, "italic"), background='red')

        root.mainloop()

    def act(self,LTitulo,img0,img1,img2,img3):
        titulo=LTitulo.cget("text")
        try:
            img0.configure(file=titulo+'.png')
        except:
            img0.configure(file='..png')
        try:
            img1.configure(file=titulo+'[MX].png')
        except:
            img1.configure(file='..png')
        try:
            img2.configure(file=titulo+'[MY].png')
        except:
            img2.configure(file='..png')
        try:
            img3.configure(file=titulo+'[MXY].png')
        except:
            img3.configure(file='..png')

ap=app()
