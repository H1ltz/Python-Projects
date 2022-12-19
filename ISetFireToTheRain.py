
Cuaderno = []

MeEstoyEjecutando = True
# tal cual eso equivale
# while(True) == while(MeEstoyEjecutando)
# exacto
# ahora debes apagarlo

while(MeEstoyEjecutando): 
    Pregunta = int(input('¿Quieres agregar una nueva tarea? pulsa 0\nSi quieres ver las tareas guardadas pulsa 1\nSi quieres terminar pulsa 2\n'))

    # ¿Quieres agregar una nueva tarea? pulsa 0
    # Si quieres ver las tareas guardadas pulsa 1
    # Si quieres terminar pulsa 2

    if Pregunta == 0:
        Tarea = (input('Escribe tu tarea manito!'))
        Cuaderno.append (Tarea)

        print('Listo manito!')
    elif Pregunta == 1:
        print('>\n'.join(Cuaderno))
    elif Pregunta == 2:
        # son para bloques de codigo, despues te explico que es eso
        MeEstoyEjecutando = False
        print ('Se acabo esta vaina')
    else:
        print('El numero que usted marco es incorrecto, por favor marque un numero correcto')
