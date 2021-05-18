from cola import Cola

class Personajes(object):
    def __init__(self, nombre, planeta_origen):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
    
    def __str__ (self):
        return self.nombre + ' - '+ self.planeta_origen 

cola = Cola()
planeta_origen_luke = ''
planeta_origen_hansolo = ''

for i in range (0, 3):
    nombre = input('ingrese nombre del personaje: ')
    planeta_origen = input('ingrese planeta de origen: ')
    cola.arribo(Personajes(nombre, planeta_origen))
  
i = 0
cantidad = cola.tamanio()

while (i < cantidad ):
    aux = cola.atencion()
    if (aux.planeta_origen == 'alderaan'):
        print(aux)
    elif (aux.planeta_origen == 'endor'):  #PUNTO A
        print(aux)
    elif (aux.planeta_origen == 'tatooine'):
        print(aux)
    cola.arribo(aux)
    i += 1
    
i = 0
while (i < cantidad ):
    aux = cola.atencion()
    if (aux.nombre == 'luke skywalker'):
        planeta_origen_luke = aux.planeta_origen  #PUNTO B
    elif (aux.nombre == 'han solo'):
        planeta_origen_hansolo = aux.planeta_origen
    cola.arribo(aux)  
    i += 1
 
    
 
    
i = 0
while (i < cantidad):
    aux = cola.atencion()
    if (aux.nombre == 'yoda'):
        nuevo_personaje =input('ingrese nombre del persoaje agregar: ') #PUNTO C
        planeta_origen_nv =input('ingrese su planeta de origen: ')
        cola.arribo(Personajes(nuevo_personaje, planeta_origen_nv))
    cola.arribo(aux)
    i += 1  
    
i = 0
  
while (i < cantidad):
    aux = cola.atencion()
    if (aux.nombre == 'jar binks'): #PUNTO D
        cola.arribo(aux)
        borrar = cola.atencion()
        i+=1
    else:
        cola.arribo(aux)
    i+= 1
    
    
i = 0
while(i < cola.tamanio()):
    aux = cola.mover_final()  #BARRIDO
    print(aux)
    i+= 1    
    
print('El planeta natal de luke skywalker es : ',planeta_origen_luke)   
print('El planeta natal de Han Solo es : ',planeta_origen_hansolo)  