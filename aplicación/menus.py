import clientes, ventas, empleados, productos, detalle_ventas, satisfacción_cliente, supervisor, direcciones, consultas

def menu_principal():
    print("1. Menú clientes. ")
    print("2. Menú empleados.")
    print("3. Menú productos.")
    print("4. Menú ventas.")
    print("5. Menú detalle de ventas.")
    print("6. Menú satisfacción de cliente.")
    print("7. Menú supervisor")
    print("8. Menú direcciones")
    print("9. Menú consultas.")
    print("10. Calcular satisfacción de cliente.")
    print("11. Salir.")


def menu_clientes():
    while True:
        print("\nMenú Clientes:")
        print("1. Agregar clientes.") #CREATE crear
        print("2. Mostrar clientes.") #READ leer o mostrar
        print("3. Modificar clientes.") #UPDATE actualizar o modificar
        print("4. Eliminar clientes.") #DELETE eliminar
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            clientes.agregar_cliente()
        elif opcion == "2":
            clientes.mostrar_clientes()
        elif opcion == "3":
            clientes.modificar_cliente()
        elif opcion == "4":
            clientes.eliminar_cliente()    
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_supervisor():
    while True:
        print("\nMenú supervisor:")
        print("1. Agregar supervisor.") 
        print("2. Mostrar supervisor.") 
        print("3. Modificar supervisor.") 
        print("4. Eliminar supervisor.") 
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            supervisor.agregar_supervisor()
        elif opcion == "2":
            supervisor.mostrar_supervisor()
        elif opcion == "3":
            supervisor.modificar_supervisor()
        elif opcion == "4":
            supervisor.eliminar_supervisor()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_productos():
    while True:
        print("\nMenú productos:")
        print("1. Agregar producto.") 
        print("2. Mostrar productos.") 
        print("3. Modificar producto.") 
        print("4. Eliminar producto.") 
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            productos.agregar_producto()
        elif opcion == "2":
            productos.mostrar_productos()
        elif opcion == "3":
            productos.modificar_producto()
        elif opcion == "4":
            productos.eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_empleados():
    while True:
        print("\nMenú empleados:")
        print("1. Agregar empleado.") 
        print("2. Mostrar empleados.") 
        print("3. Modificar empleado.") 
        print("4. Eliminar empleado.") 
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            empleados.agregar_empleado()
        elif opcion == "2":
            empleados.mostrar_empleados()
        elif opcion == "3":
            empleados.modificar_empleado()
        elif opcion == "4":
            empleados.eliminar_empleado()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_direcciones():
    while True:
        print("\nMenú direcciones:")
        print("1. Agregar dirección.") 
        print("2. Mostrar direcciones.") 
        print("3. Modificar dirección.") 
        print("4. Eliminar dirección.") 
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            direcciones.agregar_direccion()
        elif opcion == "2":
            direcciones.mostrar_direcciones()
        elif opcion == "3":
            direcciones.modificar_direccion()
        elif opcion == "4":
            direcciones.eliminar_direccion()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")



def menu_ventas():
    while True:
        print("\nMenú ventas:")
        print("1. Agregar venta.") 
        print("2. Mostrar ventas.") 
        print("3. Modificar venta.") 
        print("4. Eliminar venta.") 
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ventas.agregar_venta()
        elif opcion == "2":
            ventas.mostrar_ventas()
        elif opcion == "3":
            ventas.modificar_venta()
        elif opcion == "4":
            ventas.eliminar_venta()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_detalle_ventas():
    while True:
        print("\nMenú detalle_ventas:")
        print("1. Agregar detalle_venta.") 
        print("2. Mostrar detalle_ventas.") 
        print("3. Modificar detalle_venta.") 
        print("4. Eliminar detalle_venta.") 
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            detalle_ventas.agregar_detalle_ventas()
        elif opcion == "2":
            detalle_ventas.mostrar_detalle_ventas()
        elif opcion == "3":
            detalle_ventas.modificar_detalle_venta()
        elif opcion == "4":
            detalle_ventas.eliminar_detalle_venta()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_satisfacción_cliente():
    while True:
        print("\nMenú satisfacción_cliente:")
        print("1. Agregar satisfacción_cliente.") 
        print("2. Mostrar satisfacción_clientes.") 
        print("3. Modificar satisfacción_cliente.") 
        print("4. Eliminar satisfacción_cliente.") 
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            satisfacción_cliente.agregar_satisfacción_cliente()
        elif opcion == "2":
            satisfacción_cliente.mostrar_satisfacción_clientes()
        elif opcion == "3":
            satisfacción_cliente.modificar_satisfacción_cliente()
        elif opcion == "4":
            satisfacción_cliente.eliminar_satisfacción_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_consultas():
    while True:
        print("\nMenú consultas:")
        print("1. Consulta: Mostrar los productos que tengan un precio mayor a un valor ingresado.") #una tabla
        print("2. Consulta: Mostrar ventas las ventas realizadas entre dos fechas.") #between
        print("3. Consulta: Mostrar clientes que tengan teléfonos registrados.") #usa los nulos
        print("4. Consulta: Mostrar empleados por célula.") #inner join
        print("5. Consulta: Mostrar clientes que residan en Córdoba.") #inner join con filtro
        print("6. Consulta: Mostrar datos de empleados y supervisores por célula.") #inner join
        print("7. Consulta: Mostrar ventas pagadas con tarjeta de crédito ") #inner join - like
        print("8. Consulta: Mostrar los clientes por la cantidad de ventas que realizaron.") #group by
        print("9. Consulta: Mostrar los últimos cuatro productos cargados a la base de datos.") #limit
        print("10. Consulta: Mostrar los empleados activos.") #usa el dato lógico o booleano 
        print("11. Volver.")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            consultas.consulta_uno()
        elif opcion == "2":
            consultas.consulta_dos()
        elif opcion == "3":
            consultas.consulta_tres()
        elif opcion == "4":
            consultas.consulta_cuatro()
        elif opcion == "5":
            consultas.consulta_cinco()
        elif opcion == "6":
            consultas.consulta_seis()
        elif opcion == "7":
            consultas.consulta_siete()
        elif opcion == "8":
            consultas.consulta_ocho()
        elif opcion == "9":
            consultas.consulta_nueve()
        elif opcion == "10":
            consultas.consulta_diez()
        elif opcion == "11":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

