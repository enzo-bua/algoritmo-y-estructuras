from cola import Cola
from pila import Pila

class Notificaciones(object):
    def __init__(self, hora_notificacion, aplicacion, mensaje):
        self.hora_notificacion = hora_notificacion
        self.aplicacion = aplicacion
        self.mensaje = mensaje
    
    def __str__(self):
        return self.hora_notificacion + ' - '+ self.aplicacion + ' - ' + self.mensaje

cola = Cola()
pila = Pila()

cola.arribo(Notificaciones('14:00', 'instagram', 'recibio un me gusta'))
cola.arribo(Notificaciones('16:30', 'facebook', 'recibio un me gusta'))
cola.arribo(Notificaciones('21:20', 'twitter', 'python es el futuro'))
cola.arribo(Notificaciones('14:10', 'facebook', 'recibio solicitud de amistad'))
cola.arribo(Notificaciones('16:00', 'twitter', 'argentina es tendencia'))
cola.arribo(Notificaciones('17:15', 'instagram', 'juan comenzo a seguirte'))
cola.arribo(Notificaciones('23:55', 'twitter', 'nuevo proyecto creado en python'))

def barrido_cola():
    tamanio = cola.tamanio()
    i = 0
    while(i < tamanio):
        aux = cola.atencion()
        print(aux)
        cola.arribo(aux)
        i+= 1

#PUNTO A
def eliminar_facebook():
    """elimina las notificaciones de facebook"""
    tamanio = cola.tamanio()
    i = 0
    while(i < tamanio):
        aux = cola.atencion()
        if(aux.aplicacion != 'facebook'):
            cola.arribo(aux)            
        i+= 1

#PUNTO B
def twitter():
    """muestra notificaciones de twitter cuyo mensaje incluya la palabra python"""
    tamanio = cola.tamanio()
    i = 0
    while(i < tamanio):
        aux = cola.atencion()
        if ((aux.aplicacion == 'twitter') and ('python' in aux.mensaje)):
            print(aux)
        cola.arribo(aux)
        i+= 1

#PUNTO C
def not_instagram():
    """carga en una pila las notificaciones de instagram"""
    tamanio = cola.tamanio()
    i = 0
    while(i < tamanio): 
        aux = cola.atencion()
        if (aux.aplicacion == 'instagram'):
            pila.apilar(aux)
        cola.arribo(aux)
        i+= 1

def barrido_pila():
    while(not pila.pila_vacia()):
        print(pila.desapilar())

barrido_cola()
eliminar_facebook()
print()

barrido_cola()
print()
print('NOTOFICACIONES DE TWITTER CUYO MENSAJE INCLUYE LA PALABRA PYTHON')
twitter()
not_instagram()
print()
print('NOTIFICACIONES DE INSTAGRAM')
barrido_pila()

