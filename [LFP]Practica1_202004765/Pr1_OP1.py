from tkinter import filedialog as FileDialog

class op1:
    def LeerArchivo():
        res=[]
        #Utilizando fliedialog de tkinter para abrir un archivo
        ruta=FileDialog.askopenfilename(title="Abrir un fichero")
        c=0
        #abriendo el archivo con el comando "r" para lectura
        with open(ruta,"r") as archivo:
            #leyendo línea por línea
            for linea in archivo:
                lis=[]
                #if para obtener nombre de clase de la primera linea del archivo
                if c==0:
                    l1=linea.split("=")
                    nombreC=l1[0]
                    res.append(nombreC)
                #si no es la primera línea se obtienen nombres y notas    
                else:
                    try:
                        l1=linea.split("\"")
                        nombreA=l1[1]
                        l2=linea.split(";")
                        l3=l2[1].split(">")
                        nota=l3[0]
                        lis.append(nombreA)
                        lis.append(int(nota))
                        res.append(lis)
                    #usando try-except para evitar el error al llegar a la última línea
                    except:
                        l1=linea.split("}")
                        parametros=l1[1].split(",")
                        res.append(parametros)
                c+=1
        print("Archivo analizado con éxito")
        #retornando una lista con los parámetros obtenidos
        return res