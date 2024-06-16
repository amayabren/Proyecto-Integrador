INSERT INTO clientes (Nombre, Apellido, Correo, Teléfono)
VALUES ("Olivia", "Gonzalez", "olivia@ejemplo.com", NULL), 
("Agustina", "Molina", "agusmolina@ejemplo.com", 22211),
("Juan", "Perez", "juan@ejemplo.com", NULL),
("Victoria","Martinez", "victoria@ejemplo.com", 101010),
("Santiago", "Cepeda", "santiago@ejemplo.com", 555000),
("Pedro", "Garcia", "pedro@ejemplo.com", NULL);

INSERT INTO supervisor (Nombre, Apellido, Célula)
VALUES ("Verónica", "Aguirre", 1),
("David", "Arias", 2),
("Maria", "Escalante", 3),
("Fernando", "Perez", 4);

INSERT INTO métodopago (Tipo)
VALUES ("Tarjeta de Crédito"),
("Tarjeta de Débito"),
("Transferencia"),
("Efectivo");

INSERT INTO empleado (Nombre, Apellido, Fecha_ingreso, Supervisor_Célula, Activo)
VALUES ("Eduardo", "Lopez", "2024-01-01", 2, 1), 
("Lucia", "Acuña", "2020-01-02", 3, 1),
("Rocio", "Pacheco", "2019-05-08", 1, 1),
("Diego", "Zapata", "2022-09-01", 1, 1), 
("Jorge", "Suarez", "2024-06-05", 3, 0),
("Andrea", "Romero", "2019-05-08", 2, 0);

INSERT INTO productos (Nombre, Descripción, Precio)
VALUES ("Moto E22 64 GB", NULL, 175999),
("Moto G23 128 GB", NULL, 247999),
("Samsung Galaxy A04 64 GB", "Pantalla Infinity-V de 6,5 pulgadas.", 202499),
("Samsung Galaxy A34 5G 128 GB", NULL, 449999),
("Moto G41 128 GB", "Pantalla Full HD+ de 6,5 pulgadas.", 279999),
("Samsung Galaxy A15 128GB", NULL, 399999),
("Samsung Galaxy A54 5G 256GB", "Características de última generación.", 999999),
("Moto G13 128GB", NULL, 269999);



INSERT INTO ventas (Fecha, Total, Empleado_idEmpleado, Clientes_idClientes, MétodoPago_idMétodoPago)
VALUES ('2024-01-02', 175999, 1, 2, 2), #compró 1 producto id 1
       ('2024-01-04', 495998, 2, 4, 1), #compró 2 productos id 2
	   ('2024-02-01', 399999, 1, 5, 3), #compró 1 producto id 6
       ('2024-02-10', 607497, 3, 1, 3), #compró 3 productos id 3
       ('2024-02-08', 449999, 4, 3, 4), #compró 1 producto id 4 
       ('2024-01-10', 1199997, 2, 2, 1); #compró 3 productos id 6


INSERT INTO detalle_ventas (Ventas_idVentas, Productos_idProductos, Precio, Cantidad, Descuento)
VALUES (1, 1, 175999, 1, NULL),
(2, 2, 247999, 2, NULL),
(3, 6, 399999, 1, NULL),
(4, 3, 202499, 3, NULL),
(5, 4, 449999, 1, NULL),
(6, 6, 39999, 3, NULL);


INSERT INTO satisfacción_cliente (Puntos, Clientes_idClientes, Empleado_idEmpleado, Ventas_idVentas)
VALUES (5, 2, 1, 1),
(1, 4, 2, 2),
(2, 5, 1, 3),
(5, 1, 3, 4),
(5, 3, 4, 5),
(1, 2, 2, 6);

INSERT INTO direcciones (Localidad, Código_Postal, Calle, Clientes_idClientes)
VALUES ("Córdoba", 5030, "Belgrano 1012", 1),
("Córdoba", 5000, "Lima 800", 2),
("Bell Ville", 2550, "General Paz 745", 3),
("Córdoba", 5002, "Sam Martin 300", 4),
("Córdoba", 5002, "Caseros 4510", 5),
("Villa María", 5900, "9 de julio 1550", 6);
 







