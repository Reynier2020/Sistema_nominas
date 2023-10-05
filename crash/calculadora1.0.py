print("Calculadora 1.0")
print()
print("Elija una funcion")
print("1: Sumar")
print("2: Restar")
eleccion = int(input("Aqui: "))
if eleccion == 1:
    a = int(input("primero: "))
    b = int(input("Segunddo: "))
    c = a + b
    print("El resultado es " + str(c))
if eleccion == 2:
    a = int(input("primero: "))
    b = int(input("segundo: "))
    c = a - b
    print("El resultado es: " + str(c))
