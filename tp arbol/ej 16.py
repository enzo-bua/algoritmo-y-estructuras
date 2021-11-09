from arbol_binario import Arbol
tabla = [['Despejado', 0.22], ['Nublado', 0.15], ['Lluvia', 0.03], 
        ['Baja', 0.26], ['Alta', 0.14], ['1', 0.05], ['2', 0.01],
        ['3', 0.035],  ['5', 0.06],  ['7', 0.02],  ['8', 0.025]]

dic = {}

bosque = []


def como_comparo(arbol):
    return arbol.frecuencia


bosque = []

for info, frecuencia in tabla:
    arbol = Arbol(info, frecuencia = frecuencia)
    bosque.append(arbol)


bosque.sort(key=como_comparo)
# for arbol in bosque:
#     print(arbol.info, arbol.frecuencia)

while(len(bosque) > 1):
    arbol1 = bosque.pop(0)
    arbol2 = bosque.pop(0)
    nuevo_arbol = Arbol(frecuencia=arbol1.frecuencia+arbol2.frecuencia)
    nuevo_arbol.izq = arbol1
    nuevo_arbol.der = arbol2
    bosque.append(nuevo_arbol)
    bosque.sort(key=como_comparo)

arbol_huffman = bosque[0]

arbol_huffman.barrido_por_nivel_huff()


def generar_tabla(arbol, cadena='', dic=None):
    if(arbol is not None):
        if(arbol.izq is None):
            dic[arbol.info] = cadena
            # print(arbol.info, cadena)
        else:
            cadena += '0'
            generar_tabla(arbol.izq, cadena, dic)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(arbol.der, cadena, dic)


generar_tabla(arbol_huffman, dic=dic)


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += dic[caracter]
    return cadena_cod


def decodificar(cadena_cod, arbol_huff):
    cadena_deco = ''
    arbol_aux = arbol_huff
    pos = 0
    while(pos < len(cadena_cod)):
        if(cadena_cod[pos] == '0'):
            arbol_aux = arbol_aux.izq
        else:
            arbol_aux = arbol_aux.der
        pos += 1
        if(arbol_aux.izq is None):
            cadena_deco += arbol_aux.info
            arbol_aux = arbol_huff
        # cadena_deco
    return cadena_deco


estado = ['Nublado', 'Baja', '1', '5', '7']

arbol_huffman.barrido_por_nivel_huff()

#generar_tabla(arbol_huffman, dic)


cadena_codificada = codificar(estado, dic)

estado_decodificado = decodificar(cadena_codificada, arbol_huffman)


print('Cadena codificada: ', cadena_codificada)

print('Cadena decodificada: ',estado_decodificado)