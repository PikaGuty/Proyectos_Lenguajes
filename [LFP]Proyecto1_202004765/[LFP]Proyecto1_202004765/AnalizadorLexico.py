from Token import Token
from Error import Error
from prettytable import PrettyTable

class AnalizadorLexico:

    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = 0
        self.i = 0


    def agregar_token(self,caracter,token,linea,columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ''


    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido en el lenguaje.', linea, columna))

#********************************** ESTADO 0 **********************************
    def estado0(self,caracter):
        #Transicion para estado 1
        if caracter.isalpha():
            self.buffer += caracter
            self.columna+=1
            self.estado = 1            
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass

        #Zona de errores
        else:
            
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

#********************************** ESTADO 1 **********************************
    def estado1(self,caracter):
        global tipo
        tipo=''
        if caracter.isalpha():
            self.buffer+=caracter
            self.columna+=1
        else:
            if self.buffer=='TITULO':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='ANCHO':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='ALTO':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='FILAS':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='COLUMNAS':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='CELDAS':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='FILTROS':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='MIRRORX':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='MIRRORY':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
            elif self.buffer=='DOUBLEMIRROR':
                tipo=self.buffer
                self.agregar_token(self.buffer,'Palabra Reservada',self.linea,self.columna)            
                self.estado = 2
                self.columna+=1
                self.i -= 1
        
        

#********************************** ESTADO 2 **********************************
    def estado2(self,caracter):
        if caracter == '=':
            self.agregar_token(caracter,'igual',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1
        elif caracter=='{':
            self.agregar_token(caracter,'Llave',self.linea,self.columna) 
            self.buffer = ''
            self.columna=1
            self.estado = 5
        elif caracter=='\"':
            self.buffer += caracter
            self.columna+=1
            self.estado = 3 
        elif caracter.isdigit():
            self.buffer += caracter
            self.columna+=1
            self.estado = 3 
        elif caracter.isalpha():
            self.buffer+=caracter
            self.columna+=1
            self.estado=11
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass

        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

#********************************** ESTADO 3 **********************************
    def estado3(self,caracter):
        if caracter=='\"':
            self.buffer += caracter
            self.agregar_token(self.buffer,tipo,self.linea,self.columna)            
            self.estado = 4
            self.columna+=1
            
        else:
            if caracter==";":
                self.agregar_token(self.buffer,tipo,self.linea,self.columna-1) 
                self.agregar_token(caracter,'puntoycoma',self.linea,self.columna) 
                self.estado=0
                self.columna=1
            else:
                self.buffer+=caracter
                self.columna+=1
    
#********************************** ESTADO 4 **********************************    
    def estado4(self, caracter):
        if caracter == ';':
            self.agregar_token(caracter,'puntoycoma',self.linea,self.columna)
            self.buffer = ''
            self.columna = 1
            self.estado=0
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass

        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

#********************************** ESTADO 5 **********************************    
    def estado5(self, caracter):
        if caracter == '[':
            self.agregar_token(caracter,'corchete',self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=6
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass

        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

#********************************** ESTADO 6 ********************************** 
    def estado6(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        elif caracter==',':
            self.agregar_token(self.buffer,'posicionX',self.linea,self.columna-1)
            self.agregar_token(caracter,'coma',self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=7
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass

        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

#********************************** ESTADO 7 ********************************** 
    def estado7(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        elif caracter==',':
            self.agregar_token(self.buffer,'posicionY',self.linea,self.columna-1)
            self.agregar_token(caracter,'coma',self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=8
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass

        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

#********************************** ESTADO 8 **********************************    
    def estado8(self, caracter):
        if caracter.isalpha():
            self.buffer += caracter
            self.columna += 1
        elif caracter==',':
            self.agregar_token(self.buffer,'Booleano',self.linea,self.columna-1)
            self.agregar_token(caracter,'coma',self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=9
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass
        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
    
#********************************** ESTADO 9 ********************************** 
    def estado9(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        elif caracter.isalpha():
            self.buffer += caracter
            self.columna += 1
        elif caracter=="#":
            self.buffer += caracter
            self.columna += 1
        elif caracter==']':
            self.agregar_token(self.buffer,'Codigo de colores',self.linea,self.columna)
            self.agregar_token(caracter,'corchete',self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=10
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass
        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

    def estado10(self, caracter):
        if caracter==",":
            self.agregar_token(caracter,'coma',self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=5
        elif caracter=='}':
            self.agregar_token(caracter,'Llave',self.linea,self.columna)
            self.buffer += ''
            self.columna+=1
        elif caracter==';':
            self.agregar_token(caracter,'puntoycoma',self.linea,self.columna)
            self.buffer += ''
            self.columna+=1
            self.estado=1
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass
        #Zona de errores
        else:
            
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

    def estado11(self, caracter):
        if caracter.isalpha():
            self.buffer+=caracter
            self.columna+=1
        else:
            if self.buffer=='MIRRORX':
                self.agregar_token(self.buffer,'Palabra Reservada Filtro',self.linea,self.columna)            
                self.estado = 12
                self.columna+=1
                self.i -= 1
            elif self.buffer=='MIRRORY':
                self.agregar_token(self.buffer,'Palabra Reservada Filtro',self.linea,self.columna)            
                self.estado = 12
                self.columna+=1
                self.i -= 1
            elif self.buffer=='DOUBLEMIRROR':
                self.agregar_token(self.buffer,'Palabra Reservada Filtro',self.linea,self.columna)            
                self.estado = 12
                self.columna+=1
                self.i -= 1
    
    def estado12(self, caracter):
        if caracter == ',':
            self.agregar_token(caracter,'coma',self.linea,self.columna)
            self.buffer = ''
            self.columna +=1
            self.estado=11
        elif caracter == ';':
            self.agregar_token(caracter,'puntoycoma',self.linea,self.columna)
            self.buffer = ''
            self.columna +=1
            
        elif caracter == '@':
            self.buffer+=caracter
            self.columna+=1
            if self.buffer=='@@@@':
                self.agregar_token(self.buffer,'Nueva imagen',self.linea,self.columna)            
                self.buffer=''
                self.estado = 0
                self.columna=1
                

        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass

        #Zona de errores
        else:
            
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1

    def analizar(self, cadena):
        '''Analiza léxicamente una cadena'''
        #inicializar listas nuevamente
        self.listaTokens = []
        self.listaErrores = []
        #recorrer caracter por caracter
        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.estado0(cadena[self.i])
            elif self.estado == 1:
                self.estado1(cadena[self.i])
            elif self.estado == 2:
                self.estado2(cadena[self.i])
            elif self.estado == 3:
                self.estado3(cadena[self.i])
            elif self.estado == 4:
                self.estado4(cadena[self.i])
            elif self.estado == 5:
                self.estado5(cadena[self.i])
            elif self.estado == 6:
                self.estado6(cadena[self.i])
            elif self.estado == 7:
                self.estado7(cadena[self.i])
            elif self.estado == 8:
                self.estado8(cadena[self.i])
            elif self.estado == 9:
                self.estado9(cadena[self.i])
            elif self.estado == 10:
                self.estado10(cadena[self.i])
            elif self.estado == 11:
                self.estado11(cadena[self.i])
            elif self.estado == 12:
                self.estado12(cadena[self.i])
            self.i += 1 
                     

    def impTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarData())
        print(x)
        return self.listaTokens

    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarData())
            print(x)
        return self.listaErrores
