from heap import HeapMax

cola = HeapMax()



#punto a
cola.arribo('empleados', 1)
cola.arribo('empleados', 1)
cola.arribo('empleados', 1)

#punto b
print(cola.atencion()[0:-2])

#punto c
cola.arribo('staf de TI', 2)
cola.arribo('staf de TI', 2)

#punto d
cola.arribo('gerente', 3)
print()
#punto e
print(cola.atencion()[0:-2])
print(cola.atencion()[0:-2])

#punto f
cola.arribo('gerente', 3)
cola.arribo('empleados', 1)
cola.arribo('empleados', 1)


print()

while(not cola.vacio()):
    print(cola.atencion()[0:-2])
    # print(cola.elementos)
    # a = input()
