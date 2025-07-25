def insert_n_numbers():
    number_of_numbers = int(input("Cuantos números quiere ingresar? "))
    max_number = 0
    min_number = 0
    total_suma = 0
    for i in range(number_of_numbers):
        user_numbers = int(input("Escriba el número a guardar: "))
        total_suma = total_suma+user_numbers
        if user_numbers > 0:
            max_number += 1
        else:
            min_number += 1
    print(f"La suma total de los números es de: {total_suma}")
    print(f"El promedio de los números ingresados es de: {total_suma/number_of_numbers}")
    print(f"La cantidad de números positivos es de:{max_number}")
    print(f"La cantidad de números negativos es de: {min_number}")
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
            print("Calculo de n números")
            insert_n_numbers()
        case "2":
            print("Calcular el área de un triángulo")
        case "3":
            print("Verificar si un número es par o impar")
        case "4":
            print("Calcular el promedio de n calificaciones")
        case "5":
            print("Ingresar n números y mostrar el mayor y el menor")
        case "6":
            print("Saliendo del programa")
            break
        case _:
            print("Valor invalido, vuelva a intentar")