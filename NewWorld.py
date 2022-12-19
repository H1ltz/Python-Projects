##La lampara no funciona

Lampara = int(input("¿La lampara esta conectada? ingrese 1 si es Si, si no esta conectada ingrese cualquier numero"))
if not Lampara == 1:
    print("Conecta la lampara")
else: 
    print("El bombillo ta quemao");

Lampara2 = int(input("¿El bombillo ta quemao? ingrese 1 si ta quemao sino, ingrese cualquier numero"))
if Lampara2 == 1: 
    print("Cambie el bombillo")
else:
    print("Repare la lampara")