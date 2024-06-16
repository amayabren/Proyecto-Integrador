import baseDeDatos

def consulta_uno():
    precio = int(input("Mostrar los productos que tengan un precio mayor a: "))
    query = "SELECT * FROM productos WHERE precio > %s;"
    values = (precio,)
    baseDeDatos.cursor.execute(query, values)
    productos = baseDeDatos.cursor.fetchall()  
    for productos in productos:
        print(productos)

def consulta_dos(): #las ventas registradas van desde el mes de enero y febrero de este año
    fecha_uno = input("En formato año-mes-día, ingresa la primera fecha: ")
    fecha_dos = input("Ingresa la segunda fecha: ")
    query = "SELECT * FROM ventas WHERE Fecha BETWEEN  %s AND %s;"
    values = fecha_uno, fecha_dos
    baseDeDatos.cursor.execute(query, values)
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)        

def consulta_tres():
    query = "SELECT * FROM clientes WHERE Teléfono IS NOT NULL;"
    baseDeDatos.cursor.execute(query)
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)        

def consulta_cuatro():
    célula = input("Ingrese la célula que desa filtrar: ")
    query = "SELECT * FROM empleado WHERE Supervisor_Célula = %s;"
    values = (célula,)
    baseDeDatos.cursor.execute(query, values)
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)

def consulta_cinco():
    query = "SELECT clientes.idClientes, clientes.Nombre, direcciones.Localidad FROM direcciones INNER JOIN clientes ON direcciones.Clientes_idClientes = clientes.idClientes WHERE direcciones.Localidad  = 'Córdoba';"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)    

def consulta_seis():
    query = "SELECT empleado.idEmpleado, empleado.Nombre, empleado.Apellido, supervisor.Célula, supervisor.Nombre, supervisor.Apellido FROM supervisor INNER JOIN empleado ON supervisor.Célula = empleado.Supervisor_Célula  ORDER BY supervisor.Célula;"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas) 

def consulta_siete():
    query = "SELECT ventas.idVentas, ventas.Clientes_IdClientes, métodopago.Tipo FROM métodopago INNER JOIN ventas ON métodopago.idMétodoPago = ventas.MétodoPago_idMétodoPago WHERE métodopago.Tipo LIKE '%Tarjeta de Crédito%';" 
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas) 

def consulta_ocho():
    query = "SELECT c.idClientes, c.Nombre, c.Apellido, COUNT(v.idVentas) AS total_ventas FROM clientes c INNER JOIN ventas v ON c.idClientes = v.Clientes_idClientes GROUP BY c.idClientes, c.Nombre, c.Apellido ORDER BY total_ventas DESC;"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)

def consulta_nueve():
    query = "SELECT * FROM productos ORDER BY idProductos DESC LIMIT 4;"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)

def consulta_diez():
    query = "SELECT idEmpleado, Nombre, Apellido, Supervisor_Célula FROM empleado WHERE Activo = 1;"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)    