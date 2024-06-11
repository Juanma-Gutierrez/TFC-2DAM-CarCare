# Aplicación Angular

Disponible en este repositorio:

https://github.com/Juanma-Gutierrez/CarCare-Firebase

La versión de la aplicación Angular es la presentada como proyecto de Acceso a datos en el segundo trimestre, con ciertas mejoras para cumplir los requisitos solicitados para el proyecto final TFC.

La aplicación está actualmente desplegada en Netlify:

[Ionic App](https://carcare-firebase.netlify.app/home)

## Detalle de la aplicación

### Pantalla de `Login`

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/0e162ad5-05a7-4ea6-b1c9-89e431574bf5/Untitled.png)

-   La aplicación cuenta con una pantalla de login para iniciar la sesión.
-   El login se realiza con correo electrónico y contraseña.
-   El correo electrónico queda almacenado en localstorage del navegador.
-   Si se introducen mal los datos, se muestra un aviso de error.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/77b2ab26-6945-4dac-a4f8-4577b607923a/Untitled.png)

### Pantalla de `Registro`

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/220e0062-2385-4e30-949a-76bdbab6d7a3/Untitled.png)

-   La aplicación cuenta con una pantalla para registrar usuarios.
-   Se controla que se introduzcan correctamente todos los datos.
-   Hay control especial sobre la contraseña, solicita que tenga al menos una mayúscula, una minúscula, un número y 8 dígitos.
-   Durante el proceso de inserción de la contraseña se va indicando si se cumplen los requisitos. Si cumple correctamente se muestra en pantalla.
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/90f23358-5d58-43db-b56b-80fb860c3290/Untitled.png)

### Barra de `Menú principal`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/24c4f4ee-fe54-4e65-b92d-d84bef90e9b1)

-   Se muestra en toda la aplicación.
-   Incluye botón para traducir la aplicación entre español e inglés.
-   Si el usuario está logueado con el rol de Administrador, se mostrará la opción `Administración`.
-   Permite el cierre de sesión del usuario.

### Pantalla `Inicio`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/571dad78-27e6-485e-8dd1-5e4114c7d349)

-   En la parte izquierda de la pantalla hay un listado con los vehículos registrados a nombre del usuario. Este listado se puede filtrar entre los vehículos disponibles o todos los registrados, incluyendo los no disponibles.
-   Las imágenes de los vehículos se encuentran cargadas en Firebase Storage. Si no existe imagen asociada al vehículo, se muestra una imagen placeholder de la categoría del vehículo.
-   Cuando se hace click en un vehículo, en la parte derecha se muestran su marca y modelo, así como el total gastado y el número de gastos. Debajo de la cabecera de los gastos se muestra el listado de gastos asociados.
-   En esta pantalla hay acceso al formulario de alta, edición y borrado de vehículos y de gastos.
    ![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/cd223b78-06fc-438f-8aef-7d3292840747)
    ![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/3e232a1f-e581-4463-8c6b-d1df26bd6114)

### Pantalla `Vehículos`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/3f552e74-a7f2-4e45-aca9-8ad0009c3c7f)

-   Se muestra un listado con todos los vehículos disponibles, así como información detallada de los mismos.
-   Las categorías se muestran tanto con un campo de texto como con un icono representativo.
-   Los vehículos no disponibles se mostrarán con un texto indicativo y un efecto en la tarjeta para mostrar dicho estado.
-   Existe un botón de compartir mediante el cual se puede enviar el listado de vehículos a cualquier aplicación admitida en el dispositivo.

### Pantalla `Proveedores`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/4b30f543-9774-4629-9f62-354c19517c37)

-   Muestra un listado de los proveedores, así como la categoría a la que pertenece y su teléfono de contacto.
-   En esta pantalla se puede dar de alta, editar y eliminar cualquier proveedor mediante el formulario dinámico correspondiente.

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/0897b762-f93a-4b48-b0db-30bf7e94c03b)

### Pantalla `Sobre mí`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/9332c34f-d498-4992-81f8-e311f0e4372b)

-   Pantalla con información del autor de la aplicación.
-   Incluye enlace a GitHub y a Linkedin del autor.

### Pantalla `Administración`

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/9ad14a85-f07b-42a3-a430-66a447701de3)

-   Pantalla de administración a la que se puede acceder únicamente si el usuario logueado tiene el rol de Administrador.
-   Hay un botón de exportación de datos, que exporta un archivo en formato `.CSV` con el registro de la aplicación.
-   El formato de exportación sería el siguiente:
    ![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/65afcd31-041e-44f0-bdb8-00c65f3bf8f6)
-   Se incluyen tres gráficas, con las marcars de los vehículos más utilizados, número de vehículos por categoría y porcentaje de vehículos por categoría.
-   Se muestra una tabla con el listado de usuarios, así como los vehículos que tiene registrados cada uno de ellos.
-   En el caso del administrador, se muestra con un icono indicativo junto al nombre.
    ![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/4339aba8-0833-4cfc-bbf4-bc3c2e9af8ec)
