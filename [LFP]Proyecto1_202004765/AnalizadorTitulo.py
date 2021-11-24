from Token import Token
from Error import Error
from prettytable import PrettyTable

class AnalizadorLexicoT:

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

    def analizarTitulo(self,cadena):
        self.listaTokens = []
        self.listaErrores = []
        cadena+="#"
        while self.i < len(cadena):
            if self.estado == 0:
                self.estado0(cadena[self.i])
            elif self.estado==1:
                self.estado1(cadena[self.i])
            self.i += 1 

    def estado0(self, caracter):
        if caracter=='\"':
            self.agregar_token(caracter,'Comillas',self.linea,self.columna) 
            self.buffer = ''
            self.columna += 1
        elif caracter.isalpha():
            self.buffer+=caracter
            self.columna+=1   
            self.estado = 1
            
        elif caracter=="#":
            pass

    def estado1(self, caracter):
        if caracter=='\"':
            self.agregar_token(self.buffer,'Titulo',self.linea,self.columna)            
            self.estado = 0
            self.columna+=1
            self.i -= 1
        else:
            self.buffer+=caracter
            self.columna+=1
        

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