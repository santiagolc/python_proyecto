# Genero el menu principal como tupla, ya que el menu no se debe alterar
menu_inicial = ("Agregar producto", "Mostrar productos", "Buscar productos", "Eliminar producto", "Salir")

# Genero el menu de eliminar productos como tupla
menu_eliminar = ("Mostrar productos", "Eliminar producto", "Regresar al menu principal")

# Genero el menu de agregar productos como tupla
menu_agregar = ("Agregar nuevo producto", "Ver ultimo producto agregado", "Regresar al menu principal")

# Genero el menu de buscar productos como tupla
menu_buscar = ("Buscar un nuevo producto", "Regresar al menu principal")

# Genero la lista de productos
productos = []

# Genero la lista temporal que se va ir agregando a la lista final
producto_temp = []

# Genero las variables temporales que van almacenar los datos del producto
nombre = ""
categoria = ""
precio = 0

# Genero una lista de etiquetas para mostrar la descripcion de cada producto
etiquetas = ["Nombre", "Categoria", "Precio"]


# Muestro el menu principal al user
while True:
    for i in range(len(menu_inicial)):
        print(f"{i+1}. {menu_inicial[i]}")

    # Genero una variable que vaya guardando la opcion deseada por el user 
    opcion_user = input("Seleciona una opcion: ")

    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea del 1 al 5, si no se cumple ninguna condicion le avisa y le solicita de nuevo
    if opcion_user.isdigit():  
        opcion_user = int(opcion_user)
        if opcion_user >= 1 and opcion_user <= 5:

            # Genero la opcion 1. Agregar producto. Dejo que el user agregue un producto y luego le ofrezco un nuevo menu con otras opciones
            if opcion_user == 1:
                producto_temp = []

                # Valido que los datos que ingresa sean los correctos segun el dato que tiene que ingresar
                # Bloque codigo Nombre producto
                nombre = ""
                while nombre == "":
                    nombre = input("Agrega el nombre del producto: ").strip()
                    if nombre.isdigit():
                        print("Debes ingresar un nombre, no podes ingresar valores numericos")
                        nombre = ""
                    elif nombre == '':
                        print("Debes ingresar un nombre, no podes dejar el espacio en blanco")
                        nombre = ""
                producto_temp.append(nombre)

                # Bloque codigo Categoria producto
                categoria = ""
                while categoria == "":
                    categoria = input("Agrega la categoria del producto: ").strip()
                    if categoria.isdigit():
                        print("Debes ingresar una categoria, no podes ingresar valores numericos")
                        categoria = ""
                    elif categoria == '':
                        print("Debes ingresar una categoria, no podes dejar el espacio en blanco")
                        categoria = ""
                producto_temp.append(categoria)

                # Bloque codigo Precio producto
                precio = ""
                while precio == "":
                    precio = input("Agrega el precio del producto: ").strip()
                    if precio.isdigit() :
                        precio = int(precio)
                        producto_temp.append(precio)
                    else:  
                        print("Debes ingresar un precio, no podes ingresar letras, signos ni dejar el espacio en blanco")
                        precio = ""
                productos.append(producto_temp)
                print("Agregaste correctamente un nuevo Producto!")
                
                # Se genera el nuevo menu interactivo para el user
                while True:
                    for i in range(len(menu_agregar)):
                        print(f"{i+1}. {menu_agregar[i]}")
                    opcion_agregar = input("Seleciona una opcion: ")

                    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea del 1 al 3, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                    if opcion_agregar.isdigit():  
                        opcion_agregar = int(opcion_agregar)
                        if opcion_agregar >= 1 and opcion_agregar <= 3:

                            if opcion_agregar == 1:
                                producto_temp = []
                                
                                # Valido que los datos que ingresa sean los correctos segun el dato que tiene que ingresar
                                # Bloque codigo Nombre producto
                                nombre = ""
                                while nombre == "":
                                    nombre = input("Agrega el nombre del producto: ").strip()
                                    if nombre.isdigit():
                                        print("Debes ingresar un nombre, no podes ingresar valores numericos")
                                        nombre = ""
                                    elif nombre == '':
                                        print("Debes ingresar un nombre, no podes dejar el espacio en blanco")
                                        nombre = ""
                                producto_temp.append(nombre)

                                # Bloque codigo Categoria producto
                                categoria = ""
                                while categoria == "":
                                    categoria = input("Agrega la categoria del producto: ").strip()
                                    if categoria.isdigit():
                                        print("Debes ingresar una categoria, no podes ingresar valores numericos")
                                        categoria = ""
                                    elif categoria == '':
                                        print("Debes ingresar una categoria, no podes dejar el espacio en blanco")
                                        categoria = ""
                                producto_temp.append(categoria)

                                # Bloque codigo Precio producto
                                precio = ""
                                while precio == "":
                                    precio = input("Agrega el precio del producto: ").strip()
                                    if precio.isdigit() :
                                        precio = int(precio)
                                        producto_temp.append(precio)
                                    else:  
                                        print("Debes ingresar un precio, no podes ingresar letras, signos ni dejar el espacio en blanco")
                                        precio = ""
                                productos.append(producto_temp)
                                print("Agregaste correctamente un nuevo Producto!")
                            
                            if opcion_agregar == 2:
                                print("Producto: ")
                                for producto in range(len(producto_temp)):
                                    print(f"{etiquetas[producto]}: {str(producto_temp[producto]).capitalize()}")
                            
                            elif opcion_agregar == 3:
                                print("Te dirijo al menu principal!") 
                                break
                        else:
                            print("La opcion seleccionada no esta disponible, selecciona una opcion del 1 al 3")
                    else:
                        print("La opcion seleccionada no esta disponible, selecciona una opcion del 1 al 3")

            # Genero la opcion 2. Mostrar productos
            elif opcion_user == 2: 
                if not productos:
                    print("No tenes productos cargados para mostrar, primero deberias de cargar algun producto.")
                    continue
                else:  
                    for producto in range(len(productos)):
                        print(f"Producto {producto +1}:" )
                        for descripcion in range(len(productos[producto])):
                            print(f"{etiquetas[descripcion]}: {str(productos[producto][descripcion]).capitalize()}")

            # Genero la opcion 3. Buscar productos. Dejo que el user busque un producto y luego le ofrezco seguir buscando o volver al menu principal
            elif opcion_user == 3:
                if not productos:
                    print("No tenes productos cargados para buscar, primero deberias de cargar algun producto.")
                    continue
                else:
                    palabra = input("¿Que producto estas buscando? Ingresa una palabra o el nombre del producto: ")
                    contador = 0
                    for producto in range(len(productos)):
                        for descripcion in range(len(productos[producto])):
                            if palabra.lower() in str(productos[producto][descripcion]).lower():
                                contador += 1
                                print(f"Producto {producto + 1}:")
                                for i in range(len(productos[producto])):
                                    print(f"{etiquetas[i]}: {str(productos[producto][i]).capitalize()}")
                                break
                    if contador == 0:
                        print("La palabra o el producto no existen")

                # Se genera el nuevo menu interactivo para el user
                while True:
                    for i in range(len(menu_buscar)):
                        print(f"{i+1}. {menu_buscar[i]}")
                    opcion_buscar = input("Seleciona una opcion: ")

                    # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea 1 o 2, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                    if opcion_buscar.isdigit():  
                        opcion_buscar = int(opcion_buscar)
                        if opcion_buscar >= 1 and opcion_buscar <= 2:

                            if opcion_buscar == 1:
                                palabra = input("¿Que producto estas buscando? Ingresa una palabra o el nombre del producto: ")
                                contador = 0
                                for producto in range(len(productos)):
                                    for descripcion in range(len(productos[producto])):
                                        if palabra.lower() in str(productos[producto][descripcion]).lower():
                                            contador += 1
                                            print(f"Producto {producto + 1}:")
                                            for i in range(len(productos[producto])):
                                                print(f"{etiquetas[i]}: {str(productos[producto][i]).capitalize()}")
                                            break
                                if contador == 0:
                                    print("La palabra o el producto no existen")

                            elif opcion_buscar == 2:
                                print("Te dirijo al menu principal!") 
                                break
                        else:
                            print("La opcion seleccionada no esta disponible, selecciona una opcion entre 1 y 2")
                    else:
                        print("La opcion seleccionada no esta disponible, selecciona una opcion entre 1 y 2")

            # Genero la opcion 4. Eliminar producto. Le ofrezco al user un sub-menu para que consulte el numero de productos, elimine o regrese al menu principal
            elif opcion_user == 4: 
                if not productos:
                    print("No tenes productos cargados para eliminar, primero deberias de cargar algun producto.")
                    continue
                else:    
                    while True:
                        # Genero un sub-menu para que el user pueda ver el numero del producto, elimarlo o volver al menu anterior
                        for i in range(len(menu_eliminar)):
                            print(f"{i+1}. {menu_eliminar[i]}")
                        opcion_eliminar = input("Seleciona una opcion: ")

                        # Verifico que sea un numero lo que ingresa el usuario si es true castea a int y verifica que la opcion sea 1 o 2, si no se cumple ninguna condicion le avisa y le solicita de nuevo
                        if opcion_eliminar.isdigit():  
                            opcion_eliminar = int(opcion_eliminar)
                            if opcion_eliminar >= 1 and opcion_eliminar <= 3:

                                if opcion_eliminar == 1:
                                    if not productos:
                                        print("Ya no tenes productos cargados para eliminar, primero deberias de cargar algun producto.")
                                        continue
                                    else:
                                        for producto in range(len(productos)):
                                            print(f"Producto {producto +1}:" )
                                            for descripcion in range(len(productos[producto])):
                                                print(f"{etiquetas[descripcion]}: {str(productos[producto][descripcion]).capitalize()}")

                                elif opcion_eliminar == 2:
                                    if not productos:
                                        print("Ya no tenes productos cargados para eliminar, primero deberias de cargar algun producto.")
                                        continue
                                    else:
                                        borrar_producto = int(input("Selecciona el numero del producto que queres borrar: "))
                                        print(len(productos))
                                        if (borrar_producto < 1) or (borrar_producto > len(productos)):
                                            print("La opcion elegida no es correcta, elegi el numero de un producto correcto.")
                                        else:
                                            print(f"Elimanaste el producto correctamente! {str(productos[borrar_producto -1]).capitalize()} ya no existe en la base de datos.")
                                            productos.pop(borrar_producto -1)

                                elif opcion_eliminar == 3:
                                    print("Te dirijo al menu principal!") 
                                    break
                            else:
                                print("La opcion seleccionada no es correcta, selecciona una opcion del 1 al 3")  
                        else:
                            print("La opcion seleccionada no es correcta, selecciona una opcion del 1 al 3")          

            # Genero la opcion 5. Salir
            elif opcion_user == 5: 
                print("El programa se esta cerrando...Adios!")
                break
    # Si el user elige una opcion que no esta dentro del rango o el tipo de dato no es el correcto le devuelve un mensaje
        else:
            print("La opcion elegida no esta disponible, selecciona una opcion del 1 al 5")
    else:
        print("La opcion elegida no esta disponible, selecciona una opcion del 1 al 5")