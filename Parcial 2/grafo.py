from lista import Lista
from cola import Cola
from heap import HeapMin
from pila import Pila
from math import inf
from copy import deepcopy


class Grafo(object):

    def __init__(self, dirigido=True):
        self.dirigido = dirigido
        self.inicio = Lista()

    def insertar_vertice(self, dato, criterio='info', data=None):  # ! agregar otro
        self.inicio.insertar({'info': dato, 'visitado': False, 'aristas': Lista(), 'data': data}, criterio)


    def insertar_arista(self, peso, origen, destino, criterio='destino', data=None):  # ! agregar otro
        ver_origen = self.inicio.busqueda(origen, 'info')
        ver_destino = self.inicio.busqueda(destino, 'info')
        if(ver_origen != -1 and ver_destino != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].insertar({'peso': peso, 'destino': destino, 'data': data}, criterio)
            if(not self.dirigido and origen != destino):
                data_aux = deepcopy(data)
                if(data):
                    data_aux['relacion'].reverse()
                self.inicio.obtener_elemento(ver_destino)['aristas'].insertar({'peso': peso, 'destino': origen, 'data': data_aux}, criterio)
        else:
            print('los vertices origen o destino no estan en el grafo....', origen, destino)

    def grafo_vacio(self):
        return self.inicio.lista_vacia()

    def tamanio(self):
        return self.inicio.tamanio()
    
    def buscar_vertice(self, clave, criterio='info'):
        return self.inicio.busqueda(clave, criterio=criterio)

    def buscar_arista(self, origen, destino, criterio='destino'):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            return self.inicio.obtener_elemento(ver_origen)['aristas'].busqueda(destino, criterio)
        else:
            return ver_origen

    def barrido_vertices(self):
        self.inicio.barrido()

    def es_adyacente(self, origen, destino): # si hay paso directo
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            destino = self.buscar_arista(origen, destino)
            if(destino != -1):
                return True
            else:
                return False
        else:
            return False

    def adyacentes(self, origen): #barrido de todos los adyacentes, de todos los pasos directos
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].barrido()

    def eliminar_vertice(self, clave):
        aux = self.inicio.eliminar(clave, criterio='info')
        for posicion in range(self.tamanio()):
            origen = self.inicio.obtener_elemento(posicion)['info']
            self.eliminar_arista(origen, clave)
        return aux


    def eliminar_arista(self, origen, destino):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].eliminar(destino, 'destino')
            if(not self.dirigido):
                ver_destino = self.inicio.busqueda(destino, 'info')
                if(ver_destino != -1):
                    self.inicio.obtener_elemento(ver_destino)['aristas'].eliminar(origen, 'destino')

    def barrido_profundidad(self, ver_origen): #barrido en mas profundidad, salta nodos, encontrar el destino antes posible
        """Barrido en profundidad del grafo."""
        while(ver_origen < self.inicio.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                print(vertice['info'])
                aristas = 0
                while(aristas < vertice['aristas'].tamanio()):
                    arista = vertice['aristas'].obtener_elemento(aristas)
                    pos_vertice = self.buscar_vertice(arista['destino'])
                    nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                    if(not nuevo_vertice['visitado']):
                        self.barrido_profundidad(pos_vertice)
                    aristas += 1
            ver_origen += 1

    def barrido_amplitud(self, ver_origen): #primero proz a tu vertice y desp baja
        """Barrido en amplitud del grafo."""
        cola = Cola()
        while(ver_origen < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                cola.arribo(vertice)
                while(not cola.cola_vacia()):
                    nodo = cola.atencion()
                    print(nodo['info'], nodo['data'])
                    aristas = 0
                    while(aristas < nodo['aristas'].tamanio()):
                        adyacente = nodo['aristas'].obtener_elemento(aristas)
                        pos_vertice = self.buscar_vertice(adyacente['destino'])
                        nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                        if(not nuevo_vertice['visitado']):
                            nuevo_vertice['visitado'] = True
                            cola.arribo(nuevo_vertice)
                        aristas += 1
            ver_origen += 1

    def marcar_no_visitado(self):
        """Marca todos losvertices del grafo como no visitados."""
        for i in range(self.tamanio()):
            self.inicio.obtener_elemento(i)['visitado'] = False

    def existe_paso(self, ver_origen, ver_destino): #corta cuando llega al nodo, barrido hasta donde
        """Barrido en profundidad del grafo."""
        resultado = False
        vertice = self.inicio.obtener_elemento(ver_origen)
        if(not vertice['visitado']):
            vertice['visitado'] = True
            aristas = 0
            while(aristas < vertice['aristas'].tamanio() and not resultado):
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos_vertice = self.buscar_vertice(arista['destino'])
                nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                destino = self.inicio.obtener_elemento(ver_destino)
                if(nuevo_vertice['info'] == destino['info']):
                    return True
                else:
                    resultado = self.existe_paso(pos_vertice, ver_destino)
                aristas += 1
        return resultado

    def dijkstra(self, ver_origen, ver_destino):
        """Algoritmo de Dijkstra para hallar el camino mas corto."""
        no_visitados = HeapMin()
        camino = Pila()
        aux = 0
        while(aux < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            vertice_aux = self.inicio.obtener_elemento(aux)
            vertice_aux['anterior'] = None
            if(vertice_aux['info'] == vertice['info']):
                no_visitados.arribo([vertice_aux['info'], None], 0)
            else:
                no_visitados.arribo([vertice_aux['info'], None], inf)
            aux += 1
        while(not no_visitados.vacio()):
            dato = no_visitados.atencion()
            camino.apilar(dato)
            pos_aux = self.buscar_vertice(dato[1][0])
            vertice_aux = self.inicio.obtener_elemento(pos_aux)
            aristas = 0
            while(aristas < vertice_aux['aristas'].tamanio()):
                arista = vertice_aux['aristas'].obtener_elemento(aristas)
                pos_heap = no_visitados.busqueda(arista['destino'])
                if(pos_heap is not None and no_visitados.elementos[pos_heap][0] > dato[0] + arista['peso']):
                    no_visitados.elementos[pos_heap][1][1] = dato[1][0]
                    nuevo_peso = dato[0] + arista['peso']
                    no_visitados.cambiar_prioridad(pos_heap, nuevo_peso)
                aristas += 1
        # print(no_visitados.elementos)
        return camino

    def busqueda_prim(self, bosque, buscado):
        for elemento in bosque:
            if(buscado in elemento[1]):
                return elemento


    def prim(self): #pasar x todos los nodos al menor costo.
        """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
        bosque = []
        aristas = HeapMin()
        origen = self.inicio.obtener_elemento(0)
        adyac = 0
        while(adyac < origen['aristas'].tamanio()):
            arista = origen['aristas'].obtener_elemento(adyac)
            aristas.arribo([origen['info'], arista['destino']], arista['peso'])
            adyac += 1
        # print(bosque)
        # print(aristas.elementos)
        # print()
        while(len(bosque) // 2 < self.tamanio() and not aristas.vacio()):
            dato = aristas.atencion()
            if(len(bosque) == 0) or ((self.busqueda_prim(bosque, dato[1][0]) is not None) ^ (self.busqueda_prim(bosque, dato[1][1]) is not None)):
                bosque.append(dato)
                pos_vertice = self.buscar_vertice(dato[1][1])
                nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                adyac = 0
                while(adyac < nuevo_vertice['aristas'].tamanio()):
                    arista = nuevo_vertice['aristas'].obtener_elemento(adyac)
                    # print(arista)
                    aristas.arribo([nuevo_vertice['info'], arista['destino']], arista['peso'])
                    adyac += 1
            # print(bosque)
            # print(aristas.elementos)
            # a = input()
        return bosque

    def relaciones(self, relacion, buscado):
        """devuelve relacion especifica"""
        origen = self.buscar_vertice(buscado)
        if (origen != -1):
            dios = self.inicio.obtener_elemento(origen)
            for i in range(dios['aristas'].tamanio()):
                dio = dios['aristas'].obtener_elemento(i)
                if(relacion in dio['data']['relacion'] ):
                    print(dio['destino'])
        else:
            print('dios no encontrado')
            

# grafo = Grafo()
# grafo.insertar_vertice('A')
# grafo.insertar_vertice('C')
# grafo.insertar_vertice('B')
# grafo.insertar_vertice('F')
# grafo.insertar_vertice('Z')
# grafo.insertar_vertice('X')

# grafo.insertar_arista(5, 'A', 'B')
# grafo.insertar_arista(2, 'C', 'B')
# grafo.insertar_arista(3, 'B', 'C')
# grafo.insertar_arista(9, 'A', 'F')
# grafo.insertar_arista(5, 'B', 'F')
# grafo.insertar_arista(13, 'F', 'X')
# grafo.insertar_arista(7, 'X', 'Z')
# grafo.insertar_arista(5, 'C', 'X')
# vertice_destino = grafo.buscar_vertice('Z')
# vertice_origen = grafo.buscar_vertice('A')

# bosque = grafo.prim()
# print('arbol de expansion')
# peso = 0
# for elemento in bosque:
#     print(elemento[1][0], '-', elemento[1][1])
#     peso += elemento[0]
# print('costo total', peso)
# pila_camino = grafo.dijkstra(vertice_origen, vertice_destino)

# destino = 'Z'
# costo = None
# while(not pila_camino.pila_vacia()):
#     dato = pila_camino.desapilar()
#     if(dato[1][0] == destino):
#         if(costo is None):
#             costo = dato[0]
#         print(dato[1][0])
#         destino = dato[1][1]
# print('el costo total del camino es:', costo)
# print(grafo.existe_paso(vertice_origen, vertice_destino))
# grafo.barrido_profundidad(vertice_origen)
# grafo.marcar_no_visitado()
# print()
# vertice_origen = grafo.buscar_vertice('F')
# grafo.barrido_amplitud(vertice_origen)

# grafo.insertar_arista(100, 'B', 'B')

# grafo.inicio.obtener_elemento(0)['aristas'].barrido()
# print()
# grafo.inicio.obtener_elemento(1)['aristas'].barrido()

# grafo.barrido_vertices()

# print(grafo.es_adyacente('A', 'F'))
# print(grafo.es_adyacente('A', 'C'))
# # print(grafo.eliminar_vertice('B'))
# print()
# grafo.barrido_vertices()
# print()
# grafo.eliminar_arista('A', 'B')
# grafo.adyacentes('A')
# print()
# grafo.adyacentes('F')
# print()
# grafo.adyacentes('B')

# print(grafo.buscar_vertice('F'))
# print(grafo.buscar_vertice('B'))

# print(grafo.buscar_arista('B','A'))
# print(grafo.buscar_arista('A','A'))
