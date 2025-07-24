while True:
    print("-- Menú de opciones --")
    print("1.- Calculo de n números")
    print("2.- Calcular el área de un triángulo")
    print("3.- Verificar si un número es par o impar")
    print("4.- Calcular el promedio de n calificaciones")
    print("5.- Ingresar n números y mostrar el mayor y el menor")
    print("6.- Salir del programa")
    user_option = input("Ingrese el número de la opción que desea ingresar: ")
    print()
    match user_option:
        case "1":
            print("1.- Calculo de n números")
        case "2":
            print("2.- Calcular el área de un triángulo")
        case "3":
            print("3.- Verificar si un número es par o impar")
        case "4":
            print("4.- Calcular el promedio de n calificaciones")
        case "5":
            print("5.- Ingresar n números y mostrar el mayor y el menor")
        case "6":
            print("6.- Salir del programa")
        case _:
            print("Valor invalido, vuelva a intentar")