from lista import Lista

lista = Lista()
lista_aux = Lista()

personajes = [
    {'name': 'thor', 'aparicion': 2021, 'boolean' : 'true'},
    {'name': 'capitan america', 'aparicion': 2020, 'boolean' : 'false'},
    {'name': 'vision', 'aparicion': 2020, 'boolean' : 'true'},
    {'name': 'viuda negra', 'aparicion': 2019, 'boolean' : 'true'},
    {'name': 'hulk', 'aparicion': 2018, 'boolean' : 'true'},
    {'name': 'scalet witch', 'aparicion': 2013, 'boolean' : 'true'},
    {'name': 'gigante', 'aparicion': 2012, 'boolean' : 'false'},
    {'name': 'viento', 'aparicion': 2020, 'boolean' : 'true'},
    {'name': 'black window', 'aparicion': 2021, 'boolean' : 'false'}
]

personajes_aux = [
    {'name': 'loki', 'aparicion': 2013, 'boolean' : 'true'},
    {'name': 'hulk', 'aparicion': 2018, 'boolean' : 'true'},
    {'name': 'black window', 'aparicion': 2021, 'boolean' : 'false'},
    {'name': 'rocket racoonn', 'aparicion': 2019, 'boolean' : 'true'},
]



def cargar_lista():
    for personaje in personajes:
        lista.insertar(personaje, 'name')

def cargar_lista_aux():
    for personaje in personajes_aux:
        lista_aux.insertar(personaje, 'name')
    
#PUNTO A
def thor():
    """muestra posicion de thor"""
    posicion_thor = lista.busqueda('thor', 'name')
    if(posicion_thor != -1):
        print('Thor esta en la posicion: ',posicion_thor)

#PUNTO B
def modificar_nombre():
    pos = lista.busqueda('scalet witch', 'name')
    lista.obtener_elemento(pos)['name'] = 'scarlet witch'
    lista.ordenar('name')

#PUNTO C
def agregar_lista():
    for i in range(lista_aux.tamanio()):
        aux = lista_aux.obtener_elemento(i)
        posicion = lista.busqueda(aux['name'], 'name')
        if (posicion == -1):
            lista.insertar(aux,'name')

#PUNTO D
def barrido_descendente():
    for i in range(lista.tamanio()-1, -1 ,-1):
        aux = lista.obtener_elemento(i)
        print(aux)

#PUNTO E
def posicion7():
    print(lista.obtener_elemento(7))

#PUNTO F   
def empiezan_c_s():
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        if ((aux['name'][0] == 's') or (aux['name'][0] == 'c')):
            print(aux)



cargar_lista()
cargar_lista_aux()
thor()
modificar_nombre()
agregar_lista()
print('SE ENCUENTRAN AGREGADOS LOS PERSONAJES DE LA LISTA AUXILIAR QUE NO ESTABAN')
print('BARRIDO ASCENDENTE')
lista.barrido()
print()
print('BARRIDO DESCENDENTE')
barrido_descendente()
print()
print('INNFORMACION DEL PERSONAJE UBICADO EN LA POSICION 7')
posicion7()
print('PERSONAJES QUE EMPIEZAN CON C O S')
empiezan_c_s()
#PUNTO G
print('LISTA ORDENADO POR NOMBRE')
lista.barrido()
print()
lista.ordenar('aparicion')
print('LISTA ORDENADO POR AÑO DE APARICION')
lista.barrido()