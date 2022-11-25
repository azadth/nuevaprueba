import sys

# Función de exponenciación rápida modular
def exp_rapida(base, exponente, modulo):
    x = 1
    y = base % modulo
    b = exponente
    while (b > 0):
        if ((b % 2) == 0):  # Si b es par...
            y = (y * y) % modulo
            b = b / 2
        else:  # Si b es impar...
            x = (x * y) % modulo
            b = b - 1
    return x


#PROGRAMA PRINCIPAL

# Se pide el número de usuarios implicados y se crea una lista con 'n_usu' posiciones
n_usu = int(input("Introduzca el número de usuarios implicados: "))
usu = []
for i in range(n_usu):
    usu.append({})

# Se pide los números p y raiz por teclado
p = int(input("Introduzca el número primo 'p': "))
alpha = int(input("Introduzca la raiz primitiva 'g': "))
print()

##### Se pide los secretos por teclado y se calcula la primera 'y' de cada usuario #####

for i in range(n_usu):
    usu[i]['x'] = int(input("Usuario " + str(i) + ": Introduzca su 'x' secreto: "))
    print("Usuario " + str(i) + ": Calculando 'y'...", end="")
    # Se calcula el valor de yi
    usu[i]['y'] = exp_rapida(alpha, usu[i]['x'], p)
    print("'y" + str(i) + "' = " + str(usu[i]['y']))
    print()

for i in range(n_usu - 1):
    ##### Se simula el envío de las 'y' generadas #####
    print("--- INTERCAMBIANDO 'y' ---")
    for j in range(n_usu):
        print("Enviando 'y" + str(j) + "' al usuario " + str((j + 1) % n_usu) + "... ", end="")
        usu[(j + 1) % n_usu]['prim'] = usu[j]['y']
        print("Hecho!")
    print()

    ##### Se calcula la nueva 'y' de cada usuario #####
    print("--- CALCULANDO NUEVA 'y' ---")
    for j in range(n_usu):
        print("Usuario " + str(j) + ": Calculando nueva 'y" + str(j) + "'... ", end="")
        # Se calcula el valor de la y
        usu[j]['y'] = exp_rapida(usu[j]['prim'], usu[j]['x'], p)
        print("'y" + str(j) + "' = " + str(usu[j]['y']))
    print()

##### Se muestrala clave de cada uno de los usuarios #####
print("--- CLAVES FINALES ---")
for i in range(n_usu):
    print("Usuario " + str(i) + ": Clave 'k' =  " + str(usu[i]['y']))

sys.exit(0)