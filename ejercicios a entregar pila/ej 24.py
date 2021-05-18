from pila import Pila 

class Personajes(object):
    def __init__(self, nombre_personaje, c_peliculas_participo):
        self.nombre_personaje = nombre_personaje
        self. c_peliculas_participo = c_peliculas_participo
    
    def __str__ (self):
        return self.nombre_personaje+' - '+ self.c_peliculas_participo

pila = Pila()
pila_aux = Pila()
posicion_rocket = 0
posicion_groot = 0

for i in range(0, 2):
    nombre_personaje = input('ingrese personaje: ')
    c_peliculas_participo = input('ingrese cantidad de peliculas de la saga que participo: ')
    pila.apilar(Personajes(nombre_personaje, c_peliculas_participo))
    
while (not pila.pila_vacia()):
    aux = pila.desapilar()
    #PUNTO A
    posicion_rocket += 1
    posicion_groot += 1
    if (aux.nombre_personaje == 'rocket raccoon'):
        print('Rocket Ranccoon se encuentra en la posicion: ', posicion_rocket)
    elif (aux.nombre_personaje == 'groot'):                                   
        print('Groot se encuentra en la posicion: ', posicion_groot)
    #PUNTO C
    elif (aux.nombre_personaje == 'viuda negra'):
        print('Viuda Negra participo en ',aux.c_peliculas_participo,' peliculas')  
    #PUNTO B
    if (aux.c_peliculas_participo > '5'):
        print(aux.nombre_personaje,' aparece en mas de 5 peliculas, participo en ', aux.c_peliculas_participo)  #PUNTO B
  
    pila_aux.apilar(aux)



while (not pila_aux.pila_vacia()):
    aux = pila_aux.desapilar()

    if (aux.nombre_personaje[0] == 'c'):
         print(aux.nombre_personaje,' empieza con c')
          
    if (aux.nombre_personaje[0] == 'd'):
        print(aux.nombre_personaje,' empieza con d')    #PUNTO D
                        
    if (aux.nombre_personaje[0] == 'g'):
        print(aux.nombre_personaje,' empieza con g')
    