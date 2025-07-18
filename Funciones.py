import sqlite3

# Funcion que permite conectarse a la base de datos
def conectar():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    return conexion, cursor

# Funcion que permite crear la tabla de productos
def crear_tabla():
    conexion, cursor = conectar()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    conexion.commit()
    conexion.close()

# Funcion que permite recorrer una tupla y mostrarlo como menu
def mostrar_menu(tupla):
    for i in range(len(tupla)):
        print(f"{i+1}. {tupla[i]}")

# Funcion que permite validar si la opcion elegida por un usuario es un numero y dentro del rango necesario
def validar_opcion(opcion_str, minimo, maximo):
    if opcion_str.isdigit():
        opcion_int = int(opcion_str)
        if minimo <= opcion_int <= maximo:
            return opcion_int
    return None        

# Funcion para validar que no se ingresa un numero o un espacio en blanco donde deberia ir texto
def validar_texto(valor_ingresado, texto):
    if valor_ingresado.isdigit():
        return False
    elif valor_ingresado == '':
        return False
    return True

# Funcion para validar que solo se ingresen numeros
def validar_numero(valor_ingresado):
    try:
        valor_ingresado = int(valor_ingresado)
        return True
    except ValueError:
        return False

# Funcion para validar que solo se ingresen datos tipo float
def validar_float(valor_ingresado):
    try:
        valor_ingresado = float(valor_ingresado)
        if valor_ingresado > 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
# Funcion para validar que solo se ingresen datos tipo int
def validar_int(valor_ingresado):
    try:
        valor_ingresado = int(valor_ingresado)
        if valor_ingresado >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

# Funcion que permite agregar un producto
def agregar_producto(temporal, final):
    # Bloque codigo Nombre producto
    while True:
        nombre = input("Agrega el nombre del producto: ").strip()
        if validar_texto(nombre, "nombre"):
            break
        else: 
            print("Debes ingresar un nombre valido, no podes ingresar valores numericos ni dejar espacios vacios")
    temporal.append(nombre)

    # Bloque codigo Categoria producto
    while True:
        categoria = input("Agrega la categoria del producto: ").strip()
        if validar_texto(categoria, "categoria"):
            break
        else: 
            print("Debes ingresar una categoria valida, no podes ingresar valores numericos ni dejar espacios vacios")
    temporal.append(categoria)

    # Bloque codigo Precio producto
    while True:
        precio = input("Agrega el precio del producto: ").strip()
        if validar_numero(precio):
            precio = int(precio) 
            temporal.append(precio)
            break
        else:
            print("Debes ingresar un precio, no podes ingresar letras, signos ni dejar el espacio en blanco")
    final.append(temporal)
    print("Agregaste correctamente un nuevo Producto!")

# Funcione que permite validar si hay o no productos cargados
def validar_productos_cargados():
    conexion, cursor = conectar()
    cursor.execute("SELECT COUNT(*) FROM productos")
    conteo = cursor.fetchone()[0]
    conexion.close()
    if conteo == 0:
        print("No tenes productos cargados para realizar esta accion, primero deberias cargar algun producto.")
        return False
    return True

# Funcion que permite traer los productos
def productos_db():
    conexion, cursor = conectar()
    cursor.execute("SELECT * FROM productos")
    producto = cursor.fetchall()
    conexion.close()
    return producto

# Funcion que permite mostrar un producto
def mostrar_producto(etiquetas):
    if not validar_productos_cargados():
        return
    productos = productos_db()
    for producto in range(len(productos)):
        for descripcion in range(len(productos[producto])):
            print(f"{etiquetas[descripcion]}: {str(productos[producto][descripcion]).capitalize()}")

# Funcion que permite buscar un producto por ID
def buscar_producto_id(etiquetas):
    if not validar_productos_cargados():
        return False
    id_busqueda = input("¿Que producto estas buscando? Ingresá el ID del producto que querés buscar: ")
    contador = 0
    productos = productos_db()
    for producto in range(len(productos)):
        for i in range(len(productos[producto])):
            if id_busqueda == str(productos[producto][0]):
                contador += 1
                for i in range(len(productos[producto])):
                    print(f"{etiquetas[i]}: {str(productos[producto][i]).capitalize()}")
                break
    if contador == 0:
        print("El ID no existe")
        return False
    return True

# Funcion que permite buscar un producto por texto
def buscar_producto_texto(etiquetas):
    if not validar_productos_cargados():
        return False
    palabra = input("¿Que producto estas buscando? Ingresa una palabra o el nombre del producto: ").strip()
    contador = 0
    productos = productos_db()
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
        return False
    return True

# Funcion que permite eliminar un producto
def eliminar_producto(productos):
    if not validar_productos_cargados(productos):
        return
    borrar_producto_str = input("Selecciona el número del producto que querés borrar: ").strip()
    if not borrar_producto_str.isdigit():
        print("Debes ingresar un número válido.")
        return
    borrar_producto = int(borrar_producto_str)
    if borrar_producto < 1 or borrar_producto > len(productos):
        print("La opción elegida no es correcta, elegí el número de un producto correcto.")
        return
    print(f"Eliminaste el producto correctamente! {str(productos[borrar_producto - 1]).capitalize()} ya no existe en la base de datos.")
    productos.pop(borrar_producto - 1)    

# Funcion que permite captar los datos necesarios para agregar un producto
def datos_producto_db():
    # Bloque codigo Nombre producto
    while True:
        nombre = input("Agrega el nombre del producto: ").strip()
        if validar_texto(nombre, "nombre"):
            break
        else: 
            print("Debes ingresar un nombre valido, no podes ingresar valores numericos ni dejar espacios vacios")

    # Bloque codigo Descripcion producto
    while True:
        descripcion = input("Agrega la descripcion del producto: ").strip()
        if validar_texto(descripcion, "descripcion"):
            break
        else: 
            print("Debes ingresar una categoria valida, no podes ingresar valores numericos ni dejar espacios vacios")
  
    # Bloque codigo Cantidad producto
    while True:
        cantidad = input("Agrega la cantidad del producto: ").strip()
        if validar_int(cantidad):
            cantidad = int(cantidad) 
            break
        else:
            print("Debes ingresar una cantidad, no podes ingresar letras, signos ni dejar el espacio en blanco")
    
    # Bloque codigo Precio producto
    while True:
        precio = input("Agrega el precio del producto: ").strip()
        if validar_float(precio):
            precio = float(precio) 
            break
        else:
            print("Debes ingresar un precio, no podes ingresar letras, signos ni dejar el espacio en blanco")
    
    # Bloque codigo Categoria producto
    while True:
        categoria = input("Agrega la categoria del producto: ").strip()
        if validar_texto(categoria, "categoria"):
            break
        else: 
            print("Debes ingresar una categoria valida, no podes ingresar valores numericos ni dejar espacios vacios")

    return nombre, descripcion, cantidad, precio, categoria

# Funcion que permite agregar un producto a la db
def agregar_producto_db():
    conexion, cursor = conectar()
    nombre,descripcion,cantidad,precio,categoria = datos_producto_db()
    try:
        conexion.execute("BEGIN")

        cursor.execute("INSERT INTO productos (nombre,descripcion,cantidad,precio,categoria) VALUES (?,?,?,?,?)",(nombre,descripcion,cantidad,precio,categoria))

        print("Agregaste correctamente un nuevo Producto!")
            
        conexion.commit()
    except sqlite3.IntegrityError as error:
        conexion.rollback()
        print(f"Error al cargar el producto: {error}")
    except Exception as error:
                conexion.rollback()
                print(f"Ocurrio un error: {error}")
    finally:
        conexion.close()

# Funcion que permite mostrar el ultimo producto agregado a la db
def mostrar_ultimo_producto():
    conexion, cursor = conectar()
    cursor.execute("SELECT * FROM productos ORDER BY id DESC LIMIT 1")
    producto = cursor.fetchone()
    conexion.close()
    return producto

# Funcio que permite obtener un producto por id
def obtener_producto_id():
    if not validar_productos_cargados():
        return False
    id_busqueda = input("¿Qué producto estás buscando? Ingresá el ID del producto: ")
    productos = productos_db()

    for producto in productos:
        if str(producto[0]) == id_busqueda:
            return producto

    print("El ID no existe")
    return False

# Funcion que permite eliminar un producto
def eliminar_producto_db():
    if not validar_productos_cargados():
        return False
    conexion, cursor = conectar()
    productos = productos_db()
    borrar_producto_str = input("Selecciona el número del producto que querés borrar: ").strip()
    if not borrar_producto_str.isdigit():
        print("Debes ingresar un número válido.")
        return
    borrar_producto = int(borrar_producto_str)
    if borrar_producto < 1 or borrar_producto > len(productos):
        print("La opción elegida no es correcta, elegí el número de un producto correcto.")
        return
    print(f"Eliminaste el producto correctamente! {str(productos[borrar_producto - 1][0]).capitalize()} ya no existe en la base de datos.")

    cursor.execute(f"DELETE FROM productos WHERE id = {productos[borrar_producto - 1][1]}")
    conexion.commit()
    conexion.close()

# Funcion que permite actualizar un producto
def actualizar_producto_db(etiquetas):
    if not validar_productos_cargados():
        return False
    conexion, cursor = conectar()

    while True:
        actualizar_producto = obtener_producto_id()
        if not actualizar_producto:
            continue
        for i, valor in enumerate(actualizar_producto):
            print(f"{etiquetas[i]}: {str(valor).capitalize()}")
        respuesta_user = input("Este es el producto que queres actualizar? Responde con SI o NO ")
        if respuesta_user.upper() == "SI":
            nombre,descripcion,cantidad,precio,categoria = datos_producto_db()
            try:
                cursor.execute("UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? WHERE id = ?", (nombre, descripcion, cantidad, precio, categoria, actualizar_producto[0]))
                print("Producto actualizado correctamente!")
                conexion.commit()
            except sqlite3.IntegrityError as error:
                conexion.rollback()
                print(f"Error al actualizar el producto: {error}")
            except Exception as error:
                        conexion.rollback()
                        print(f"Ocurrio un error: {error}")
            finally:
                conexion.close()
            break
        else:
            print("Volvamos a intentar con otro ID...")

# Funcion 1ue permite ver si hay productos con stock bajo segun el criterio del usuario
def reporte_baja_cantidad():
    if not validar_productos_cargados():
        return False
    conexion, cursor = conectar()
    stock_busqueda = input("¿Querés ver los productos con stock menor o igual a qué cantidad? Ingresa un numero: ")
    if validar_int(stock_busqueda):
        stock_busqueda = int(stock_busqueda) 
        cursor.execute(F"SELECT * FROM productos WHERE cantidad <= {stock_busqueda}")
        productos = cursor.fetchall()
        conexion.close()
        return productos
    else:
        print("Debes ingresar una cantidad, no podes ingresar letras, signos ni dejar el espacio en blanco")
        conexion.close()
        return []
    
    
    
