import csv

# TODOS LOS MENU

def menu_principal():
    print("MENU PRINCIPAL")
    print("1 . Carga de Datos:")
    print("\t\t\t * Lee y carga los archivos de texto y csv.")
    print("2. Análisis de la actividad de los influencers")
    print("3. Reportes")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    while opcion not in ['1','2','3','4']:
        opcion = input("Elija una opción válida: ")

    return int(opcion)

def menu_secundario():
    print("MENU SECUNDARIO")
    print("1. Las 5 publicaciones con mejor calificación")
    print("2. El usuario publicador con más comentarios positivos.")
    print("3. El usuario con mayor participación.")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    while opcion not in ['1','2','3','4']:
        opcion = input("Elija una opción válida: ")

    return int(opcion)

def menu_reportes():
    
    usuario = input("Ingrese el usuario a analizar sin el @: ")
    intentos = 3
    while not validacion(usuario) and intentos != 1: 
        usuario = input("Ingrese el usuario a analizar sin el @: ")
        intentos -= 1
    
    if intentos == 1:
        return None
    else:
        return usuario


# HERRAMIENTAS UTILIZADAS 

def split(string,separador):
            
  
    l = []
    inicio = 0
    final = len(string)-1
    for i in range(len(string)):
        
        
        if string[i] == separador or i == final:
            
            if i == final:
                palabra = string[inicio:]
            else:    
                palabra = string[inicio:i]
            
            inicio = i + 1
            
            l.append(palabra)
            
    return l 

def ordenar(id_publicacion,usuario_publicador,publicacion,promedio):
    
    
    for i in range(len(promedio)-1,0,-1): 
        for j in range(0,i):
            if promedio[j] < promedio[j+1]:
                
                aux= promedio[j]
                promedio[j]=promedio[j+1]
                promedio[j+1]=aux

                aux= id_publicacion[j]
                id_publicacion[j]=id_publicacion[j+1]
                id_publicacion[j+1]=aux

                aux= usuario_publicador[j]
                usuario_publicador[j]=usuario_publicador[j+1]
                usuario_publicador[j+1]=aux

                aux= publicacion[j]
                publicacion[j]=publicacion[j+1]
                publicacion[j+1]=aux

def minusculas(S):
    transformado = ""
    for i in range(len(S)):
        if 'A' <= S[i] <= 'Z':
            transformado += chr(ord(S[i]) + 32)
        else:
            transformado += S[i]
    return transformado

def strip(string):
    transformado = ""
    primera = True
    primera_posicion = 0
    ultima_posicion = 0
    
    for i in range(len(string)):
        
        if string[i] != " ":
            ultima_posicion = i
            
            if primera:
                primera_posicion = i
                primera = False
            
    
    if ultima_posicion == len(string):
        transformado = string[primera_posicion:]
    else:
        transformado = string[primera_posicion:ultima_posicion+1]
    return transformado




# MENU DE CARGAR DATOS

def leer_publicaciones(id_publicacion,usuario_publicador,publicacion):
    
    with open('publicaciones.csv', 'r') as publicaciones:

        lector = csv.reader(publicaciones)
        skip = True
        for i in lector:
            if not skip:
                id_publicacion.append(i[0])
                usuario_publicador.append(i[1])
                publicacion.append(i[2])
            else:
                skip=False

def leer_comentarios(id_publicacion,usuario_comentador,comentario):
    with open('comentarios.csv', 'r') as comentarios:

        lector = csv.reader(comentarios)
        skip_header = True
        for i in lector:
            if not skip_header:
                id_publicacion.append(i[0])
                usuario_comentador.append(i[1])
                comentario.append(i[2])
            else:
                skip_header = False


def leer_sentimientos(negativos, positivos):

    neg_text = ""
    pos_text = ""
    
    with open("sentimientos.txt", 'r') as file:
        pos_text = file.readline()
        neg_text = file.readline()
    
    pos_text = pos_text[11:-1] 
    neg_text = neg_text[11:] 

    pos_text = split(pos_text, ',')
    for i in range(len(pos_text)):
        frase = strip(pos_text[i]) 
        positivos.append(frase)

    neg_text = split(neg_text, ',')
    for i in range(len(neg_text)):
        frase = strip(neg_text[i])
        negativos.append(frase)

def leer_data(id_publicacion,usuario_publicador, publicacion, usuario_comentador, calificacion):

    with open("data.csv", "r") as data:
        lector = csv.reader(data)
        skip = True
        for i in lector:
            
            if not skip:
                if len (i) >= 5:
                    id_publicacion.append(i[0])
                    usuario_publicador.append(i[1])
                    publicacion.append(i[2])
                    usuario_comentador.append(i[3])
                    calificacion.append(i[4])
            else:
                skip = False
                
def calificar(neg,pos,comentario):
    
    calificacion = 0
    comentario = minusculas(comentario)
    for i in neg:
        if  i  in comentario:
            calificacion -= 1
    for j in pos:
        if j in comentario :
            calificacion +=1

    print (comentario, calificacion)
    return calificacion


def cargar_datos():
    
    id_publicacion_comentarios = []
    usuario_comentador =[]
    comentario = []

    leer_comentarios(id_publicacion_comentarios, usuario_comentador, comentario)

    id_publicacion = []
    usuario_publicador = []
    publicacion = []

    leer_publicaciones(id_publicacion, usuario_publicador, publicacion)

    neg = []
    pos= []

    leer_sentimientos(neg, pos)

    data_usuario_publicacion =[]
    data_calificacion=[]
    data_publicacion =[]

    for i in range(len(comentario)): 
                
        id = int(id_publicacion_comentarios[i])
        publi = publicacion[id-1]
        usuario = usuario_publicador[id -1]
        
        data_publicacion.append(publi)
        data_usuario_publicacion.append(usuario)
        data_calificacion.append(calificar(neg,pos, comentario[i]))


    with open("data.csv",'w', newline="") as data:

        escritor = csv.writer(data)
        escritor.writerow(["ID_PUBLICACION", "USUARIO_PUBLICADOR", "PUBLICACION", "USUARIO_COMENTADOR","CALIFICACION"])

        for i in range(len(comentario)):
            escritor.writerow([id_publicacion_comentarios[i], data_usuario_publicacion[i], data_publicacion[i], usuario_comentador[i], data_calificacion[i]])


#MENU DE ANALISIS

def mejores_5 ():

    id_publicacion= []
    publicacion= []
    usuario_publicador= []

    leer_publicaciones (id_publicacion,publicacion,usuario_publicador)

    promedio_de_notas = [0] * len(id_publicacion)
    contador = [0] * len(id_publicacion)

    id_publicacion_data_csv = []
    calificacion_data_csv = []

    try:
        leer_data(id_publicacion_data_csv, [], [], [], calificacion_data_csv)

        for i in range (len(id_publicacion_data_csv)):

            id= int(id_publicacion_data_csv [i])
            nota= calificacion_data_csv[i]

            promedio_de_notas[id-1] += int(nota)

            contador[id-1] += 1

        for j in range (len(promedio_de_notas)):

            if contador [j] != 0:
                promedio_de_notas[j] = promedio_de_notas[j] / contador[j]

        ordenar(id_publicacion,usuario_publicador,publicacion,promedio_de_notas)
        
        
        print("Top 5 publicaciones y sus calificaciones:")
        for i in range(5):
            
            print("Publicación:", publicacion[i])
            print("Calificación:", promedio_de_notas[i])

    except FileNotFoundError:
        print("Primero debe cargar los datos.")
        return None


def suma_mas_alta ():
    usuario_publicador_data_csv= []
    calificacion_data_csv= []
    try:
        leer_data([], usuario_publicador_data_csv, [], [], calificacion_data_csv)

        suma_max= None
        usuario_suma_max= ""
        usuarios_ya_medidos= []

        for i in range (len(usuario_publicador_data_csv)):

            usuario= usuario_publicador_data_csv [i]

            if usuario not in usuarios_ya_medidos:

                suma_notas= 0

                for j in range (len (calificacion_data_csv)):

                    if usuario_publicador_data_csv[j] == usuario:

                        suma_notas += int(calificacion_data_csv [j])

                if (suma_max == None) or (suma_notas > suma_max):

                    suma_max = suma_notas
                    usuario_suma_max = usuario

                usuarios_ya_medidos.append (usuario)

        print ("El usuario con la suma de calificaciones mas alta es", usuario_suma_max, "con una suma total de: ", suma_max)

    except FileNotFoundError:
        print("Primero debe cargar los datos.")
        return None


def participaciones_usuarios ():

    id_publicacion_data_csv = []
    usuario_publicador = []
    usuario_comentador = []
    try:
        leer_data(id_publicacion_data_csv, usuario_publicador, [], usuario_comentador, [])

        usuarios_totales = [] 
        mayor_participacion = 0
        mayor_usuario= ""

        for i in range(len(id_publicacion_data_csv)):
            if usuario_publicador[i] not in usuarios_totales:
                usuarios_totales.append(usuario_publicador[i])

            if usuario_comentador[i] not in usuarios_totales:
                usuarios_totales.append(usuario_comentador[i])

        publicaciones_medidas = [] 

        for iteracion_usuario in usuarios_totales:
            participacion = 0
            for i in range(len(id_publicacion_data_csv)):  
                

                if usuario_comentador[i] == iteracion_usuario:
                    participacion += 1
                    
                if usuario_publicador[i] == iteracion_usuario and id_publicacion_data_csv[i] not in publicaciones_medidas:
                    participacion += 1
                    publicaciones_medidas.append(id_publicacion_data_csv[i])
                

            if participacion >= mayor_participacion:
                mayor_participacion = participacion
                mayor_usuario = iteracion_usuario


        print("El usuario con mayor participación es: ", mayor_usuario, " con ", mayor_participacion, "participaciones")
    
    except FileNotFoundError:
        print("Primero debe cargar los datos.")
        return None


#MENU DE REPORTES

def validacion(usuario):
    
    publicadores = []
    comentadores = []
    leer_data([], publicadores, [], comentadores, [])

    usuario =  '@' + usuario

    if (usuario in publicadores) or (usuario in comentadores) :
        return True
    
    return False 

def reporte(usuario):
    
    usuario= '@' + usuario
    
    ids = []
    publicadores = []
    comentadores = []
    leer_data(ids, publicadores, [], comentadores, [])

    

    publicaciones = 0
    comentarios = 0
    ids_analizados = []
    for i in range(len(ids)):

        id = ids[i]
        if id not in ids_analizados and publicadores[i] == usuario:
            publicaciones += 1
            ids_analizados.append(id)

        if comentadores[i] == usuario:
            comentarios += 1


    with open('reporte.txt', 'a') as file:

        file.write("Usuario: " + usuario + "\n \t Comentarios: " + str(comentarios) + "\n \t Publicaciones: " + str(publicaciones) + "\n")
    
