from AnalizadorLexico import AnalizadorLexico

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

if __name__ == '__main__':
    #Leemos el archivo de entrada
    cadena = leerArchivo('entrada.txt')

    #Instanciamos un nuevo analizador lexico o scanner
    scanner = AnalizadorLexico()

    #Enviamos la cadena a analizar
    scanner.analizar(cadena)
    
    lista=scanner.impTokens()
    scanner.impErrores()

    print('HOLAAAAAAAAAAAA')
    list=[]
    lis=[]
    for i in lista:
        if i.enviarData()[0] in ['=',';','{','}','[',']',',']:
            pass
        elif i.enviarData()[0] == '@@@@':
            lista.append(lis)
            lis=[]
        else:
            lis.append(i.enviarData()[0])
            print(i.enviarData()[0])

    list.append(lis)
    print(list)