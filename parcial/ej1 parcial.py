vector = ['jar bink', 'yoda','gigante', 'palpetine']

def barrido(posicion):
    if (posicion == len(vector)):
        return ''
    else:
        return vector[posicion] + barrido(posicion + 1)
    

#print(barrido(0))

def yoda(posicion):
    if (posicion < len(vector)):
        if (vector[posicion] == 'yodasa'):
            return posicion
        else:
            return yoda(posicion + 1)
    else:
        return -1
    

if (yoda(0) != -1):
    print('YODA ESTA EN LA POSICION:',yoda(0))
else:
    print('YODA NO SE ENCUENTRA')