from os import environ, system
from tkinter import *
from tkinter import ttk
from AnalizadorLexico import AnalizadorLexico
from AnalizadorTitulo import AnalizadorLexicoT
from Obj_Imagen import Imagen
from tkinter import messagebox
from html2image import Html2Image


imagen=[]
LNombre=[]
LFiltros=[]


def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

class op2:
    def AnalizarArchivo(ruta,myframe2,lt,ltt,img0,img1,img2,img3):
        #Leemos la ruta
        archivo=ruta.cget("text")
        if archivo!='':
            cadena = leerArchivo(archivo)

            #Instanciamos un nuevo analizador lexico o scanner
            scanner = AnalizadorLexico()

            #Enviamos la cadena a analizar
            scanner.analizar(cadena)
            
            lista=scanner.impTokens()
            listaE=scanner.impErrores()

            list=[]
            lis=[]
            l=[]
            ll=[]
            filtros=[]
            #entre corchetes
            sl=False
            #entre llaves
            ssl=False
            fil=False
            for i in lista:
                if i.enviarData()[0] in ['=',';',','] and sl==False and fil==False:
                    pass
                elif i.enviarData()[0] == '@@@@':

                    list.append(lis)
                    l=[]
                    ll=[]
                    filtros=[]
                    #entre corchetes
                    sl=False
                    #entre llaves
                    ssl=False
                    fil=False
                    lis=[]
                elif i.enviarData()[0] == 'FILTROS':
                    fil=True
                elif i.enviarData()[0] == ';' and fil==True:
                    lis.append(filtros)
                    filtros=[]
                elif fil==True:
                    if i.enviarData()[0]!=',' and i.enviarData()[0]!='=':
                        filtros.append(i.enviarData()[0])
                
                elif i.enviarData()[0]=='{' and ssl==False:
                    ssl=True
                elif i.enviarData()[0]=='}' and sl==False and ssl==True:
                    lis.append(ll)
                    ll=[]
                    ssl=False
                elif i.enviarData()[0]=='[' and sl==False and ssl==True:
                    sl=True
                elif i.enviarData()[0]==']' and sl==True and ssl==True:
                    ll.append(l)
                    l=[]
                    sl=False
                elif sl:
                    if i.enviarData()[0]!=',':
                        l.append(i.enviarData()[0])
                else:
                    lis.append(i.enviarData()[0])
            fil=False    
            list.append(lis)
            for j in range(len(list)):
                LNombre.append(list[j][1])
                LFiltros.append(list[j][12])
                imagen.append(Imagen(list[j][1],list[j][3],list[j][5],list[j][7],list[j][9],list[j][11],list[j][12]))
            generarRTokens(lista)
            generarRErrores(listaE)
            generarHTML(imagen)
            generarHTML_MX(imagen)
            generarHTML_MY(imagen)
            generarHTML_MXY(imagen)
            LlenarT(myframe2,lt,ltt,img0,img1,img2,img3)
        else:
            messagebox.showinfo(message="Debe seleccionar un archivo en la seccion de \"Cargar Archivo\"", title="Título")

def generarRTokens(lista):
    encabezado='''<!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8" />
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
                            <meta name="description" content="" />
                            <meta name="author" content="" />
                            <title>{}</title>
                            <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
                            <script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" crossorigin="anonymous"></script>
                            <link href="https://cdnjs.cloudflare.com/ajax/libs/simple-line-icons/2.5.5/css/simple-line-icons.min.css" rel="stylesheet" />
                            <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css" />
                            <link href="css/styles.css" rel="stylesheet" />
                        </head>

                        <body id="page-top">
                            

                            <header class="masthead d-flex align-items-center">
                                <div class="container px-4 px-lg-5 text-center">
                                    <h1 class="mb-1">{}</h1>
                                </div>
                            </header>

                            <section class="content-section bg-light" id="about">
                                <div class="container px-4 px-lg-5 text-center">
                                    <table class="table table-striped table-dark">
                                        <thead>
                                            <tr>
                                            <th scope="col">Lexema</th>
                                            <th scope="col">Token</th>
                                            <th scope="col">Fila</th>
                                            <th scope="col">Columna</th>
                                            </tr>
                                        </thead>
                                        <tbody>'''.format('Lista de Tokens','Lista de Tokens')
    tabla=''
    for i in lista:
        tabla+='''<tr>
                    <th>{}</th>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                   </tr>'''.format(i.enviarData()[0],i.enviarData()[1],i.enviarData()[2],i.enviarData()[3])
    fin='''</tbody>
                        </table>
                        </div>
                    </section>

                    <a class="scroll-to-top rounded" href="#page-top"><i class="fas fa-angle-up"></i></a>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"></script>
                    <script src="js/scripts.js"></script>
                </body>
            </html>'''

    contenido=encabezado+tabla+fin
    f = open ('Lista_de_Tokens.html','w')
    f.write(contenido)
    f.close()

def generarRErrores(listaE):
    encabezado='''<!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8" />
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
                            <meta name="description" content="" />
                            <meta name="author" content="" />
                            <title>{}</title>
                            <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
                            <script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" crossorigin="anonymous"></script>
                            <link href="https://cdnjs.cloudflare.com/ajax/libs/simple-line-icons/2.5.5/css/simple-line-icons.min.css" rel="stylesheet" />
                            <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css" />
                            <link href="css/styles.css" rel="stylesheet" />
                        </head>

                        <body id="page-top">
                            

                            <header class="masthead d-flex align-items-center">
                                <div class="container px-4 px-lg-5 text-center">
                                    <h1 class="mb-1">{}</h1>
                                </div>
                            </header>

                            <section class="content-section bg-light" id="about">
                                <div class="container px-4 px-lg-5 text-center">
                                    <table class="table table-striped table-dark">
                                        <thead>
                                            <tr>
                                            <th scope="col">Descripcion</th>
                                            <th scope="col">Fila</th>
                                            <th scope="col">Columna</th>
                                            </tr>
                                        </thead>
                                        <tbody>'''.format('Lista de Errores','Lista de Errores')
    tabla=''
    if len(listaE)==0:
        print('No hay errores')
        tabla='<h2>NO HAY ERRORES</h2>'
    else:
        for i in listaE:
            tabla+='''<tr>
                    <th>{}</th>
                    <td>{}</td>
                    <td>{}</td>
                   </tr>'''.format(i.enviarData()[0],i.enviarData()[1],i.enviarData()[2])
    fin='''</tbody>
                        </table>
                        </div>
                    </section>

                    <a class="scroll-to-top rounded" href="#page-top"><i class="fas fa-angle-up"></i></a>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"></script>
                    <script src="js/scripts.js"></script>
                </body>
            </html>'''
    contenido=encabezado+tabla+fin
    f = open ('Lista_de_Errores.html','w')
    f.write(contenido)
    f.close()
 
def generarHTML(imagen):
    
    for i in imagen:
        
        ancho=int(i.getAncho())
        alto=int(i.getAlto())

        codigo='<html><head><title>{}</title></head><body>'.format(i.getTitulo())
        
        codigot='<table>'
        for y in range(i.getColumnas()):
            codigot+='<tr>'
            for x in range(i.getFilas()):
                imprime=False
                print('X '+str(x)+' Y '+str(y))
                for z in i.getCeldas():
                    if z[2]=='TRUE' and int(z[0])==x and int(z[1])==y:
                        print('Existe')
                        imprime=True
                        codigot+='<td style="background-color: {}; width: {}; height: {};"></td>'.format(z[3],i.getX(),i.getY())
                if imprime==False:
                    print('NO Existe')
                    codigot+='<td style="background-color: #FFFFFF; width: {}; height: {};"></td>'.format(i.getX(),i.getY())
            
            codigot+='</tr>'
        
        codigot+='</table>'
        codigof='</body></html>'

        scan = AnalizadorLexicoT()
        scan.analizarTitulo(i.getTitulo())
        listaT=scan.impTokens()
        titulo=''

        for i in listaT:
            if i.enviarData()[0] != '\"':
                titulo=i.enviarData()[0]

        listaT=[]

        codigoo=codigo+codigot+codigof

        f = open (titulo+'.html','w')
        f.write(codigoo)
        f.close()

        hti = Html2Image()

        hti.screenshot(html_str=codigoo, size=(ancho,alto), save_as=titulo+'.png')

def generarHTML_MY(imagen):
    
    for i in imagen:
        if 'MIRRORY' in i.getFiltros():
            ancho=int(i.getAncho())
            alto=int(i.getAlto())

            codigo='<html><head><title>{}</title></head><body>'.format(i.getTitulo())
            
            codigot='<table>'
            for y in range(i.getColumnas()-1,-1,-1):
                codigot+='<tr>'
                for x in range(i.getFilas()):
                    imprime=False
                    print('X '+str(x)+' Y '+str(y))
                    for z in i.getCeldas():
                        if z[2]=='TRUE' and int(z[0])==x and int(z[1])==y:
                            print('Existe')
                            imprime=True
                            codigot+='<td style="background-color: {}; width: {}; height: {};"></td>'.format(z[3],i.getX(),i.getY())
                    if imprime==False:
                        print('NO Existe')
                        codigot+='<td style="background-color: #FFFFFF; width: {}; height: {};"></td>'.format(i.getX(),i.getY())
                
                codigot+='</tr>'
            
            codigot+='</table>'
            codigof='</body></html>'

            scan = AnalizadorLexicoT()
            scan.analizarTitulo(i.getTitulo())
            listaT=scan.impTokens()
            titulo=''

            for i in listaT:
                if i.enviarData()[0] != '\"':
                    titulo=i.enviarData()[0]

            listaT=[]

            codigoo=codigo+codigot+codigof

            f = open (titulo+'[MY].html','w')
            f.write(codigoo)
            f.close()

            hti = Html2Image()

            hti.screenshot(html_str=codigoo, size=(ancho,alto), save_as=titulo+'[MY].png')

def generarHTML_MX(imagen):
    
    for i in imagen:
        if 'MIRRORX' in i.getFiltros():
            ancho=int(i.getAncho())
            alto=int(i.getAlto())

            codigo='<html><head><title>{}</title></head><body>'.format(i.getTitulo())
            
            codigot='<table>'
            for y in range(i.getColumnas()):
                codigot+='<tr>'
                for x in range(i.getFilas()-1,-1,-1):
                    imprime=False
                    print('X '+str(x)+' Y '+str(y))
                    for z in i.getCeldas():
                        if z[2]=='TRUE' and int(z[0])==x and int(z[1])==y:
                            print('Existe')
                            imprime=True
                            codigot+='<td style="background-color: {}; width: {}; height: {};"></td>'.format(z[3],i.getX(),i.getY())
                    if imprime==False:
                        print('NO Existe')
                        codigot+='<td style="background-color: #FFFFFF; width: {}; height: {};"></td>'.format(i.getX(),i.getY())
                
                codigot+='</tr>'
            
            codigot+='</table>'
            codigof='</body></html>'

            scan = AnalizadorLexicoT()
            scan.analizarTitulo(i.getTitulo())
            listaT=scan.impTokens()
            titulo=''

            for i in listaT:
                if i.enviarData()[0] != '\"':
                    titulo=i.enviarData()[0]

            listaT=[]

            codigoo=codigo+codigot+codigof

            f = open (titulo+'[MX].html','w')
            f.write(codigoo)
            f.close()

            hti = Html2Image()

            hti.screenshot(html_str=codigoo, size=(ancho,alto), save_as=titulo+'[MX].png')

def generarHTML_MXY(imagen):
    
    for i in imagen:
        if 'DOUBLEMIRROR' in i.getFiltros():
            ancho=int(i.getAncho())
            alto=int(i.getAlto())

            codigo='<html><head><title>{}</title></head><body>'.format(i.getTitulo())
            
            codigot='<table>'
            for y in range(i.getColumnas()-1,-1,-1):
                codigot+='<tr>'
                for x in range(i.getFilas()-1,-1,-1):
                    imprime=False
                    print('X '+str(x)+' Y '+str(y))
                    for z in i.getCeldas():
                        if z[2]=='TRUE' and int(z[0])==x and int(z[1])==y:
                            print('Existe')
                            imprime=True
                            codigot+='<td style="background-color: {}; width: {}; height: {};"></td>'.format(z[3],i.getX(),i.getY())
                    if imprime==False:
                        print('NO Existe')
                        codigot+='<td style="background-color: #FFFFFF; width: {}; height: {};"></td>'.format(i.getX(),i.getY())
                
                codigot+='</tr>'
            
            codigot+='</table>'
            codigof='</body></html>'

            scan = AnalizadorLexicoT()
            scan.analizarTitulo(i.getTitulo())
            listaT=scan.impTokens()
            titulo=''

            for i in listaT:
                if i.enviarData()[0] != '\"':
                    titulo=i.enviarData()[0]

            listaT=[]

            codigoo=codigo+codigot+codigof

            f = open (titulo+'[MXY].html','w')
            f.write(codigoo)
            f.close()

            hti = Html2Image()

            hti.screenshot(html_str=codigoo, size=(ancho,alto), save_as=titulo+'[MXY].png')

def LlenarT(myframe2,lt,ltt,img0,img1,img2,img3):
    radioValue = IntVar() 
    for i in range(len(LNombre)):
        scan = AnalizadorLexicoT()
        scan.analizarTitulo(LNombre[i])
        listaT=scan.impTokens()
        titulo=''

        for x in listaT:
            if x.enviarData()[0] != '\"':
                titulo=(x.enviarData()[0])

        Radiobutton(myframe2, text=str(LNombre[i]),font=("Comic Sans MS", 16, "italic"),bg="#CFFA8C",variable=radioValue,value=titulo).pack()

        lt.configure(textvariable=radioValue)
        ltt.configure(textvariable=radioValue)

        
