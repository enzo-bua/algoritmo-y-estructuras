from lista import Lista   

lista = Lista()
lista2 = Lista()

def cargar():
    lista.insertar(5)
    lista.insertar(4)
    lista.insertar(1)
    lista.insertar(2)
    
    lista2.insertar(12)
    lista2.insertar(1)
    lista2.insertar(4)
    lista2.insertar(5)
    
def elementos_repetidos():
    vector = []
    cantidad_rep = 0
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        if (aux not in vector):
            vector.append(aux)
            for j in range(lista2.tamanio()):
                aux2 = lista2.obtener_elemento(j)
                if (aux == aux2):
                    cantidad_rep +=1
    print('LA CANTIDAD DE ELEMENTOS REPETIDOS ES: ',cantidad_rep)

def unir_lista():
    for i in range(lista2.tamanio()):
        aux = lista2.obtener_elemento(i)
        if (lista.busqueda(aux) == -1):
            lista.insertar(aux)
        
def eliminar():
    while(not lista.lista_vacia()):
        aux = lista.obtener_elemento(0)
        lista.eliminar(aux)
        print(aux)


cargar()
lista.barrido()
print('lista 2')
lista2.barrido()
print("--")
elementos_repetidos()
unir_lista()
print('LISTA CONCATENADA')
lista.barrido()
print('LISTA ELIMINADA ELEMENTO A ELEMENTO')
eliminar()


