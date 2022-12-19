import random
# hacer una aplicacion que el usuario eliga un numero del 0 al 10
# luego eliga el robot
# y si ambos son iguales decir que gano
# si no decir que perdieron

Numbers = input ("Elija un numero del 0 al 10: ")
Rnumbers = random.randint (0, 10)

if Numbers == Rnumbers: print ("Ganaste")
else:
#Para poder desplegar numeros en un texto es necesario usar SRT(Variable) 
    print("Perdiste, el bot eligio " + str(Rnumbers))

        

#a variable la puedes tratar como text, numero, array, etc... 
# ento  nces si dices print(variable + " sirve")
# por que si la variable es texto se concatena con # hay que entender bien el probrema para escribir codigo
# Leí ota vez el enunciado y rebusque en mi mente lo qu1e hacen
# las variables y todo hizo clic
# durisimo veo la terminal manito Estaba intentando a ver si ganaba 
# haz que diga que numero eligio el bot
# haz que si pierde diga el numero que eligio el bot


#Escribelo aqui porque no entiendo hahah