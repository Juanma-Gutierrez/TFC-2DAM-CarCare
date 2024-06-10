# Aplicación Kotlin

Disponible en este repositorio:

https://github.com/Juanma-Gutierrez/CarCare-Kotlin

Aplicación realizada desde cero durante el tercer trimestre como entrega final del TFC.

## Detalle de la aplicación

### Pantallas `OnBoarding`

![01.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/1fca11d2-3d49-4b61-8597-ab9576d4cf26/01.jpg)

La aplicación cuenta con varias pantallas `OnBoarding`, que se muestran la primera vez que se accede a la aplicación. Estas pantallas muestran información sobre:

-   Qué hace la aplicación.
-   Cómo gestionar los vehículos.
-   Cómo gestionar los proveedores.
-   Cómo gestionar los gastos.

Estas pantallas OnBoarding se generan dinámicamente desde la aplicación.

### Pantallas `Login` y `Registro`

![02.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/5d642de9-f97d-4b01-b157-e31141f27b37/02.jpg)

### Login

-   Solicita correo electrónico y contraseña para realizar el login.
-   Si se produce algún error, se muestra un snackbar de aviso.

### Registro

-   Pide los datos del usuario.
-   Controla si el correo electrónico ya está previamente en uso.
-   Controla que la contraseña cumpla los requisitos de seguridad y que tanto la contraseña como la confirmación de contraseña coincidan.
-   Una vez realizado el registro, automáticamente redirige al usuario a la pantalla inicial de la aplicación con el login hecho.

### Pantalla `Vehículos`

![Google Pixel 4 XL Presentation (2).jpg](<https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/3e35eb35-825e-475b-8636-586ddbdc2dfe/Google_Pixel_4_XL_Presentation_(2).jpg>)

### Pantalla listado de vehículos

-   En esta pantalla se muestra un listado con los vehículos del usuario.
-   Si no existe ningún vehículo creado, muestra un aviso.
-   Se pueden filtrar por vehículos disponibles o todos los vehículos. Si el vehículo no está disponible, se muestra con filtro rojo y mensaje indicativo.
-   Se muestra un icono con la categoría correspondiente del vehículo.

### Pantalla detalle de vehículo

-   Se pueden añadir nuevos vehículos, mostrando un formulario en blanco.
-   Se pueden modificar vehículos del usuario, cargando todos los datos del vehículo.
-   La carga de la categoría, marca y modelo se realizan de forma dinámica mediante consultas a la API desarrollada en Python para el proyecto.

![Google Pixel 4 XL Presentation.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/b6b4c0fa-d04f-4fa2-a727-96e28a059fc2/Google_Pixel_4_XL_Presentation.jpg)

-   Al pulsar sobre el botón con la `fecha de registro`, se despliega el calendario interactivo.
-   Si se le ha hecho click a un vehículo, mostrará la opción de eliminar. Esta opción permanece oculta en la creación de vehículo.
-   Al pulsar en el botón de `cámara`, mostrará un diálogo solicitando al usuario de dónde se va a capturar la imagen, de la cámara o de la galería.
-   Si no se han concedido previamente los permisos de acceso a cámara o galería, mostrará la solicitud de permisos correspondiente.
-   La imagen capturada pasa por un proceso de compresión y redimensionado para minimizar el espacio en Firebase Storage.

### Pantalla `Proveedores`

![proveed.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/594ad285-93ac-4100-b1b1-20119d7f52a8/proveed.png)

### Pantalla listado de proveedores

-   Muestra un listado con los proveedores.
-   Si no existe ningún proveedor creado, muestra un aviso.
-   Se muestra el nombre, la categoría, un icono de la categoría correspondiente y el teléfono si lo tuviera.
-   Si el proveedor tiene teléfono, al hacer click sobre el icono del teléfono realiza una llamada.

### Pantalla detalle de proveedor

-   Permite crear un nuevo proveedor.
-   Si se hace click sobre un proveedor, entra en la pantlla de edición.

### Pantalla `Gastos`

![gastos1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/207a2e5b-3614-4018-a107-b7c27331004c/gastos1.png)

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
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/a8b3bf54-e627-4135-a701-8d9dbabdf709/Untitled.png)
    -   Bloque gráfica:
        -   Se muestra una gráfica animada con los proveedores que más importe han acumulado en este vehículo.
        -   Si hay solamente un proveedor o menos, no se muestra este bloque.
        -   El tamaño de la gráfica es adaptativa, hasta un máximo de 5 proveedores.
    -   Bloque listado de gastos:
        -   Se muestra un recyclerView con un listado de los gastos asociados al vehículo seleccionado.
        -   Al hacer click sobre alguno de estos gastos se accede a la pantalla de edición del gasto.

![gastos2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/aea20d74-aded-4394-8462-aee3eedc76d5/gastos2.png)

### Pantalla detalle de gasto

-   Permite la creación de un nuevo gasto.
-   También permite la edición y eliminación de un gasto ya creado.
-   El selectable se carga con los datos de proveedores del usuario.
-   Para mejorar la accesibilidad, al hacer click en el importe, se selecciona todo el campo.
-   Al hacer click sobre la fecha del gasto, se despliega el calendario dinámico.

### Menú de `Opciones`

![opciones.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/97f9f7fb-5d92-441b-ab57-4b57c8d901bb/opciones.png)

El menú de opciones incluye la siguiente información:

-   Correo electrónico del usuario logueado.
-   Opción de configuración.
    -   La pantalla de configuración permite modificar diferentes opciones de la aplicación:
        -   Listado de vehículos: En formato lista compacta o vista ampliada.
        -   Listado de proveedores: En formato vista rejilla o vista lista.
            ![ejemplos.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/2ae2f12c-c461-4faf-8863-6d0ffd44132c/ejemplos.png)
        -   Tamaño de la gráfica de proveedores: hasta un máximo de 5 proveedores o sin gráfica si así se desea.
            ![opciones2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/771aff53-67bb-439a-9f74-41f5c1d63c1f/opciones2.png)
-   Pantalla Sobre mí. Muestra datos del autor de la aplicación, así como enlaces a GitHub y Linkedin del autor.
-   Opción Cerrar sesión: Permite cerrar la sesión del usuario activo.

### Mensajes de aviso

![mensajes.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/dd78451b-d348-4735-ac6c-47ce20902c62/mensajes.png)

La aplicación tiene múltiples mensajes de aviso para informar al usuario de errores o consejos de uso. Estos son algunos ejemplos:

-   Si no existe ningún vehículo, informa al usuario.
-   Si no existe ningún proveedor, informa al usuario.
-   Si entra en la pantalla de gastos, informa si no hay ningún vehículo. Si hay al menos un vehículo pero no hay ningún proveedor, informa y no muestra el botón de añadir gasto.
-   Para las operaciones de creación, edición y eliminación muestra un dialogo para confirmar la operación.
-   Para el cierre de sesión muestra un diálogo de confirmación.

## Persistencia de datos

### Room

En almacenamiento local se guardan los datos de los vehículos, mediante el uso de `Room`. También existe persistencia de datos con Firebase, de manera que la aplicación puede ser utilizada parcialmente aunque no se disponga de conexión con la base de datos.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/4b7ef5c1-d304-44a1-9be5-fa14a45fa37d/Untitled.png)

### SharedPreferences

También existe persistencia de datos mediante el uso de SharedPreferences, para almacenar la configuración personalizada de la aplicación por parte del usuario.
