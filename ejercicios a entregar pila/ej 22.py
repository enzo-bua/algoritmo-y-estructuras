from pila import Pila 

class Bitacoras(object):
    def __init__(self, planeta_visitado, captura, recompensa):
        self.planeta_visitado = planeta_visitado 
        self.captura = captura
        self.recompensa = recompensa 
    def __str__(self):
        return self.planeta_visitado +' - '+ self.captura +' - '+ self.recompensa

pila_cazarec1 = Pila() #Boba Fett 
pila_cazarec2 = Pila() #Din Djarin
pila_aux_c1 = Pila()
pila_aux_c2 = Pila()


total_recompensa_caza1 = 0
total_recompensa_caza2 = 0
cantidad_capturas_caza1 = 0
cantidad_capturas_caza2 = 0

print('BOB FETT')
for i in range (0, 2):
    planeta_visitado = input('ingrese planeta visitado ')
    captura = input('ingrese a quien capturo (SI NO OBTUVO CAPTURAS PRESIONE NO) ')
    recompensa = float(input('ingrese recompensa '))
    bitacoras = Bitacoras(planeta_visitado, captura, recompensa)
    pila_cazarec1.apilar(bitacoras)    
    
print('DIN DJARIN')
for i in range (0, 2):
    planeta_visitado = input('ingrese planeta visitado ')
    captura = input('ingrese a quien capturo (SI NO OBTUVO CAPTURAS PRESIONE NO) ')
    recompensa = float(input('ingrese recompensa '))
    bitacoras = Bitacoras(planeta_visitado, captura, recompensa)
    pila_cazarec2.apilar(bitacoras)    
    
print()
 
##PUNTO A Y B
while(not pila_cazarec1.pila_vacia()):
    pila_aux_c1.apilar(pila_cazarec1.desapilar()) #Muestra en orden, ya que estan cargados ordenados por lugar visitado
    
print('LUGARES VISITADOS POR BOB FETT')  

while (not pila_aux_c1.pila_vacia()):
    aux = pila_aux_c1.desapilar()
    print(aux.planeta_visitado)
    total_recompensa_caza1 = total_recompensa_caza1 + aux.recompensa #PUNTO B
    pila_cazarec1.apilar(aux)
           
                         
while(not pila_cazarec2.pila_vacia()):
    pila_aux_c2.apilar(pila_cazarec2.desapilar()) #Muestra en orden, ya que estan cargados ordenados por lugar visitado

print('LUGARES VISITADOS POR DIN DJARIN')

while (not pila_aux_c2.pila_vacia()):
    aux = pila_aux_c2.desapilar()
    print(aux.planeta_visitado)     
    total_recompensa_caza2 = total_recompensa_caza2 + aux.recompensa #PUNTO B
    if(aux.captura != 'no'):
        cantidad_capturas_caza2 += 1   #PUTNO D
    pila_cazarec2.apilar(aux)    

    
while (not pila_cazarec1.pila_vacia()):
    aux = pila_cazarec1.desapilar()
    if (aux.captura == 'han solo'):
        print('Boba Fett capturo a Han Solo en la mision: ',pila_cazarec1.tamanio()+1) #PUNTO C
    if(aux.captura != 'no'):
        cantidad_capturas_caza1 += 1   #PUTNO D
    
    
print()
print('La cantidad recaudo el Bob Fett es: ',total_recompensa_caza1)
print('La cantidad recaudo el Din Djarin es: ',total_recompensa_caza2)
if (total_recompensa_caza1 > total_recompensa_caza2):
    print('Recaudo mas Bob Fett')
elif (total_recompensa_caza1 < total_recompensa_caza2):
    print('Recaudo mas Dian Djarin')
else:
    print('Recaudaron lo mismo')


print('Bob Fett capturo: ',cantidad_capturas_caza1)
print('Din Djarin capturo: ',cantidad_capturas_caza2)
