from arbol_binario import Arbol

arbol_nombre = Arbol()
arbol_codigo = Arbol()

def cargar(arbol_nombre, arbol_codigo):
    dinosaurio = {'name' : 'mosasaurus', 'codigo': '08925', 'ubicacion': '7A'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'spinosaurus', 'codigo': '10923', 'ubicacion': '9B'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 't-rex', 'codigo': '88890', 'ubicacion': '14D'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'tiranosaurio', 'codigo': '90872', 'ubicacion': '1C'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'sgimoloch', 'codigo': '78541', 'ubicacion': '2K'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'ankilosaurus', 'codigo': '792', 'ubicacion': '3J'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'diplodocus', 'codigo': '92923', 'ubicacion': '3H'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'raptor', 'codigo': '09231', 'ubicacion': '6T'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 't-rex', 'codigo': '11201', 'ubicacion': '6A'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'raptor', 'codigo': '11923', 'ubicacion': '23H'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'diplodocus', 'codigo': '99982', 'ubicacion': '10L'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'diplodocus', 'codigo': '12031', 'ubicacion': '12M'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'raptor', 'codigo': '76762', 'ubicacion': '71A'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'mosasaurus', 'codigo': '11111', 'ubicacion': '9G'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 'diplodocus', 'codigo': '12021', 'ubicacion': '12F'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    dinosaurio = {'name' : 't-rex', 'codigo': '09998', 'ubicacion': '90A'}
    arbol_nombre = arbol_nombre.insertar_nodo(dinosaurio['name'], dinosaurio)
    arbol_codigo = arbol_codigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)

    return arbol_nombre, arbol_codigo

def info():
    pos = arbol_codigo.busqueda('792')
    if(pos):
        print(pos.datos)


    

# #PUNTO 1, 2
arbol_nombre, arbol_codigo = cargar(arbol_nombre, arbol_codigo)
# #PUNTO 3
arbol_nombre.inorden()
#PUNTO 4
info()
#PUNTO 5
arbol_nombre.info_dino('t-rex')
#PUNTO 6
arbol_nombre.dato_mal_cargado()
arbol_codigo.dato_mal_cargado()
arbol_nombre.inorden()
#PUNTO 7
arbol_nombre.ubicacion('raptor')
#PUNTO 8
print('La cantidad de diplodocus en el parque es:', arbol_nombre.contar_ocurrencias('diplodocus'))

