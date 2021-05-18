from pila import Pila 

pila_episodio_V = Pila()
pila_episodio_VII = Pila()
pila_aux = Pila()

print('PERSONAJES EPISODIO V')
for i in range(0, 3):
    personaje = input('ingrese personaje: ')
    pila_episodio_V.apilar(personaje)
    

print('PERSONAJES EPISODIO VII')
for i in range(0, 3):
    personaje = input('ingrese personaje: ')
    pila_episodio_VII.apilar(personaje)



while (not pila_episodio_V.pila_vacia()):    
    aux_pila_epV = pila_episodio_V.desapilar()  
    while (not pila_episodio_VII.pila_vacia()):
        aux_pila_epVII = pila_episodio_VII.desapilar()      
        if (aux_pila_epV == aux_pila_epVII ):
            print('El personaje ',aux_pila_epVII, ' aparece en ambos episodios')
        pila_aux.apilar(aux_pila_epVII)
    while (not pila_aux.pila_vacia()):
        pila_episodio_VII.apilar(pila_aux.desapilar())
