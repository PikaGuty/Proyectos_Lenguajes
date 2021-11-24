class op3:
    def GenerarReporte(res):
        Reporte=res[0]
        #Primera parte del html
        encabezado='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" /><meta name="description" content="" /><meta name="author" content="" /><title>'+str(Reporte)+'</title><link rel="icon" type="image/x-icon" href="assets/favicon.ico" /><script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" crossorigin="anonymous"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/simple-line-icons/2.5.5/css/simple-line-icons.min.css" rel="stylesheet" /><link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css" /><link href="css/styles.css" rel="stylesheet" /></head><body id="page-top"><header class="masthead d-flex align-items-center"><div class="container px-4 px-lg-5 text-center"><h1 class="mb-1">'+str(Reporte).replace("_"," ")+'</h1></div></header><section class="content-section" id="portfolio"><div class="container px-4 px-lg-5"><div class="content-section-heading text-center"><h2 class="mb-5">Listado de estudiantes</h2></div><center>'
        c=0
        #Generando tabla exacta como se ingresó
        tabla1='<table class="table table-striped table-dark"><thead><tr><th scope="col">Nombre</th><th scope="col">Nota</th></tr></thead><tbody>'
        
        for x in res:
            if c!=0 and c!=(len(res)-1):
                if x[1]>61:
                    tabla1=tabla1+'<tr class="table-info"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
                else:
                    tabla1=tabla1+'<tr class="table-danger"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
            c+=1
        tabla1=tabla1+'</tbody></table>'
        con=''
        NTabla=''

        ord=[]
        c=0
        for x in res:
            if c!=0 and c!=(len(res)-1):
                li=[x[0],x[1]]
                ord.append(li)
            c+=1
        #Generando tabla ascendente/descendente
        if " ASC" in res[len(res)-1]:
            
            for n in range(len(ord)-1,1,-1):
                for i in range(n):
                    if int(ord[i][1])>int(ord[i+1][1]):
                        temp = int(ord[i][1])
                        ord[i][1] = int(ord[i+1][1])
                        ord[i+1][1] = temp

            NTabla='Ordenado ascendentemente'
            for x in ord:
                if x[1]>61:
                    con=con+'<tr class="table-info"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
                else:
                    con=con+'<tr class="table-danger"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
        elif "ASC" in res[len(res)-1]:
            for n in range(len(ord)-1,1,-1):
                for i in range(n):
                    if int(ord[i][1])>int(ord[i+1][1]):
                        temp = int(ord[i][1])
                        ord[i][1] = int(ord[i+1][1])
                        ord[i+1][1] = temp

            NTabla='Ordenado ascendentemente'
            for x in ord:
                if x[1]>61:
                    con=con+'<tr class="table-info"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
                else:
                    con=con+'<tr class="table-danger"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
        elif "DESC" in res[len(res)-1]:
            for n in range(len(ord)-1,0,-1):
                for i in range(n):
                    if int(ord[i][1])<int(ord[i+1][1]):
                        temp = int(ord[i][1])
                        ord[i][1] = int(ord[i+1][1])
                        ord[i+1][1] = temp
            NTabla='Ordenado descendentemente'
            for x in ord:
                if x[1]>61:
                    con=con+'<tr class="table-info"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
                else:
                    con=con+'<tr class="table-danger"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
        elif " DESC" in res[len(res)-1]:
            for n in range(len(ord)-1,0,-1):
                for i in range(n):
                    if int(ord[i][1])<int(ord[i+1][1]):
                        temp = int(ord[i][1])
                        ord[i][1] = int(ord[i+1][1])
                        ord[i+1][1] = temp
            NTabla='Ordenado descendentemente'
            for x in ord:
                if x[1]>61:
                    con=con+'<tr class="table-info"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
                else:
                    con=con+'<tr class="table-danger"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
        else:
            NTabla='No se proporcionó un orden'
            for x in res:
                if c!=0 and c!=(len(res)-1):
                    if x[1]>61:
                        con=con+'<tr class="table-info"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
                    else:
                        con=con+'<tr class="table-danger"><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>'
                c+=1
        
        tabla2='<div class="content-section-heading text-center"><h2 class="mb-5">'+str(NTabla)+'</h2></div><center><table class="table table-striped table-dark"><thead><tr><th scope="col">Nombre</th><th scope="col">Nota</th></tr></thead><tbody>'
        utabla2='</tbody></table><br>'
        #Obteniendo Promedio
        if " AVG" in res[len(res)-1]:
            suma=0
            promedio=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                   suma+=int(x[1])
                cc+=1
            promedio=suma/len(res)
            avg='<h3 class="mb-5"> Promedio: '+str(round(promedio,2))+'</h3>'
            

        if "AVG" in res[len(res)-1]:
            suma=0
            promedio=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                   suma+=int(x[1])
                cc+=1
            promedio=suma/len(res)
            avg='<h3 class="mb-5"> Promedio: '+str(round(promedio,2))+'</h3>'
        
        #Obteniendo minimo
        if " MIN" in res[len(res)-1]:
            min=100
            nom=""
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if min>int(x[1]):
                        min=int(x[1])
                        nom=x[0]
                   
                cc+=1
            min='<h3 class="mb-5"> Menor nota: '+str(nom)+' con '+str(min)+'pts. </h3>'

        if "MIN" in res[len(res)-1]:
            min=100
            nom=""
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if min>int(x[1]):
                        min=int(x[1])
                        nom=x[0]
                   
                cc+=1
            min='<h3 class="mb-5"> Menor nota: '+str(nom)+' con '+str(min)+'pts. </h3>'
        #Obteniendo maximo
        if " MAX" in res[len(res)-1]:
            max=0
            nom=""
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if max<int(x[1]):
                        max=int(x[1])
                        nom=x[0]
                   
                cc+=1
            max='<h3 class="mb-5"> Mayor nota: '+str(nom)+' con '+str(max)+'pts. </h3>'

        if "MAX" in res[len(res)-1]:
            max=0
            nom=""
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if max<int(x[1]):
                        max=int(x[1])
                        nom=x[0]
                   
                cc+=1
            max='<h3 class="mb-5"> Mayor nota: '+str(nom)+' con '+str(max)+'pts. </h3>'
        #Obteniendo número de aprobados
        if " APR" in res[len(res)-1]:
            cont=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if 61<=int(x[1]):
                        cont+=1
                cc+=1
            
            apr='<h3 class="mb-5"> Aprobados: '+str(cont)+' </h3>'

        if "APR" in res[len(res)-1]:
            cont=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if 61<=int(x[1]):
                        cont+=1
                cc+=1
            
            apr='<h3 class="mb-5"> Aprobados: '+str(cont)+' </h3>'
        #Obteniendo reprobados
        if " REP" in res[len(res)-1]:
            cont=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if 61>int(x[1]):
                        cont+=1
                cc+=1
            rep='<h3 class="mb-5"> Reprobados: '+str(cont)+' </h3>'
        
        if " REP" in res[len(res)-1]:
            cont=0
            cc=0
            for x in res:
                if cc!=0 and cc!=(len(res)-1):
                    if 61>int(x[1]):
                        cont+=1
                cc+=1
            rep='<h3 class="mb-5"> Reprobados: '+str(cont)+' </h3>'
        #Ultima parte del html
        fin='</center></div></div></section></body></html>'
        #Escribiendo HTML
        f = open (str(Reporte)+'.html','w')
        contenido=encabezado+tabla1+tabla2+con+utabla2+avg+min+max+apr+rep
        
        f.write(contenido)
        f.close()
        print("Reporte generado con éxito")