# Importo las funciones
import Funciones

# Creo la tabla en la DB en caso que no exista, si ya existe continua
Funciones.crear_tabla()

# Genero el menu principal como tupla, ya que el menu no se debe alterar
menu_inicial = ("Agregar producto", "Mostrar productos", "Buscar productos", "Eliminar producto", "Actualizar Producto", "Control de Stock", "Salir")

# Genero el menu de eliminar productos como tupla
menu_eliminar = ("Mostrar productos", "Eliminar producto", "Regresar al menu principal")

# Genero el menu de actualizar productos como tupla
menu_actualizar = ("Mostrar productos", "Actualizar producto", "Regresar al menu principal")

# Genero el menu de agregar productos como tupla
menu_agregar = ("Agregar nuevo producto", "Ver ultimo producto agregado", "Regresar al menu principal")

# Genero el menu de buscar productos como tupla
menu_buscar = ("Buscar un nuevo producto", "Regresar al menu principal")

# Genero el menu de control de stock productos como tupla
menu_stock = ("Control de Stock", "Regresar al menu principal")

# Genero el sub_menu de buscar productos como tupla
sub_menu_buscar = ("Buscar por ID", "Buscar por palabra", "Regresar al menu principal")

# Genero la lista de productos
productos = []

# Genero una lista de etiquetas para mostrar la descripcion de cada producto
etiquetas = ["ID Producto","Nombre","Descripcion","Cantidad","Precio","Categoria"]

# Muestro el menu principal al user
while True:
    Funciones.mostrar_menu(menu_inicial)

    # Genero una variable que vaya guardando la opcion deseada por el user 
    opcion_user = input("Seleciona una opcion: ")

    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea del 1 al 6, si no se cumple ninguna condicion le avisa y le solicita de nuevo
    opcion_user = Funciones.validar_opcion(opcion_user, 1, 7)

    if opcion_user is not None:
                # Genero la opcion 1. Agregar producto. Dejo que el user agregue un producto y luego le ofrezco un nuevo menu con otras opciones
            if opcion_user == 1:
                Funciones.agregar_producto_db()
                                
                # Se genera el nuevo menu interactivo para el user
                while True:
                    Funciones.mostrar_menu(menu_agregar)
                    opcion_agregar = input("Seleciona una opcion: ")

                    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea del 1 al 3, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                    opcion_agregar = Funciones.validar_opcion(opcion_agregar, 1, 3)

                    if opcion_agregar is not None:

                            if opcion_agregar == 1:
                                Funciones.agregar_producto_db()
                            
                            if opcion_agregar == 2:
                                ultimo = Funciones.mostrar_ultimo_producto()
                                print("Producto: ")
                                for producto in range(len(ultimo)):
                                    print(f"{etiquetas[producto]}: {str(ultimo[producto]).capitalize()}")
                            
                            elif opcion_agregar == 3:
                                print("Te dirijo al menu principal!") 
                                break
                    else:
                        print("La opción ingresada no es válida. Elegí una opción del 1 al 3.")
            
            # Genero la opcion 2. Mostrar productos
            elif opcion_user == 2: 
                Funciones.mostrar_producto(etiquetas)

            # Genero la opcion 3. Buscar productos. Dejo que el user busque un producto y luego le ofrezco seguir buscando o volver al menu principal
            elif opcion_user == 3:
                if not Funciones.validar_productos_cargados(productos):
                    continue  
                Funciones.mostrar_menu(sub_menu_buscar)
                opcion_buscar = input("Seleciona una opcion: ")

                # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea 1 o 3, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                opcion_buscar = Funciones.validar_opcion(opcion_buscar, 1, 3)

                if opcion_buscar is not None:

                            if opcion_buscar == 1:
                                Funciones.buscar_producto_id(etiquetas)

                            elif opcion_buscar == 2:
                                Funciones.buscar_producto_texto(etiquetas)    

                            elif opcion_buscar == 3:
                                print("Te dirijo al menu principal!") 
                                break
                else:
                    print("La opción ingresada no es válida. Elegí una opción del 1 al 3.")

                #if not Funciones.buscar_producto_id(etiquetas):
                #    continue
                # Se genera el nuevo menu interactivo para el user
                while True:
                    Funciones.mostrar_menu(menu_buscar)
                    opcion_buscar = input("Seleciona una opcion: ")

                    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea 1 o 2, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                    opcion_buscar = Funciones.validar_opcion(opcion_buscar, 1, 2)

                    if opcion_buscar is not None:

                            if opcion_buscar == 1:
                                Funciones.mostrar_menu(sub_menu_buscar)
                                opcion_buscar_sub= input("Seleciona una opcion: ")

                                # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea 1 o 3, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                                opcion_buscar_sub = Funciones.validar_opcion(opcion_buscar_sub, 1, 3)

                                if opcion_buscar_sub is not None:

                                            if opcion_buscar_sub == 1:
                                                Funciones.buscar_producto_id(etiquetas)

                                            elif opcion_buscar_sub == 2:
                                                Funciones.buscar_producto_texto(etiquetas)    

                                            elif opcion_buscar_sub == 3:
                                                print("Te dirijo al menu principal!") 
                                                break
                                else:
                                    print("La opción ingresada no es válida. Elegí una opción del 1 al 3.")

                            elif opcion_buscar == 2:
                                print("Te dirijo al menu principal!") 
                                break
                            else:
                                print("La opción ingresada no es válida. Elegí una opción del 1 al 2.")

            # Genero la opcion 4. Eliminar producto. Le ofrezco al user un sub-menu para que consulte el numero de productos, elimine o regrese al menu principal
            elif opcion_user == 4: 
                if not Funciones.validar_productos_cargados():
                    continue  
                while True:
                    # Genero un sub-menu para que el user pueda ver el numero del producto, elimarlo o volver al menu anterior
                    Funciones.mostrar_menu(menu_eliminar)
                    opcion_eliminar = input("Seleciona una opcion: ")

                    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea 1 o 2, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                    opcion_eliminar = Funciones.validar_opcion(opcion_eliminar, 1, 3)

                    if opcion_eliminar is not None:

                            if opcion_eliminar == 1:
                                Funciones.mostrar_producto(etiquetas)

                            elif opcion_eliminar == 2:
                                Funciones.eliminar_producto_db()

                            elif opcion_eliminar == 3:
                                print("Te dirijo al menu principal!") 
                                break
                    else:
                        print("La opción ingresada no es válida. Elegí una opción del 1 al 3.")          

            # Genero la opcion 5. Actualizar producto. Le ofrezco al user un sub-menu para que consulte el numero de productos, actualice o regrese al menu principal
            elif opcion_user == 5:
                if not Funciones.validar_productos_cargados():
                    continue  
                while True:
                    # Genero un sub-menu para que el user pueda consultar el stock o volver al menu anterior
                    Funciones.mostrar_menu(menu_actualizar)
                    opcion_actualizar = input("Seleciona una opcion: ")

                    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea 1 2 o 3, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                    opcion_actualizar = Funciones.validar_opcion(opcion_actualizar, 1, 3)

                    if opcion_actualizar is not None:

                            if opcion_actualizar == 1:
                                Funciones.mostrar_producto(etiquetas)

                            elif opcion_actualizar == 2:
                                Funciones.actualizar_producto_db()

                            elif opcion_actualizar == 3:
                                print("Te dirijo al menu principal!") 
                                break
                    else:
                        print("La opción ingresada no es válida. Elegí una opción del 1 al 3.") 

            # Genero la opcion 6. Control de stock. Le ofrezco al user la posibilidad de ver el stock de sus productos y luego le doy un sub-menu para que revise de nuevo o vuelva al menu principal.
            elif opcion_user == 6:
                # Funciones.reporte_baja_cantidad()
                productos = Funciones.reporte_baja_cantidad()
                for producto in range(len(productos)):
                    for descripcion in range(len(productos[producto])):
                        print(f"{etiquetas[descripcion]}: {str(productos[producto][descripcion]).capitalize()}")

                if not Funciones.validar_productos_cargados():
                    continue  
                while True:
                    # Genero un sub-menu para que el user pueda ver el numero del producto, actualizarlo o volver al menu anterior
                    Funciones.mostrar_menu(menu_stock)
                    opcion_stock = input("Seleciona una opcion: ")

                    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea 1 2 o 3, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                    opcion_stock = Funciones.validar_opcion(opcion_stock, 1, 2)

                    if opcion_stock is not None:

                            if opcion_stock == 1:
                                # Funciones.reporte_baja_cantidad()
                                productos = Funciones.reporte_baja_cantidad()
                                for producto in range(len(productos)):
                                    for descripcion in range(len(productos[producto])):
                                        print(f"{etiquetas[descripcion]}: {str(productos[producto][descripcion]).capitalize()}")

                            elif opcion_stock == 2:
                                print("Te dirijo al menu principal!") 
                                break
                    else:
                        print("La opción ingresada no es válida. Elegí una opción del 1 al 2.")   
            
            # Genero la opcion 7. Salir
            elif opcion_user == 7: 
                print("El programa se esta cerrando...Adios!")
                break
    # Si el user elige una opcion que no esta dentro del rango o el tipo de dato no es el correcto le devuelve un mensaje
    else:
        print("La opción ingresada no es válida. Elegí una opción del 1 al 7.")
