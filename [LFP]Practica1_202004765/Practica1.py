from Pr1_OP1 import op1
from Pr1_OP2 import op2
from Pr1_OP3 import op3
from Pr1_OP4 import op4

seleccion = 0
res=[]

while seleccion != 4:
    print(' ***************************************************************\n','**                            MENU                           **\n','***************************************************************\n','** 1. Cargar archivo                                         **\n','** 2. Mostrar reporte en consola                             **\n','** 3. Exportar reporte                                       **\n','** 4. Salir                                                  **\n','***************************************************************')
    print('Seleccione una opción del menú')
    try:
        seleccion = int(input())
    except:
        print("Debe ingresar un número")
    if seleccion==1:
        res=op1.LeerArchivo()
    elif seleccion==2:
        op2.MostrarConsola(res)
    elif seleccion==3:
        op3.GenerarReporte(res)
    elif seleccion==4:
        print("¿Quiere salir? S/N")
        conf=input().upper()
        if conf=="S":
            op4.despedirse()
        elif conf=="N":
            seleccion=0
        else:
            print("Debe ingresar una opción del menú")
    elif seleccion==0:
        print("")
    else:
        print("Escoja un número del menú")

