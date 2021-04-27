def numero_binario(numero):
    if (numero == 1) or (numero == 0):
        return str(numero)
    elif  ((numero % 2) == 0) and (numero < 2):
        return str(0)
    else: 
        return str(numero % 2) + numero_binario(numero // 2) 

def invertir_cadena(cadena):#! 6
    if(len(cadena) == 0):
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[0:-1])


print(invertir_cadena(numero_binario(10)))




vector = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num2roman(vector, num, posicion):
    i, r = vector[posicion]
    if (num == 0):
        return ''
    elif (num >= i):
        num -=i
        return r + str(num2roman(vector, num, posicion+1))
    else:
       return num2roman(vector, num, posicion+1)

print(num2roman(vector, 1100, 0))


vector_mochila = ['lata' , 'sable azul' ,'hh','dddd']

def jeidi(vector_mochila,inicio):
    if  (inicio <=  len(vector_mochila)-1):
        if (vector_mochila[inicio] == 'sable azul'):
            return inicio
        else:
            return jeidi(vector_mochila,inicio +1)
    else:
        return -1

    
if (jeidi(vector_mochila,0) == -1):
   print('El zable azul no esta')
else:
    print('El zable azul esta en la posicion ', jeidi(vector_mochila, 0)+1)
    print('tuvo que sacar ',jeidi(vector_mochila, 0)+1)
    
    
    
  
matriz= [[1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 2]]
  
def laberinto(matriz, x, y, caminos=[]):
    """Salida del laberinto."""
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 5
            caminos.append([x, y])
            # print("mover este")
            laberinto(matriz, x, y+1, caminos)
            # print("mover oeste")
            laberinto(matriz, x, y-1, caminos)
            # print("mover norte")
            laberinto(matriz, x-1, y, caminos)
            # print("mover sur")
            laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1
 
laberinto(matriz, 0, 0)            
 

  
  
  
  
  
  
    