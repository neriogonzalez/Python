

def conversacion(mensaje):
    print('Hola')
    print('Cómo estás?')
    print(mensaje)
    print('Adios')


opcion = int(input('elige una opción (1,2,3): '))

if opcion == 1:
    conversacion('Elegiste la opción ' + str(opcion))
elif opcion == 2:
    conversacion('Elegiste la opción ' + str(opcion))
elif opcion == 3:
    conversacion('Elegiste la opción ' + str(opcion))
else:
    print('Escribe la opción correcta')
