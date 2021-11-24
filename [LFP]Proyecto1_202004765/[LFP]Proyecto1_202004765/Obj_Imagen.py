class Imagen:
    def __init__(self,titulo,ancho,alto,filas,columnas,celdas,filtros):
        self.titulo = titulo
        self.ancho = int(ancho) 
        self.alto = int(alto)
        self.filas = int(filas)
        self.columnas = int(columnas)
        self.x = self.ancho/self.columnas
        self.y = (self.alto/self.filas)-((self.alto/self.filas)/self.filas)
        self.celdas = celdas
        self.filtros = filtros

    #Métodos GET
    def getTitulo(self):
        return self.titulo
    
    def getAncho(self):
        return self.ancho

    def getAlto(self):
        return self.alto

    def getFilas(self):
        return self.filas

    def getColumnas(self):
        return self.columnas

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCeldas(self):
        return self.celdas

    def getFiltros(self):
        return self.filtros    

    #Métodos SET
    def setTitulo(self,titulo):
        self.titulo = titulo

    def setAncho(self,ancho):
        self.ancho = ancho

    def setAlto(self,alto):
        self.alto = alto

    def setFilas(self,filas):
        self.filas = filas

    def setColumnas(self,columnas):
        self.columnas = columnas

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setCeldas(self,celdas):
        self.celdas = celdas

    def setFiltros(self,filtros):
        self.filtros = filtros

