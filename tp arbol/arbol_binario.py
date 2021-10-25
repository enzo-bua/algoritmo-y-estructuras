
from cola import Cola


class Arbol(object):

    def __init__(self, info=None, datos=None, frecuencia = None):
        self.frecuencia = frecuencia
        self.info = info
        self.datos = datos
        self.der = None
        self.izq = None
        self._altura = 0

    def arbol_vacio(self):
        return self.info is None
    
    def altura(self, arbol):
        if(arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura(self):
        if(self is not None):
            altura_izq = self.altura(self.izq)
            altura_der = self.altura(self.der)
            self._altura = (altura_izq if altura_izq > altura_der else altura_der) + 1
    
    def rotacion_simple(self, control):
        if(control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else:
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura()
        aux.actualizar_altura()
        return aux

    def rotacion_doble(self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos=None):
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden()
            print(self.info)
            if(self.der is not None):
                self.der.inorden()

    def postorden(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden(self):
        if(self.info is not None):
            print(self.info, self._altura)
            if(self.izq is not None):
                self.izq.preorden()
            if(self.der is not None):
                self.der.preorden()

    def busqueda(self, clave):
        pos = None
        if(self.info is not None):
            if(self.info == clave):
                pos = self
            elif(clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif(self.der is not None):
                pos = self.der.busqueda(clave)
        return pos
    
    def busqueda_proximidad(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)

    def remplazar(self):
        """Determina el nodo que remplazará al que se elimina."""
        info, datos = None, None
        if(self.der is None):
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
                self.datos = self.izq.datos
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.remplazar()
        return info, datos

    def eliminar_nodo(self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.remplazar()
                    self.info = info_aux
                    self.datos = datos_aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        # self = self.balancear()
        self.actualizar_altura()
        return info, datos
    
    def contar_ocurrencias(self, buscado):
        cantidad = 0
        if(self.info is not None):
            if(self.info == buscado):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad
    
    def contar_pares_impares(self):
        pares, impares = 0, 0
        if(self.info is not None):
            if(self.info % 2 == 0):
                pares += 1
            else:
                impares += 1
            if(self.izq is not None):
                par, impar = self.izq.contar_pares_impares()
                pares += par
                impares += impar
            if(self.der is not None):
                par, impar = self.der.contar_pares_impares()
                pares += par
                impares += impar
        return pares, impares

    def barrido_por_nivel(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)    

    def barrido_por_nivel_huff(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info, nodo.datos)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)

    def busqueda_proximidad(self, clave):
            if(self.info is not None):
                if(self.izq is not None):
                    self.izq.busqueda_proximidad(clave)
                if(self.info[0:len(clave)] == clave):
                    print(self.info)
                if(self.der is not None):
                    self.der.busqueda_proximidad(clave)

    #EJERCICIO 5
    def empieza_con_c(self):
        """muestra superheroes que empiezan con c"""
        if(self.info is not None):
            if(self.datos['superheroe'] == True):
                if(self.info[0] == 'c'):
                    print(self.info, 'Empieza con C')
                if (self.izq is not None):
                    self.izq.empieza_con_c()
                if(self.der is not None):
                    self.der.empieza_con_c()
           
    
    
    def cantidad_superheroes(self):
        """cantidad de superheroes"""
        cantidad_super = 0
        if(self.info is not None):
            if(self.datos['superheroe'] == True):
                cantidad_super += 1
            if(self.izq is not None):
                cantidad_super+= self.izq.cantidad_superheroes()
            if(self.der is not None):
                cantidad_super+= self.der.cantidad_superheroes()
        return cantidad_super

    def inorden_villanos(self):
        if(self.info is not None):
            if(self.datos['superheroe'] == False):
                print(self.info)
            if(self.izq is not None):
                self.izq.inorden_villanos()
            if(self.der is not None):
                self.der.inorden_villanos()


    def dos_arboles(self,arbol_superheroes, arbol_villanos):
        if(self.info is not None):
                if(self.datos['superheroe'] == True):
                    arbol_superheroes = arbol_superheroes.insertar_nodo(self.info, self.datos)
                else:
                    arbol_villanos = arbol_villanos.insertar_nodo(self.info, self.datos)
                if(self.izq is not None):
                    self.izq.dos_arboles(arbol_superheroes, arbol_villanos)
                if(self.der is not None):
                    self.der.dos_arboles(arbol_superheroes, arbol_villanos)

    def cantidad_nodos(self):
        contador_nodos = 0
        if(self.info is not None):
            contador_nodos +=1 
            if(self.izq is not None):
                contador_nodos += self.izq.cantidad_nodos()
            if(self.der is not None):
                contador_nodos += self.der.cantidad_nodos()
        return contador_nodos

    def listado_descendiente(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.listado_descendiente()
            if(self.datos['superheroe'] == True):
                print(self.info)
            if(self.izq is not None):
                self.izq.listado_descendiente()

    def dato_mal_cargado(self):
        """modifica usuario mal cargado, cambia nombre"""
        buscado = input('ingrese lo que desa buscar ')
        self.busqueda_proximidad(buscado)
        buscado_modificar = input('ingrese el nombre que desea modificar ')
        pos = self.busqueda(buscado_modificar)
        if(pos):
            nuevo_nombre = input('ingrese el nuevo nombre ')
            nombre,datos = self.eliminar_nodo(buscado_modificar)
            datos['name'] = nuevo_nombre
            self.insertar_nodo(nombre, datos)
    #FIN EJERCICIO 5

    # def dioses(self, v_dioses):  CARGA NOMBRES SIN REPETIRLOS, PASO EL VECTOR DESDE AFUERA
    #     if(self.info is not None):
    #         if (self.datos['derrotado'] not in v_dioses):
    #             v_dioses.append(self.datos['derrotado'])
    #         if(self.izq is not None):
    #             self.izq.dioses(v_dioses)
    #         if(self.der is not None):
    #             self.der.dioses(v_dioses)
    #     return v_dioses

    #EJERCICIO 23

    def inorden_criaturas(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_criaturas()
            print(self.datos['name'],'--', self.datos['derrotado'])
            if(self.der is not None):
                self.der.inorden_criaturas()

                
    def conta_criaturas_derrotadas(self, dic):
        """cuenta que dioses derroto mas criaturas"""
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.conta_criaturas_derrotadas(dic)
            if(self.datos['derrotado'] in dic):
                dic[self.datos['derrotado']] += 1 #si esta lo va incrementando
            else:
                dic[self.datos['derrotado']] = 1 #lo asigna y lo pone en 1
            if(self.der is not None):
                self.der.conta_criaturas_derrotadas(dic)

    def listar_criaturas_derrotadas(self, aux):
        """lista criaturas derrotadas, pasar nombre de x quien fuerron derrotadas"""
        if(self.info is not None):
            if (self.datos['derrotado'] == aux):
                print(self.info)
            if (self.izq is not None):
                self.izq.listar_criaturas_derrotadas(aux)
            if (self.der is not None):
                self.der.listar_criaturas_derrotadas(aux)

    def listar_criaturas_capturadas(self, aux):
        """lista criaturas capturadas, pasar nombre de x quien fuerron derrotadas"""
        if(self.info is not None):
            if (self.datos['capturada'] == aux):
                print(self.info)
            if (self.izq is not None):
                self.izq.listar_criaturas_capturadas(aux)
            if (self.der is not None):
                self.der.listar_criaturas_capturadas(aux)

    def eliminar_nodos_iguales(self, buscado):
        """elimina nodos iguales, pasar a quien eliminar"""
        cantidad = self.contar_ocurrencias(buscado)
        for i in range(cantidad):
            self.eliminar_nodo(buscado)

    def listado_arbol(self, campo, clave):
        """listado, pasar campo y clave"""
        if(self.info is not None):
            if (self.datos[campo] == clave):
                print(self.info)
            if (self.izq is not None):
                self.izq.listado_arbol(campo, clave)
            if (self.der is not None):
                self.der.listado_arbol(campo, clave)
        