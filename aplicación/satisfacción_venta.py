import baseDeDatos

def menu_satisfacción_venta():
    while True:
        print("\nMenú de satisfacción del cliente de empleados:")
        print("1. Calcular satisfacción de cliente por empleado.") 
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            satisfacción_venta()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def satisfacción_venta():
    id = input("Ingrese el id del empleado que desea evaluar: ")
    query = "SELECT Puntos FROM satisfacción_cliente WHERE Empleado_idEmpleado = %s;"
    values = (id,)
    baseDeDatos.cursor.execute(query, values)
    satisfaccion_cliente = baseDeDatos.cursor.fetchall() #va a extraer el resultado de la consulta sql en una lista
    
    if satisfaccion_cliente: #if para imprimir un mensaje en el caso de que satisfacción_cliente no traiga ningún dato
        suma_total = 0 #establece la variable para usarla en el for
        #como satisfacción_cliente es una lista compuesta por tuplas, hay que extraer cada tupla para poder sumarlas
        for item in satisfaccion_cliente: #por cada item en satisfacción_cliente
            suma_total += item[0]  # va a ir sumando el item que ocupe la posición 0, y así con cada posición hasta que termine la lista
        
        prom = suma_total / len(satisfaccion_cliente) #calcula el promedio. len nos da la longitud de la lista, o sea cuantas tuplas tiene.   
        
        if prom > 4:
            print("La satisfacción de cliente es BUENA.")
        elif prom > 3:
            print("La satisfacción de cliente es REGULAR.")
        else:
            print("La satisfacción de cliente es MALA.")
    else:
        print("No se encontraron datos de satisfacción para el empleado.")