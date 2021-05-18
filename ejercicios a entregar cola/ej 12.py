from cola import Cola

cola = Cola()
cola2 = Cola()
cola_combinadas = Cola()

cola.arribo(2)
cola.arribo(4)
cola.arribo(8)
cola.arribo(20)

cola2.arribo(1)
cola2.arribo(6)
cola2.arribo(7)
cola2.arribo(93)

while (not cola.cola_vacia() and not cola2.cola_vacia()):
    aux = cola.atencion()
    aux2 = cola2.atencion()
    if (aux  >  aux2):   
        cola_combinadas.arribo(aux2)
        cola_combinadas.arribo(aux)
    elif (aux  <  aux2):   
        cola_combinadas.arribo(aux)
        cola_combinadas.arribo(aux2)
    else:
        cola_combinadas.arribo(aux)
        cola_combinadas.arribo(aux2)

while (not cola_combinadas.cola_vacia()):
    print(cola_combinadas.atencion())
    