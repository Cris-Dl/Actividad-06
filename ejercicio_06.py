from zmq.backend import first


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

def area_triangle():
    base_triangle = float(input("Ingrese la medida de la base del triangulo: "))
    height_triangle = float(input("Ingrese la medida de la altura del triangulo: "))
    print(f"El área del triangulo es de: {base_triangle*height_triangle/2}")

def even_or_odd_number():
    user_number = int(input("Ingrese el número ha revisar: "))
    if user_number%2 == 0:
        print(f"El número {user_number} es par")
    else:
        print(f"El número {user_number} es impar")

def grade_point_average():
    number_of_grades = int(input("Cuantas calificaciones quiere ingresar? "))
    total_grades = 0
    for i in range(number_of_grades):
        user_grades = float(input("Ingrese la calificación: "))
        total_grades = total_grades + user_grades
    print(f"El promedio de calificaciones es de: {total_grades/number_of_grades}")

def greater_or_lesser_number():
    number_of_numbers = int(input("Cuantos números desea ingresar: "))
    first_number = float(input("Ingrese el primer número: "))
    largest_number = first_number
    smaller_number = first_number
    for i in range(number_of_numbers-1):
        user_number = float(input("Ingrese el número: "))
        if user_number > largest_number:
            largest_number = user_number
        elif user_number < smaller_number:
            smaller_number = user_number
    print(f"El número mayor entre todos los que ingresaste es el {largest_number}")
    print(f"El número menor entre todos los  que ingresaste es el {smaller_number}")
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
            print()
        case "2":
            print("Calcular el área de un triángulo")
            area_triangle()
            print()
        case "3":
            print("Verificar si un número es par o impar")
            even_or_odd_number()
            print()
        case "4":
            print("Calcular el promedio de n calificaciones")
            grade_point_average()
            print()
        case "5":
            print("Ingresar n números y mostrar el mayor y el menor")
            greater_or_lesser_number()
            print()
        case "6":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")