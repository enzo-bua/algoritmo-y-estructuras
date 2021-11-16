from grafo import Grafo

grafo = Grafo(dirigido=False)


grafo.insertar_vertice('Manjaro', data = {'PC'})
grafo.insertar_vertice('Parrot', data = {'PC'})
grafo.insertar_vertice('Fedora', data = {'PC'})
grafo.insertar_vertice('Mint', data = {'PC'})
grafo.insertar_vertice('Ubuntu', data = {'PC'})

grafo.insertar_vertice('Arch', data = {'Notebook'})
grafo.insertar_vertice('Debian', data = {'Notebook'})
grafo.insertar_vertice('Red Hat', data = {'Notebook'})

grafo.insertar_vertice('Router 1', data = {'Router'})
grafo.insertar_vertice('Router 2', data = {'Router'})
grafo.insertar_vertice('Router 3', data = {'Router'})

grafo.insertar_vertice('Guarani', data = {'Servidor'})
grafo.insertar_vertice('MongoDB', data = {'Servidor'})

grafo.insertar_vertice('Switch 1')
grafo.insertar_vertice('Switch 2')
   
grafo.insertar_vertice('Impresora', data = {'impresora'})


grafo.insertar_arista(40, 'Manjaro', 'Switch 2')
grafo.insertar_arista(12, 'Parrot', 'Switch 2')
grafo.insertar_arista(5, 'MongoDB', 'Switch 2')
grafo.insertar_arista(56, 'Arch', 'Switch 2')
grafo.insertar_arista(40, 'Manjaro', 'Switch 2')
grafo.insertar_arista(61, 'Router 3', 'Switch 2')

grafo.insertar_arista(43, 'Router 1', 'Router 3')
grafo.insertar_arista(50, 'Router 2', 'Router 3')
grafo.insertar_arista(37, 'Router 2', 'Router 1')

grafo.insertar_arista(9, 'Router 2', 'Guarani')
grafo.insertar_arista(25, 'Router 2', 'Red Hat')

grafo.insertar_arista(29, 'Router 1', 'Switch 1')

grafo.insertar_arista(17, 'Switch 1', 'Debian')
grafo.insertar_arista(18, 'Switch 1', 'Ubuntu')
grafo.insertar_arista(22, 'Switch 1', 'Impresora')
grafo.insertar_arista(80, 'Switch 1', 'Mint')


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


# PUNTO 2
pos_redHat = grafo.buscar_vertice('Red Hat') 
pos_debian = grafo.buscar_vertice('Debian') 
pos_arch = grafo.buscar_vertice('Arch') 

print('BARRIDO EN PROFUNDIDAD PARTIENDO DESDE RED HAT')
grafo.barrido_profundidad(pos_redHat)
grafo.marcar_no_visitado()


print('BARRIDO EN PROFUNDIDAD PARTIENDO DESDE DEBIAN')
grafo.barrido_profundidad(pos_debian)
grafo.marcar_no_visitado()

print('BARRIDO EN PROFUNDIDAD PARTIENDO DESDE ARCH')
grafo.barrido_profundidad(pos_arch)
grafo.marcar_no_visitado()
print()
print('BARRIDO EN AMPLITUD PARTIENDO DESDE RED HAT')
grafo.barrido_amplitud(pos_redHat)
grafo.marcar_no_visitado()

print('BARRIDO EN AMPLITUD PARTIENDO DESDE DEBIAN')
grafo.barrido_amplitud(pos_debian)
grafo.marcar_no_visitado()

print('BARRIDO EN AMPLITUD PARTIENDO DESDE ARCH')
grafo.barrido_amplitud(pos_arch)
grafo.marcar_no_visitado()

# PUNTO 3
print()
print('CAMINO MAS CORTO DE DEBIAN HASTA MONGODB')
camino_corto('Debian', 'MongoDB')
print()
print('CAMINO MAS CORTO DE RED HAT HASTA MONGODB')
camino_corto('Red Hat', 'MongoDB')
# PUNTO 4
print()
print('ARBOL DE EXPANSION MINIMA')
print(grafo.prim())

# PUNTO 5
grafo.eliminar_vertice('Impresora')
grafo.barrido_profundidad(0)

    