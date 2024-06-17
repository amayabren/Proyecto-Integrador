# Proyecto
LINK VIDEO: https://drive.google.com/file/d/1fiaasi7xSWpqPOolw76oagVsyi7eQs0P/view?usp=sharing
## Integrantes del Grupo

- **Nombre:** Brenda Tamara 
  - **Apellido:** Amaya
  - **DNI:** 41846601
  - **Correo Electrónico:** brendaamaya9@gmail.com 
  - **GitHub:** [AmayaBrendaTamara](https://github.com/amayabren)

- **Nombre:** María Florencia
  - **Apellido:** Gimenez
  - **DNI:** 33029489
  - **Correo Electrónico:** floxi87@gmail.com
  - **GitHub:** [MaríaFlorenciaGimenez](https://github.com/Floxi87)

- **Nombre:** José Augusto
  - **Apellido:** Lazarte
  - **DNI:** 28763838
  - **Correo Electrónico:** augusto.lazarte81@gmail.com
  - **GitHub:** [JoséAugustoLazarte](https://github.com/AugustoLaz)

- **Nombre:** Florencia
  - **Apellido:** Lelli
  - **DNI:** 40574799
  - **Correo Electrónico:** florlelli6@gmail.com
  - **GitHub:** [FlorenciaLelli](https://github.com/florlelli)

- **Nombre:** María Cecilia
  - **Apellido:** Linares
  - **DNI:** 33171021
  - **Correo Electrónico:** mcecilialinares@gmail.com
  - **GitHub:** [MaríaCeciliaLinares](https://github.com/cecilinares)

## Descripción del proyecto
Nuestro proyecto consiste en desarrollar un sistema que gestione el proceso de venta y la satisfacción del cliente. Las principales funcionalidades incluyen:

- Registro de clientes.
- Registro de productos.
- Gestión de ventas.
- Evaluación de la satisfacción del cliente.
- Gestión de empleados.
- Gestión de detalle de venta.
- Gestión de supervisores.
- Gestión de direcciones del cliente.
- Gestión de método de pago.

## Detalle de la Aplicación Modularizada
La aplicación se ha estructurado de manera modular para facilitar su mantenimiento y escalabilidad. A continuación, se detalla la estructura de archivos y su contenido:

1. **index.py**:
    - **Descripción**: Este es el archivo principal de la aplicación. Contiene el menú principal desde el cual se puede acceder a la gestión de clientes, empleados, productos, ventas y la generación de informes.
    - **Funciones**: Implementa el menú principal y llama a los submenús correspondientes.

2. **cliente.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD (Crear, Leer, Actualizar, Eliminar) para la entidad de Cliente.
    - **Funciones**: `agregar_cliente`, `mostrar_clientes`, `modificar_cliente`, `eliminar_cliente`, `menu_clientes`.
    - **Uso**: Gestiona la información de los clientes del comercio.

3. **empleado.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de Empleado.
    - **Funciones**: `agregar_empleado`, `mostrar_empleados`, `modificar_empleado`, `eliminar_empleado`, `menu_empleados`.
    - **Uso**: Gestiona la información de los empleados del comercio.

4. **producto.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de Producto.
    - **Funciones**: `agregar_producto`, `mostrar_productos`, `modificar_producto`, `eliminar_producto`, `menu_productos`.
    - **Uso**: Gestiona la información de los productos disponibles en el comercio.

5. **venta.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de Venta.
    - **Funciones**: `registrar_venta`, `mostrar_ventas`, `modificar_venta`, `eliminar_venta`, `menu_ventas`.
    - **Uso**: Gestiona la información de las ventas realizadas en el comercio.

6. **detalle_ventas.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de detalle_ventas.
    - **Funciones**: `registrar_detalle_ventas`, `mostrar_detalle_ventas`, `modificar_detalle_venta`, `eliminar_detalle_venta`, `menu_detalle_ventas`.
    - **Uso**: Gestiona la información del detalle de las ventas realizadas en el comercio.
    - 
7. **satisfacción_cliente.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de satisfacción_cliente.
    - **Funciones**: `registrar_satisfacción_cliente`, `mostrar_satisfacción_cliente`, `modificar_satisfacción_cliente`, `eliminar_satisfacción_cliente`, `menu_satisfacción_cliente`.
    - **Uso**: Gestiona el puntaje que recibe el empleado de un cliente al realizarse una venta.
    - 
8. **direcciones.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de direcciones.
    - **Funciones**: `registrar_direcciones`, `mostrar_direcciones`, `modificar_direcciones, `eliminar_direcciones`, `menu_direcciones`.
    - **Uso**: Gestiona la información del domicilio de los clientes.

9. **supervisor.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de Supervisor.
    - **Funciones**: `registrar_supervisor`, `mostrar_supervisores`, `modificar_supervisor`, `eliminar_supervisor`, `menu_supervisor`.
    - **Uso**: Gestiona la información de los supervisores del comercio.
      
10. **consultas.py**:
    - **Descripción**: Este archivo contiene las consultas que ejecutan SQL dentro de Python.
    - **Funciones**: Contiene siete consultas.
    - **Uso**: Muestra informes específicos.

## Uso de la Aplicación
Para ejecutar la aplicación, usa el siguiente comando en la terminal (para la tranquilidad del usuario se facilitaran los driver correspondientes que te indicaran el paso a paso para concretar la isntalación):

**python index.py** 

Sigue las instrucciones en pantalla para navegar por el menú principal y gestionar las diferentes entidades. Esto te permitirá gestionar el stock de tu emprendimiento, tener seguimiento de las ventas realizadas vía detalle de las mismas y su vez poder monitorizar el rendimiento de los empleados mediante la satisfacción obtenida de los cliente en el proceso de venta. Con la aplicación podras tener un sustento númerico para gestionar volumenes de venta y resultados operativos. 

## Base de Datos
Diseñamos una base de datos MySQL siguiendo el modelo entidad-relación (DER) y convertimos este modelo en un modelo relacional. La base de datos contiene tablas para cada entidad con relaciones bien definidas. También hemos incluido scripts SQL para crear la estructura de la base de datos, insertar datos iniciales y realizar consultas.
Información para el usuario: Los driver incluyen la instalación de la estructura de tablas para la base de datos (estimamos contemplar esto en el diseño de un interfaz grafico amigable con el usuario, con el nombre Setup BD), donde solo se debera definir nombre de las tablas para admnistrar el negocio y posteriormente ingresar en las mismas los datos de stockeo de productos, detalle de ventas para su control/seguimiento y datos del personal en general para recabar el rendimiento y resultado de los mismos en el proceso de gestión de venta. 

## Navegación del Repositorio
El repositorio está organizado de la siguiente manera:

1. **Carpeta aplicacion**: Contiene todos los archivos fuente .py.

   - **index.py**: Archivo principal de la aplicación.
   - **cliente.py**: Funciones CRUD para la entidad Cliente.
   - **empleado.py**: Funciones CRUD para la entidad Empleado.
   - **producto.py**: Funciones CRUD para la entidad Producto.
   - **venta.py**: Funciones CRUD para la entidad Venta.
   - **detalle_venta.py**: Funciones CRUD para la entidad detalle_ventas.

2. **Carpeta bd**: Contiene los scripts SQL para la base de datos y los diagramas de entidad-relación.

   - **ventas_satisfacción.sql**: Script para crear la estructura de la base de datos.
   - **datos.ql**: Script para insertar datos iniciales en la base de datos.
   - **consultas sql.sql**: Scrip de las consultas para la base de datos.
   - **Diagrama Crowfoot png**
   - **Diagrama Entidad Relación**

3. **Archivo README.md**: Contiene la descripción del proyecto, instrucciones de uso y detalles de instalación.



