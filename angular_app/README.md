# Aplicación Angular

Disponible en este repositorio:

https://github.com/Juanma-Gutierrez/CarCare-Firebase

La versión de la aplicación Angular es la presentada como proyecto de Acceso a datos en el segundo trimestre, con ciertas mejoras para cumplir los requisitos solicitados para el proyecto final TFC.

La aplicación está actualmente desplegada en Netlify:

[Ionic App](https://carcare-firebase.netlify.app/home)

## Detalle de la aplicación

### Barra de `Menú principal`

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/be2783e1-02fc-488d-b750-9f37c3f7e8d1/Untitled.png)

-   Se muestra en toda la aplicación.
-   Incluye botón para traducir la aplicación entre español e inglés.
-   Si el usuario está logueado con el rol de Administrador, se mostrará la opción `Administración`.
-   Permite el cierre de sesión del usuario.

### Pantalla `Inicio`

![2024-06-08 21_13_31-Ionic App.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/51700597-6779-41a3-89f5-65fffdba10ca/2024-06-08_21_13_31-Ionic_App.png)

-   En la parte izquierda de la pantalla hay un listado con los vehículos registrados a nombre del usuario. Este listado se puede filtrar entre los vehículos disponibles o todos los registrados, incluyendo los no disponibles.
-   Las imágenes de los vehículos se encuentran cargadas en Firebase Storage. Si no existe imagen asociada al vehículo, se muestra una imagen placeholder de la categoría del vehículo.
-   Cuando se hace click en un vehículo, en la parte derecha se muestran su marca y modelo, así como el total gastado y el número de gastos. Debajo de la cabecera de los gastos se muestra el listado de gastos asociados.
-   En esta pantalla hay acceso al formulario de alta, edición y borrado de vehículos y de gastos.
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/3280ab0f-0a77-415d-bc87-3891eae25e0d/Untitled.png)
    ![2024-06-08 21_24_59-Ionic App.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/440d2a1f-0590-429e-9004-ad28987c017d/2024-06-08_21_24_59-Ionic_App.png)

### Pantalla `Vehículos`

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/150598c1-6fa3-4818-ab83-2313c70c0299/Untitled.png)

-   Se muestra un listado con todos los vehículos disponibles, así como información detallada de los mismos.
-   Las categorías se muestran tanto con un campo de texto como con un icono representativo.
-   Los vehículos no disponibles se mostrarán con un texto indicativo y un efecto en la tarjeta para mostrar dicho estado.
-   Existe un botón de compartir mediante el cual se puede enviar el listado de vehículos a cualquier aplicación admitida en el dispositivo.

### Pantalla `Proveedores`

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/133c14b3-2d6c-46ff-a81a-2b6f17b81f34/Untitled.png)

-   Muestra un listado de los proveedores, así como la categoría a la que pertenece y su teléfono de contacto.
-   En esta pantalla se puede dar de alta, editar y eliminar cualquier proveedor mediante el formulario dinámico correspondiente.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/7f3d2f58-2157-49d9-a8a6-8ca28a3cb682/Untitled.png)

### Pantalla `Sobre mí`

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/012d2c61-36cf-4c9a-8bf2-4599c8aa98c9/Untitled.png)

-   Pantalla con información del autor de la aplicación.
-   Incluye enlace a GitHub y a Linkedin del autor.

### Pantalla `Administración`

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/ebe89f0a-f3cc-4b04-8942-843353fecd5b/Untitled.png)

-   Pantalla de administración a la que se puede acceder únicamente si el usuario logueado tiene el rol de Administrador.
-   Hay un botón de exportación de datos, que exporta un archivo en formato `.CSV` con el registro de la aplicación.
-   Se incluyen tres gráficas, con las marcars de los vehículos más utilizados, número de vehículos por categoría y porcentaje de vehículos por categoría.
-   Se muestra una tabla con el listado de usuarios, así como los vehículos que tiene registrados cada uno de ellos.
-   En el caso del administrador, se muestra con un icono indicativo junto al nombre.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/b9903964-4ae6-4035-9d9b-e920d97d0157/Untitled.png)
