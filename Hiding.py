
import random #Usamos import random, para agregar una libreria a nuestro proyecto (random, es una libreria)

Accion = input("Elija: Piedra, Papel o Tijera ") #Siempre los input son string, es decir, python lo lee como texto

# <Selecion del bot>
SeleccionDelBot = random.randint(0, 2) #Recuerda que una sola = es asignar. #Aqui asignamos a SeleccionDelBot la funcion randint mas el rango de numero que seran randoms.

if SeleccionDelBot == 0:
    SeleccionDelBot = "Piedra" #Si el random sale 0, entonces SeleccionDelBot valdra Piedra, asi con los demas
elif SeleccionDelBot == 1:
    SeleccionDelBot = "Papel" 
elif SeleccionDelBot == 2:
    SeleccionDelBot = "Tijera"
# </Selecion del bot>
# Eso queria que me dijeras :D SIP SIP
# <Averiguar quien gano> 
#Aqui comparamos, para eso usamos and.  Si el bot saco piedra y el jugador (Accion) saca piedra tambien, entonces es empate. Asi se lee
if SeleccionDelBot == "Piedra" and Accion == "Piedra": print ("Empate")
elif SeleccionDelBot == "Piedra" and Accion == "Papel": print ("Gano El Jugador")
elif SeleccionDelBot == "Piedra" and Accion == "Tijera": print ("Gano El Bot")

elif SeleccionDelBot == "Papel" and Accion == "Piedra": print ("Gano El Bot")
elif SeleccionDelBot == "Papel" and Accion == "Papel": print ("Empate")
elif SeleccionDelBot == "Papel" and Accion == "Tijera": print ("Gano El Jugador")

elif SeleccionDelBot == "Tijera" and Accion == "Piedra": print ("Gano El Jugador")
elif SeleccionDelBot == "Tijera" and Accion == "Papel": print ("Gano el Bot")
elif SeleccionDelBot == "Tijera" and Accion == "Tijera": print ("Empate")
# </Aceriguar quien gano>