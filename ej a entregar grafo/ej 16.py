# Implementar un grafo no dirigido para almacenar puntos turísticos de interés de un determi-
# nado país teniendo en cuenta los siguientes requerimientos:

# a. debe ser un grafo completo es decir que todos los vértices se deben conectar con todos;

# b. cargar los siguientes lugares (con sus coordenadas de latitud y longitud) templos de: Ate-
# nas (Partenón), Zeus (Olimpia), Hera (Olimpia), Apolo (Delfos),Poseidón (Sunión), Arte-
# misa (Éfeso) y Teatro de Dionisio (Acrópolis)

# c. hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;

# d. hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta
# el templo de Apolo, en Delfos.

from grafo import Grafo

grafo = Grafo(dirigido=False)
grafo.insertar_vertice('Atenas' ,data={'Latitud' : '21º 46 52 S', 'Longitud': '66º 13 17'})
grafo.insertar_vertice('Zeus' ,data={'Latitud' : ' 28º 23 67', 'Longitud': '66º 12 87'})
grafo.insertar_vertice('Hera',data={'Latitud' : ' 27º 713 11', 'Longitud': '615º 83 87'})
grafo.insertar_vertice('Apolo', data={'Latitud' : ' 71º 2 10', 'Longitud': '102º 1 87'})
grafo.insertar_vertice('Poseidon',data={'Latitud' : ' 38º 91 09', 'Longitud': '59º 92 87'})
grafo.insertar_vertice('Artemisa', data={'Latitud' : ' 11º 10 12', 'Longitud': '16º 1 91'})
grafo.insertar_vertice('Teoatro de Dionsio', data={'Latitud' : ' 99º 13 1', 'Longitud': '62º 1 64'})

grafo.insertar_arista(120, 'Atenas', 'Zeus')
grafo.insertar_arista(11, 'Atenas', 'Hera')
grafo.insertar_arista(10.3, 'Atenas', 'Apolo')
grafo.insertar_arista(121, 'Atenas', 'Poseidon')
grafo.insertar_arista(23, 'Atenas', 'Artemisa')
grafo.insertar_arista(54, 'Atenas', 'Teoatro de Dionsio')


grafo.insertar_arista(64, 'Zeus', 'Hera')
grafo.insertar_arista(12, 'Zeus', 'Apolo')
grafo.insertar_arista(67, 'Zeus', 'Poseidon')
grafo.insertar_arista(10.2, 'Zeus', 'Artemisa')
grafo.insertar_arista(1.5, 'Zeus', 'Teoatro de Dionsio')

grafo.insertar_arista(23, 'Hera', 'Apolo')
grafo.insertar_arista(93, 'Hera', 'Poseidon')
grafo.insertar_arista(8.1, 'Hera', 'Artemisa')
grafo.insertar_arista(6.1, 'Hera', 'Teoatro de Dionsio')

grafo.insertar_arista(21, 'Apolo', 'Poseidon')
grafo.insertar_arista(461, 'Apolo', 'Artemisa')
grafo.insertar_arista(741, 'Apolo', 'Teoatro de Dionsio')

grafo.insertar_arista(211, 'Poseidon', 'Artemisa')
grafo.insertar_arista(61, 'Poseidon', 'Teoatro de Dionsio')

grafo.insertar_arista(14, 'Artemisa', 'Teoatro de Dionsio')



def camino_corto(dios1, dios2):
    """devuelve el camino mas corto entre dos dioses"""
    vertice_origen = grafo.buscar_vertice(dios1)
    vertice_destino = grafo.buscar_vertice(dios2)
    camino = grafo.dijkstra(vertice_origen, vertice_destino)
    destino = dios2
    costo = None
    while(not camino.pila_vacia()):
        dato = camino.desapilar()
        if(dato[1][0] == destino):
            if(costo is None):
                costo = dato[0]
            print(dato[1][0])
            destino = dato[1][1]
    print('El costo total del camino es:', costo)


camino_corto('Atenas', 'Apolo')
print(grafo.prim())