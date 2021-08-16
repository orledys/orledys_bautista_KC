"""
    Numeros palíndromos:
    Escriba una función que reciba un numero entero (positivo) o un String
    y entregue como respuesta si la entrada es o no un palíndromo.
"""
import math


def numero_palindromo(numero)->str:
    if numero == int( ''.join( reversed( str(numero) ) ) ):
        return 'ES palindromo'
    else:
        return 'NO es palindromo'

#print( numero_palindromo(17371) )

"""
    Numeros romanos:
    Escriba una función que reciba un numero y retorne como resultado
    el numero romano de dicho número.
"""
def numero_romano(numero)->str:
    u = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    d = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    c = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    if numero >= 100:
        return c[int(str(numero)[0])-1]+d[int(str(numero)[1])-1]+u[int(str(numero)[2])-1]
    elif numero >= 10:
        return d[int(str(numero)[0])-1] + u[int(str(numero)[1])-1]
    else:
        return u[int(str(numero))-1]

#print(numero_romano(981))

"""
    Máximo común divisor:
    Escriba una función que reciba dos numeros 
    y retorne el cálculo de su máximo común divisor. 
"""
def max_comun_divisor(a, b)->int:
    return math.gcd(a,b)

#print(max_comun_divisor(12,18))

"""
    Numeros primos:
    Escriba una función que reciba como entrada un número 
    y determine si es o no un numero primo. 
"""
def es_primo(numero)->str:
    if numero == 2 | numero == 3 | numero == 5 | numero == 7:
        return 'ES primo'
    elif numero % 2 == 0:
        return 'NO es primo'
    else:
        contador = 0
        for i in range(3, int(math.sqrt(numero)), 2):
            if numero % i == 0:
                contador += 1
                break

        if contador == 0:
            return 'ES primo'
        else:
            return 'NO es primo'

#print( es_primo(95) )

"""
    Numeros primos 2:
    Escriba una función que devuelva una lista de numeros primos
    con base a la cantidad que el usuario le solicite,
    Ejemplo si el usuario ingresa 3 
    debe retornar los 3 primeros numeros primos.
"""
def devolver_cantidas_num_primos(numero)->list:
    posibles = []
    primos = [2]
    for i in range(3, numero*5, 2):
        posibles.append(i)

    for i in primos:
        contador = 0
        for j in posibles:
            if contador == 0:
                primos.append(j)
                posibles.remove(j)
            elif j % primos[-1] == 0:
                posibles.remove(j)
            contador += 1

    return primos[:numero]


#print(devolver_cantidas_num_primos(20))

"""
    Numeros primos 3:
    El primo de Mersenne es un numero primo de la forma 2
    𝑝 − 1, una de las propiedades de los primos de Mersenne es que p 
    debe ser también un número primo, escriba una función que
    imprima la cantidad de numeros que el usuario solicite, 
    Ejemplo: si el usuario ingreso 3 los
    primeros primos de Mersenne deberían ser 3, 7 y 31.
"""
def primos_mersenne(cantidad)->list:
    primos = devolver_cantidas_num_primos(cantidad)
    mersenne = []
    for i in range(cantidad):
        mersenne.append( 2**primos[i] - 1 )

    return mersenne

print(primos_mersenne(3))

