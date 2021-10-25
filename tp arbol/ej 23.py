from arbol_binario import Arbol

arbol = Arbol()

    

def cargar(arbol):  
    criaturas = {'name': 'basiliscos', 'derrotado':'zeus', 'descripcion':'', 'capturada': ''}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    criaturas = {'name': 'tifon', 'derrotado':'zeus', 'descripcion':'', 'capturada': ''}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    criaturas = {'name': 'tifon', 'derrotado':'argos panoptes', 'descripcion':'', 'capturada': ''}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    criaturas = {'name': 'dino', 'derrotado':'-', 'descripcion':'', 'capturada': ''}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    criaturas = {'name': 'pefredo', 'derrotado':'zeus', 'descripcion':'', 'capturada': ''}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    criaturas = {'name': 'enio', 'derrotado':'heracle', 'descripcion':'', 'capturada': ''}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    criaturas = {'name': 'medusa', 'derrotado':'heracle', 'descripcion':'', 'capturada': ''}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    criaturas = {'name': 'aves del estinfalo', 'derrotado':'heracle', 'descripcion':'', 'capturada': ''}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    criaturas = {'name': 'ladon', 'derrotado':'zeus', 'descripcion':'', 'capturada': 'heracles'}
    arbol = arbol.insertar_nodo(criaturas['name'], criaturas)
    return arbol
   
def talos():
    """muestra info de talos"""
    pos = arbol.busqueda('talos')
    if (pos):
        print(pos.datos)

def aves_del_estinfalo():
    """cambia derrotado"""
    pos = arbol.busqueda('aves del estinfalo')
    if(pos):
        pos.datos['derrotado'] = 'heracles'


def cambiar_derrotados():
    """cambia derrotado a heracles"""
    aux = 'si'
    while (aux == 'si'):
        buscado = input('ingrese nombre a buscar para modificar derrotados a heracle ')
        pos = arbol.busqueda(buscado)
        if(pos):
            pos.datos['derrotado'] = 'heracles'
        aux = input('ingrese si para cambiar a otro, no para salir ')

def ordenar_dic(item):
    return item[1]

def ordenar_diccionario():
    lista = list(dic.items())
    lista.sort(key=ordenar_dic, reverse=True)
    print(lista[:3])

arbol = cargar(arbol)
arbol.inorden_criaturas()
talos() #punto c
dic = {}
arbol.conta_criaturas_derrotadas(dic) #punto d
print('LOS 3 DIOSES QUE DERROTARON MAYOR CANTIDAD DE CRIATURAS')
ordenar_diccionario()

print('CRIATURAS DERROTADAS POR HERACLE') 
arbol.listar_criaturas_derrotadas('heracle') #punto e
print()
print('CRIATURAS QUE NO HAN SIDO DERROTADAS') 
arbol.listar_criaturas_derrotadas('-') #punto f
arbol.eliminar_nodos_iguales('tifon') #punto j, sirenas/ basiliscos
aves_del_estinfalo() #punto k

arbol.dato_mal_cargado() #punto l
print('LISTADO POR NIVEL')
arbol.barrido_por_nivel() #punto m
print('CRIATURAS CAPTURADAS POR HERACLE')
arbol.listar_criaturas_capturadas('heracles') #punto n
arbol.inorden_criaturas()
print()
cambiar_derrotados() #PUNTO G
arbol.inorden_criaturas()

#falta punto I, se debe permitir búsquedas por coincidencia;