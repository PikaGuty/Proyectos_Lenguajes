class op2:
    def MostrarConsola(res):
        NoAlumnos=len(res)-2
        print("\n\n")
        print("************************************************************")
        print("**  {:<52}  **".format(res[0]))
        print("************************************************************")
        #print(res[len(res)-1])
        print("**  {:<3}{:<49}  **".format(NoAlumnos,"alumnos en este curso"))
        print("**  {:<52}  **".format(""))
        c=0
        print("**  NOMBRE                                       NOTA     **")
        
        ord=[]
        for x in res:
            if c!=0 and c!=(len(res)-1):
                li=[x[0],x[1]]
                ord.append(li)
            c+=1

        #dec=sorted(ord, key=lambda notas: notas[1])
        

        #Forma de ordenar la salida
        if " ASC" in res[len(res)-1]:
            #asc=sorted(ord, key=lambda notas: notas[1])
            
            for n in range(len(ord)-1,1,-1):
                for i in range(n):
                    if int(ord[i][1])>int(ord[i+1][1]):
                        temp = int(ord[i][1])
                        ord[i][1] = int(ord[i+1][1])
                        ord[i+1][1] = temp
            
            for x in ord:
                print("**  {:<44} {:<7}  **".format(x[0],x[1]))
        elif "ASC" in res[len(res)-1]:
            #asc=sorted(ord, key=lambda notas: notas[1])
            for n in range(len(ord)-1,1,-1):
                for i in range(n):
                    if int(ord[i][1])>int(ord[i+1][1]):
                        temp = int(ord[i][1])
                        ord[i][1] = int(ord[i+1][1])
                        ord[i+1][1] = temp
            
            for x in ord:
                print("**  {:<44} {:<7}  **".format(x[0],x[1]))
        elif "DESC" in res[len(res)-1]:
            #dec=sorted(ord, key=lambda notas: notas[1],reverse=True)
            for n in range(len(ord)-1,0,-1):
                for i in range(n):
                    if int(ord[i][1])<int(ord[i+1][1]):
                        temp = int(ord[i][1])
                        ord[i][1] = int(ord[i+1][1])
                        ord[i+1][1] = temp
            
            for x in ord:
                print("**  {:<44} {:<7}  **".format(x[0],x[1]))
        elif " DESC" in res[len(res)-1]:
            #dec=sorted(ord, key=lambda notas: notas[1],reverse=True)
            for n in range(len(ord)-1,0,-1):
                for i in range(n):
                    if int(ord[i][1])<int(ord[i+1][1]):
                        temp = int(ord[i][1])
                        ord[i][1] = int(ord[i+1][1])
                        ord[i+1][1] = temp
            
            for x in ord:
                print("**  {:<44} {:<7}  **".format(x[0],x[1]))
        else:
            for x in res:
                if c!=0 and c!=(len(res)-1):
                    print("**  {:<44} {:<7}  **".format(x[0],x[1]))
                c+=1
                

        #Obteniendo promedio
        if " AVG" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            suma=0
            promedio=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                   suma+=int(x[1])
                cc+=1
            promedio=suma/len(res)
            print("**  {:<44}{:<8}  **".format("Promedio: ",round(promedio,2)))

        if "AVG" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            suma=0
            promedio=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                   suma+=int(x[1])
                cc+=1
            promedio=suma/len(res)
            print("**  {:<46}{:<7}  **".format("Promedio: ",round(promedio,2)))
        #Obteniendo minimo
        if " MIN" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            min=100
            nom=""
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if min>int(x[1]):
                        min=int(x[1])
                        nom=x[0]
                   
                cc+=1
            
            print("**  {:<6}{:<37}{:<7}  **".format("Mínimo: ",nom,min))

        if "MIN" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            min=100
            nom=""
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if min>int(x[1]):
                        min=int(x[1])
                        nom=x[0]
                   
                cc+=1
            
            print("**  {:<6}{:<37}{:<7}  **".format("Mínimo: ",nom,min))
        #Obteniendo maximo
        if " MAX" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            max=0
            nom=""
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if max<int(x[1]):
                        max=int(x[1])
                        nom=x[0]
                   
                cc+=1
            
            print("**  {:<6}{:<37}{:<7}  **".format("Máximo: ",nom,max))

        if "MAX" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            max=0
            nom=""
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if max<int(x[1]):
                        max=int(x[1])
                        nom=x[0]
                   
                cc+=1
            
            print("**  {:<6}{:<37}{:<7}  **".format("Máximo: ",nom,max))
        #Obteniendo numero de aprobados
        if " APR" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            cont=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if 61<=int(x[1]):
                        cont+=1
                cc+=1
            
            print("**  {:<46}{:<6}  **".format("Aprobados: ",cont))

        if "APR" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            cont=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if 61<=int(x[1]):
                        cont+=1
                cc+=1
            
            print("**  {:<46}{:<6}  **".format("Aprobados: ",cont))
        #Obteniendo numero de reprobados
        if " REP" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            cont=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if 61>int(x[1]):
                        cont+=1
                cc+=1
            
            print("**  {:<46}{:<6}  **".format("Reprobados: ",cont))
        
        if "REP" in res[len(res)-1]:
            print("**  {:<52}  **".format(""))
            cont=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if 61>int(x[1]):
                        cont+=1
                cc+=1
            
            print("**  {:<46}{:<6}  **".format("Reprobados: ",cont))
        


        print("************************************************************")
        print("\n\n")