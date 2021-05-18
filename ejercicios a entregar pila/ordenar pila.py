from pila import Pila

pila = Pila()
pila_aux = Pila()

numeros = [3,50,8,51]

for i in range(0, len(numeros)):
    aux = numeros[i]
    if (pila.pila_vacia()):
        pila.apilar(aux)
    else:
        

        while (not pila.pila_vacia() and aux > pila.elemento_cima() ):
            pila_aux.apilar(pila.desapilar())
        pila.apilar(aux)
    
        while (not pila_aux.pila_vacia()):
            pila.apilar(pila_aux.desapilar())
    
    
while (not pila.pila_vacia()):
    print(pila.desapilar())
        
        
    
