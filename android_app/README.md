# Aplicación Kotlin

Disponible en este repositorio:

https://github.com/Juanma-Gutierrez/CarCare-Kotlin

Aplicación realizada desde cero durante el tercer trimestre como entrega final del TFC.

## Detalle de la aplicación

### Pantallas `OnBoarding`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/453f9243-2a7b-4257-9c0c-9a59de3f2b71)

La aplicación cuenta con varias pantallas `OnBoarding`, que se muestran la primera vez que se accede a la aplicación. Estas pantallas muestran información sobre:

-   Qué hace la aplicación.
-   Cómo gestionar los vehículos.
-   Cómo gestionar los proveedores.
-   Cómo gestionar los gastos.

Estas pantallas OnBoarding se generan dinámicamente desde la aplicación.

### Pantallas `Login` y `Registro`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/13697e5a-0359-4cba-96b3-7d91020fc752)

### Login

-   Solicita correo electrónico y contraseña para realizar el login.
-   Si se produce algún error, se muestra un snackbar de aviso.

### Registro

-   Pide los datos del usuario.
-   Controla si el correo electrónico ya está previamente en uso.
-   Controla que la contraseña cumpla los requisitos de seguridad y que tanto la contraseña como la confirmación de contraseña coincidan.
-   Una vez realizado el registro, automáticamente redirige al usuario a la pantalla inicial de la aplicación con el login hecho.

### Pantalla `Vehículos`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/25e94f26-3aa8-4375-a73d-ad22dcf8f3fe)

### Pantalla listado de vehículos

-   En esta pantalla se muestra un listado con los vehículos del usuario.
-   Si no existe ningún vehículo creado, muestra un aviso.
-   Se pueden filtrar por vehículos disponibles o todos los vehículos. Si el vehículo no está disponible, se muestra con filtro rojo y mensaje indicativo.
-   Se muestra un icono con la categoría correspondiente del vehículo.

### Pantalla detalle de vehículo

-   Se pueden añadir nuevos vehículos, mostrando un formulario en blanco.
-   Se pueden modificar vehículos del usuario, cargando todos los datos del vehículo.
-   La carga de la categoría, marca y modelo se realizan de forma dinámica mediante consultas a la API desarrollada en Python para el proyecto.

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/934e8b83-6ea9-4eb1-9e6c-ad3c37b17528)

-   Al pulsar sobre el botón con la `fecha de registro`, se despliega el calendario interactivo.
-   Si se le ha hecho click a un vehículo, mostrará la opción de eliminar. Esta opción permanece oculta en la creación de vehículo.
-   Al pulsar en el botón de `cámara`, mostrará un diálogo solicitando al usuario de dónde se va a capturar la imagen, de la cámara o de la galería.
-   Si no se han concedido previamente los permisos de acceso a cámara o galería, mostrará la solicitud de permisos correspondiente.
-   La imagen capturada pasa por un proceso de compresión y redimensionado para minimizar el espacio en Firebase Storage.

### Pantalla `Proveedores`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/561fa5e3-c7b2-426f-bee0-4de961c92b4b)

### Pantalla listado de proveedores

-   Muestra un listado con los proveedores.
-   Si no existe ningún proveedor creado, muestra un aviso.
-   Se muestra el nombre, la categoría, un icono de la categoría correspondiente y el teléfono si lo tuviera.
-   Si el proveedor tiene teléfono, al hacer click sobre el icono del teléfono realiza una llamada.

### Pantalla detalle de proveedor

-   Permite crear un nuevo proveedor.
-   Si se hace click sobre un proveedor, entra en la pantlla de edición.

### Pantalla `Gastos`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/20b7defa-7a0e-4c55-9eb1-7650ca5a03e0)

### Pantalla listado de gastos

-   Se muestra un carousel de Material Design en la parte superior de la pantalla.
-   Los vehículos disponibles se muestran con un filtro azul y los no disponibles con un filtro rojo.
-   Si no existe ningún proveedor creado, muestra un aviso.
-   Mientras no se haga click en ningún vehículo, el `fab` de añadir gasto estará oculto, ya que no se puede asignar un gasto si no se ha indicado a qué vehículo asignarlo.
-   Al hacer click en alguno de los vehículos, se muestra la siguiente información organizada en tres bloques separados:
    -   Bloque totales:
        -   Se muestran la marca y el modelo del vehículo.
        -   Gastos totales de este vehículo.
        -   Número de gastos del vehículo.
        -   Botón de exportación de datos, con la fecha de exportación, vehículo, listado de gastos ordenado por fecha, con la fecha, proveedor e importe, número de gastos y gastos totales.
        -   Ejemplo de exportación de datos.
          
            <img src="https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/a1362b46-f53c-4b00-bd73-b0563026ce03" width="300"/>
    -   Bloque gráfica:
        -   Se muestra una gráfica animada con los proveedores que más importe han acumulado en este vehículo.
        -   Si hay solamente un proveedor o menos, no se muestra este bloque.
        -   El tamaño de la gráfica es adaptativa, hasta un máximo de 5 proveedores.
    -   Bloque listado de gastos:
        -   Se muestra un recyclerView con un listado de los gastos asociados al vehículo seleccionado.
        -   Al hacer click sobre alguno de estos gastos se accede a la pantalla de edición del gasto.
        -   
### Pantalla detalle de gasto

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/b865cdab-6511-4106-b510-62b1f8c51789)

-   Permite la creación de un nuevo gasto.
-   También permite la edición y eliminación de un gasto ya creado.
-   El selectable se carga con los datos de proveedores del usuario.
-   Para mejorar la accesibilidad, al hacer click en el importe, se selecciona todo el campo.
-   Al hacer click sobre la fecha del gasto, se despliega el calendario dinámico.

### Menú de `Opciones`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/bd9e09b1-4b4b-453f-a071-94a2ef1a6fa6)

El menú de opciones incluye la siguiente información:

-   Correo electrónico del usuario logueado.
-   Opción de configuración.
    -   La pantalla de configuración permite modificar diferentes opciones de la aplicación:
        -   Listado de vehículos: En formato lista compacta o vista ampliada.
        -   Listado de proveedores: En formato vista rejilla o vista lista.
            ![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/2a296649-e615-4a89-abcf-867859f3a3a7)
        -   Tamaño de la gráfica de proveedores: hasta un máximo de 5 proveedores o sin gráfica si así se desea.
            <img src="https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/182f1c6c-010f-4e8e-86e3-39a1052dae26" width="500"/>

-   Pantalla Sobre mí. Muestra datos del autor de la aplicación, así como enlaces a GitHub y Linkedin del autor.
-   Opción Cerrar sesión: Permite cerrar la sesión del usuario activo.

### Mensajes de aviso

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/dc39263d-ade2-4a79-8ee7-b943c36b3417)

La aplicación tiene múltiples mensajes de aviso para informar al usuario de errores o consejos de uso. Estos son algunos ejemplos:

-   Si no existe ningún vehículo, informa al usuario.
-   Si no existe ningún proveedor, informa al usuario.
-   Si entra en la pantalla de gastos, informa si no hay ningún vehículo. Si hay al menos un vehículo pero no hay ningún proveedor, informa y no muestra el botón de añadir gasto.
-   Para las operaciones de creación, edición y eliminación muestra un dialogo para confirmar la operación.
-   Para el cierre de sesión muestra un diálogo de confirmación.

## Persistencia de datos

### Room

En almacenamiento local se guardan los datos de los vehículos, mediante el uso de `Room`. También existe persistencia de datos con Firebase, de manera que la aplicación puede ser utilizada parcialmente aunque no se disponga de conexión con la base de datos.

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/731a0c12-c6d6-496f-a333-a7ac5e279bae)

### SharedPreferences

También existe persistencia de datos mediante el uso de SharedPreferences, para almacenar la configuración personalizada de la aplicación por parte del usuario.
