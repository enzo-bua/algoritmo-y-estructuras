from cola import Cola
cola = Cola()



class Personajes(object):
    
    def __init__(self, nombre_personaje, nombre_super, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_super = nombre_super
        self.genero = genero
    
    def __str__(self):
        return self.nombre_personaje+' - '+self.nombre_super+' - '+self.genero
    

for i in range (0, 3):
    nombre_personaje = input('ingrese nombre del personaje: ')
    nombre_super = input('ingrese nombre del superheroe: ')
    genero = input('ingrese su genero (m - f): ')
    cola.arribo(Personajes(nombre_personaje, nombre_super, genero))


nombre_personaje_capitana_marvel = ''
cantidad = cola.tamanio()

i = 0
while (i < cantidad ):
    aux = cola.atencion()
    if (aux.nombre_super == 'capitana marvel'):  # PUNTO A
        nombre_personaje_capitana_marvel = aux.nombre_personaje
    cola.arribo(aux)
    i+= 1


i = 0
print('SUPERHEROES FEMENINOS')
while (i < cantidad ):
    aux = cola.atencion()
    if (aux.genero == 'f'): #PUNTO B
        print(aux.nombre_super)
    cola.arribo(aux)
    i+= 1


i = 0
print('SUPERHEROES MASCULINOS')
while (i < cantidad ):
    aux = cola.atencion()
    if (aux.genero == 'm'):  #PUNTO C
        print(aux.nombre_super)
    cola.arribo(aux)
    i+= 1
    
i = 0
while (i < cantidad ):
    aux = cola.atencion()
    if (aux.nombre_personaje == 'scott lang'):
        nombre_super_scott_lang = aux.nombre_super
    cola.arribo(aux)
    i+= 1
 
    
print('SUPERHEROES QUE EMPIEZAN CON S')
i = 0
while (i < cantidad ):
    aux = cola.atencion()
    if (aux.nombre_personaje[0] == 's'):
        print(aux)
    cola.arribo(aux)
    i+= 1

i = 0
carol_danvers = 0
while (i < cantidad ):
    aux = cola.atencion()
    if (aux.nombre_personaje == 'carol danvers'):
        carol_danvers+= 1
        nombre_super_carol_danvers = aux.nombre_super
    cola.arribo(aux)
    i+= 1



print('El nombre del superheroe de Scott Lang es: ',nombre_super_scott_lang)
print('El nombre superheroe capitana marvel es: ',nombre_personaje_capitana_marvel)

if (carol_danvers == 1):
    print('Carol Danvers esta en la cola, el nombre de su superheroe es: ', nombre_super_carol_danvers)   
else:
    print('Carol Danvers no esta en la cola')