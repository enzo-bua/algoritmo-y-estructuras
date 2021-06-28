from lista import Lista 
lista = Lista()

def cargar():
    for i in range(2):
        superheroes = {}
        superheroes['name'] = input('ingrese nombre: ')
        superheroes['anio'] = int(input('ingrese año de aparicion: '))
        superheroes['casa'] = input('ingrese casa donde pertenece (MARVEL - DC): ')       
        superheroes['biografia'] = input('ingrese biografia: ')
        lista.insertar(superheroes,'name')

#PUNTO A
def linterna_verde():
    lista.eliminar('linterna verde', 'name')


#PUNTO B
def cambiar_casa():
    busqueda_strange = lista.busqueda('strange', 'name')
    if(busqueda_strange != -1):
        lista.obtener_elemento(busqueda_strange)['casa'] = 'marvel'

# PUNTO C
def año_wolverine():
    anio_wolverine = 0
    busqueda_wolverine = lista.busqueda('wolverine', 'name')
    if(busqueda_wolverine != -1):
        anio_wolverine = lista.obtener_elemento(busqueda_wolverine)['anio']
    return anio_wolverine



# PUNTO D
def biografia():
    for i in range (lista.tamanio()):
        aux = lista.obtener_elemento(i)
        biografia_traje = aux['biografia']
        if ('traje' in biografia_traje) or ('armadura' in biografia_traje):
            print(aux['name'])
 
def aparicion_anterior1963():
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        if(aux['anio'] < 1963):
            print(aux['name'], '--', aux['casa'])

def casa_cm_mm():
    if (lista.busqueda('capitana marvel', 'name') != -1):     
        print('CASA CAPITANA MARVEL')
        print(lista.obtener_elemento(lista.busqueda('capitana marvel', 'name'))['casa'])
    if (lista.busqueda('mujer maravilla', 'name') != -1):
        print('CASA MUJER MARAVILLA')
        print(lista.obtener_elemento(lista.busqueda('mujer maravilla', 'name'))['casa'])

def flash_starLord():
    pos_flash = lista.busqueda('flash', 'name')
    if (pos_flash != -1):
        print('INFORMACION FLASH')
        print(lista.obtener_elemento(pos_flash))
    pos_startLord = lista.busqueda('start lord', 'name')
    if (pos_startLord != -1):
        print('INFORMACION STAR LORD')
        print(lista.obtener_elemento(pos_startLord))

def superheroes_b_m_s():
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        if (aux['name'][0] == 'b'):
            print(aux['name'],' empieza con b')
        elif (aux['name'][0] == 'm'):
            print(aux['name'], ' empieza con m')
        elif (aux['name'][0] == 's'):
            print(aux['name'], ' empieza con s')

def cantidad_casa(): #esto es mas para cuando son varios tipos de casas
    vector = [] #cargo las casas para que no las repitas
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        cantidad = 0
        if (aux['casa'] not in vector):
            vector.append(aux['casa'])
            for j in range(lista.tamanio()):
                aux2 = lista.obtener_elemento(j)
                if (aux['casa'] == aux2['casa']):
                    cantidad +=1
            print('La cantidad de superheroes en la casa ',aux['casa'], ' es: ',cantidad)

           
cargar()
lista.barrido()
print()
linterna_verde()
# cambiar_casa()
# lista.barrido()
# print()
# if (año_wolverine()!= 0):
#     print(año_wolverine())
# print('PERSONAJES QUE EN SU BIOGRAFIA MENCIONA ARMADURA O TRAJE')    
# biografia()
# print('NOMBRE Y CASA DE PERSONAJES QUE APARECIERON ANTES DE 1963')
# aparicion_anterior1963()
# casa_cm_mm()
# flash_starLord()
# superheroes_b_m_s()
# cantidad_casa()
