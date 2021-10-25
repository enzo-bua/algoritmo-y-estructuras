from arbol_binario import Arbol

arbol = Arbol()
arbol_superheroes = Arbol()
arbol_villanos = Arbol()

def cargar(arbol):
    superheroes = {'name': 'doctor strange','superheroe': True }
    arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
    superheroes = {'name': 'calentor','superheroe': True }
    arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
    superheroes = {'name': 'fuego','superheroe': False }
    arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
    superheroes = {'name': 'tierra','superheroe': True }
    arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
    superheroes = {'name': 'callian','superheroe': False }
    arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
    superheroes = {'name': 'sangre','superheroe': True }
    arbol = arbol.insertar_nodo(superheroes['name'], superheroes)
    
def cargar_teclado():
    for i in range(3):
        info = input('ingrese nombre ')
        aux = input('Es superheroe? (si-no) ')
        if (aux =='si'):
            otro = True
        else:
            otro = False
        arbol.insertar_nodo(info, otro)
   


#como iria dentro del ejercico ejemplo      
# def empieza_con_c(self):
#     """muestra superheroes que empiezan con c"""
#     if(self.info is not None):
#         if(self.otro == True):
#             if(self.info[0] == 'c'):
#                 print(self.info, 'Empieza con C')
#             if (self.izq is not None):
#                 empieza_con_c(self.izq)
#             if(self.der is not None):
#                 empieza_con_c(self.der)





def cantidad_nodos_arboles(arbol_superheroes, arbol_villanos):
    """muestra cantidad de nodos del arbol superheroes y arbol villanos"""
    cantidad_nodos_super = arbol_superheroes.cantidad_nodos()
    print('La cantidad de nodos del arbol superheroes es: ',cantidad_nodos_super)
    cantidad_nodos_villanos = arbol_villanos.cantidad_nodos()
    print('La cantidad de nodos del arbol villanos es: ',cantidad_nodos_villanos)

def barrido_ordenado(arbol_superheroes, arbol_villanos):
    print('ARBOL SUPERHEROES')
    arbol_superheroes.inorden()
    print('ARBOL VILLANOS')
    arbol_villanos.inorden()




cargar(arbol) #PUNTO A
print('VILLANOS ORDENADOS')
arbol.inorden_villanos() #PUNTO B
print()
arbol.empieza_con_c() #PUNTO C
print('CANTIDAD DE SUPERHEROES')
print(arbol.cantidad_superheroes()) #PUNTO D

arbol.dato_mal_cargado() #PUNTO E

print('LISTADO DE SUPERHEROES DE FORMA DESCENDIENTES')
arbol.listado_descendiente() #PUNTO F

print()
arbol.dos_arboles(arbol_superheroes, arbol_villanos) #punto G
cantidad_nodos_arboles(arbol_superheroes, arbol_villanos)
barrido_ordenado(arbol_superheroes,arbol_villanos)
    