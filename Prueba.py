# Genero el menu principal como tupla, ya que el menu no se debe alterar
menu_inicial = ("Agregar producto", "Mostrar productos", "Buscar productos", "Eliminar producto", "Salir")
import Funciones

while True:
    Funciones.menu_interactivo(menu_inicial)

    # Genero una variable que vaya guardando la opcion deseada por el user 
    opcion_user = input("Seleciona una opcion: ")

    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea del 1 al 5, si no se cumple ninguna condicion le avisa y le solicita de nuevo
    if opcion_user.isdigit():  
        opcion_user = int(opcion_user)
        if opcion_user >= 1 and opcion_user <= 5:
            if opcion_user == 1:
                print("Selecciono 1")
            elif opcion_user == 2:
                print("Selecciono 2")
            elif opcion_user == 3:
                print("Selecciono 3")
            elif opcion_user == 4:
                print("Selecciono 4")
            elif opcion_user == 5: 
                print("El programa se esta cerrando...Adios!")
                break    
    # Si el user elige una opcion que no esta dentro del rango o el tipo de dato no es el correcto le devuelve un mensaje
        else:
            print("La opcion elegida no esta disponible, selecciona una opcion del 1 al 5")
    else:
        print("La opcion elegida no esta disponible, selecciona una opcion del 1 al 5")