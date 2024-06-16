import baseDeDatos

def agregar_cliente():
    nombre = input("Ingrese el nombre: ") #guarda los datos ingresados por el usuario en variables correspondientes a la tabla 
    apellido = input("Ingrese el apellido: ")
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el número de teléfono: ")

    correo = correo or None #correo y telefono pueden ser valores nulos, entonces lo que hace esto es tomar el valor ingresado por el usuario y si no está ese valor
    #permite que sea nulo con el "none"
    telefono = telefono or None 

    query = "INSERT INTO clientes (Nombre, Apellido, correo, Teléfono) VALUES (%s, %s, %s, %s)" #se guarda lo de sql en query
    values = (nombre, apellido, correo, telefono) #los valores ingresados en la lista van a reemplazar el %s de arriba de sql
    
    baseDeDatos.cursor.execute(query, values) #ejecuta en la base de datos el query y los valores ingresados que fueron guardados en values
    baseDeDatos.conn.commit() #lo commitea para que quede
    print("Cliente registrado.")
    print(values)

def mostrar_clientes():
    query = "SELECT * FROM clientes" #de la misma manera, la consulta en sql se guarda en query y después se la ejecuta.
    baseDeDatos.cursor.execute(query)
    lista_clientes = baseDeDatos.cursor.fetchall() #a los resultados de la consulta los recopila con fetchall y los guarda en lista_clientes
    
    for cliente in lista_clientes: #por cada cliente en la lista_cliente, va imprimir el mismo. 
        print(cliente)


def modificar_cliente():
    id = input("Ingrese el id del cliente: ")

    print("Ingrese qué desea cambiar: ")
    print("Nombre - Apellido - Correo - Teléfono")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Nombre", "Apellido", "Correo", "Teléfono"]
    if columna not in columnas_permitidas: #verifica que lo que se ingresó sea alguna de esas columnas que existen en la tabla, sino se vuelve. 
        print("La columna ingresada no es válida.")
        return
           
    query = "UPDATE clientes SET {} = %s WHERE idClientes = %s".format(columna) #format(columna) va a reemplazar {} por el valor de la columna. Los %s se van a reemplazar por los values
    values = (cambio, id)
 
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit()

def eliminar_cliente():
    id = int(input("Ingrese el id del cliente: "))
   
    query = "DELETE FROM clientes WHERE idClientes = %s"
    values = (id,) # values tiene que ser una tupla, lista o dic, y acá como es un solo valor el que insertamos, le ponemos coma para que sea haga tupla

    baseDeDatos.cursor.execute(query,values)
    baseDeDatos.conn.commit()
    

