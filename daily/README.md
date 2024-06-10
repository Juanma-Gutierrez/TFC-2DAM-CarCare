# Diario del proyecto

### Semana 11/3 - 17/3

- Trabajo con Figma para la generación de los modelos de la aplicación.
- Selección de recursos para la aplicación.

### Semana 18/3 - 24/3

- Revisión de los modelos creados con Figma y modificación del modo responsive en el propio figma.
- Creación en pythonanywhere de la aplicación en Python para generar una API que devuelva datos de json hospedados localmente en el servidor.
- Inicio del proyecto en Android Studio y Kotlin.
- Creación del onBoarding.
- Añadida pantalla de login.
- Añadida autenticación mediante correo electrónico y contraseña.
- Añadida pantalla de registro de usuario.
- Añadida validación de campos en el registro de usuarios.

### Semana 25/3 - 31/3

- Creación de modal logout.
- Creación de Top Toolbar y Botton Navigation Bar.
- Creación del sistema de registro log.
- Creación de modelos de datos.
- Añadida grabación de datos locales de vehículos en Room.
- Añadida toolbar y bottombar con iconos, segunda toolbar en pantalla de vehículos, navegación con la bottombar.
- Creación de activity itemLIstActivity con los siguientes fragments:
    - Vehicles
    - Providers
    - Spents
- Creación de vehicleItem para el RecyclerView con el listado de vehículos.
- Creación del RecyclerView de vehículos.
- Puesta en marcha del switch selector de vehículos disponibles.
- Añadido diseño de pantalla de detalle.

### Semana 1/4 - 7/4

- Modificación de estructura de directorios del proyecto.
- Refactorización de código.
- Uso de corrutinas para la carga de datos.
- Añadida carga de datos desde Firebase.
- Carga de datos de vehículos en el RecyclerView.
- Añadida lógica de la creación de vehículos.
- Creación de layout de detalle de vehículos.
- Creación de spinners desplegables.

### Semana 8/4 - 14/4

- Llamada a la API para la recepción de marcas de vehículos.
- Modificación del orden de carga de los spinners selectables.
- Modificación de la navegación entre pantallas.
- Modificación del isLoading.

### Semana 15/4 - 21/4

- Añadidas pantallas vacías de detalle de proveedor y gastos.
- Creación de background lottie animado.
- Añadido background animado al proyecto.
- Refactorización de código y limpieza con SonarLint.
- Modificación del sistema de navegación.
- Añadida función Alert Dialog.
- Modificación de la grabación de vehículos en Firebase.
- Añadidos iconos.

### Semana 22/4 - 28/4

- Paso del id del vehículo seleccionado a la pantalla de detalle de vehículo.
- Creación de los fragments VehicleNew y VehicleEdit.
- Añadidos placeholders de vehículos.
- Añadido calendario de Material Design.
- Añadida funcionalidad editar vehículo.

### Semana 29/4 - 5/5

- Añadida la función para solicitar permisos.
- Añadida la funcionalidad de la cámara a pantalla de edición de vehículos.
- Añadida la funcionalidad de galería a pantalla de edición de vehículos.
- Añadida compresión de imágenes de los vehículos del usuario para optimizar espacio en Firebase storage y tiempos de carga.
- Modificación de la pantalla de edición para que haga edición y creación de vehículos.
- Añadido segundo layout para el vehicleItem para mostrar en el RecyclerView.
- Creación de AlertDialog con selección del tamaño de las tarjetas de vehículos.
- Grabación y carga de la selección del tamaño de las tarjetas en SharedPreferences.
- Arreglo del sistema de registro y login.
- Control de carga de imágenes y de placeholders si no hay imágenes de vehículos.

### Semana 6/5 - 12/5

- Añadidos layout list y grid para proveedores.
- Añadida carga de datos al recyclerView de proveedores.
- Añadido AlertDialog con la selección de tamaño de tarjetas de proveedores.
- Añadida carga de categorias en el selectable de proveedores.
- Añadida edición de proveedor y cancelar ventana de detalle.
- Añadido control de mensajes del userInterface mediante un objeto.
- Añadida creación de proveedor.
- Modificados layouts de item vehículo y gasto.

### Semana 13/5 - 19/5

- Arreglo de recyclerView de proveedores.
- Añadir carrusel de vehículos en fragment gastos.
- Añadida función de llamada al proveedor.
- Añadida confirmación de llamada.
- Añadido cálculo total de gastos y número de gastos.
- Arreglo de control del registro, chequeo de email válido.
- Añadido padding bottom a los recyclerView para dejar sitio a los fab.
- Añadida carga de proveedores en selectable.

### Semana 20/5 - 26/5

- Añadido el paso del dato vehicleId al detalle del gasto.
- Añadida carga del gasto en el formulario de detalle.
- Limpieza del proyecto y refactorización del código.
- Añadido calendario al fragment de gastos.
- Añadida creación de nuevo gasto.
- Añadida edición de gasto.
- Añadido borrado de gasto.
- Arreglada visibilidad de lottie isLoading.
- Personalización del color de los fab y de la bottomBar.
- Revisado mensajes del sistema.
- Añadida gráfica de gastos al listado de gastos.

### Semana 27/5 - 2/6

- Ajustes en la gráfica de gastos.
- Ajustes en la altura de la gráfica.
- Añadida pantalla about-me.
- Añadida exportación de gastos.
- Modificación del logotipo de la aplicación.
- Añadida Splash Screen con nuevo logotipo.
- Añadido logitipo al icono de la aplicación.

### Semana 3/6 - 9/6

- Aplicación Android:
    - Arreglado ordenación de los elementos en los selectables.
    - Añadidos mensajes de aviso si no hay creados vehículos o proveedores.
    - Añadido observable al número de proveedores creados.
    - Limpieza de código.
    - Modificados estilos y colores.
    - Añadidos comentarios.
    - Creación de documentación.
- Aplicación Angular:
    - Modificado isLoading.
    - Añadido log a creación, edición y borrado de vehículos.
    - Añadido log a creación, edición y borrado de proveedores.
    - Añadido log a creación, edición y borrado de gastos.
    - Añadido log a registro  de usuarios.
    - Añadido log a login y logout de usuarios.
    - Añadida exportación del log en formato CSV.
    - Modificado el calendario, formato y colores.

### Semana 10/6 - 16/6

- Test generales de las aplicaciones.
- Comprobaciones de exportaciones de datos para su importación en Power Bi.
- Revisión de documentación.
- Actualización de repositorios.
- Generación de archivo APK de la aplicación Android.