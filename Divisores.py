import math


def ObtenertNumeroNatural():
    while True:
        try:
            numNat = int(input("Ingrese un número natural: "))
            if numNat < 1:
                raise ValueError("El número debe ser un número natural.")
            return numNat
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente con otro número natural.")

def Calcular_Divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

if __name__== "__main__":
    numero = ObtenertNumeroNatural()
    divisores = Calcular_Divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")