# Dashboard en Power Bi

Para el dashboard en Power Bi, se utiliza el archivo .CSV exportado desde la aplicación web con permisos de administrador. Este archivo CSV es importado en Power Bi para ser transformado y generar las tablas necesarias para mostrar el dashboard desarrollado.

## Transformaciones realizadas

Sobre el archivo inicial, se realizan diferentes transformaciones para limpiar datos, agruparlos, generar tramos horarios.

Finalmente, se generan las siguientes tablas:

### Datos:

-   log: Datos originales del CSV sin modificación, no se habilita la carga.
-   f_logs: Tabla de hechos

### Dimensiones:

-   d_Aux Usuario: Datos de usuarios
    -   uid
    -   Correo electrónico
-   d_Aux Tipo: Tipo de línea de log
    -   id_type
    -   Tipo
-   d_Aux Operación: Tipo de operación
    -   id_operation
    -   Operación
-   d_Aux Contenido: Desglose del contenido del log
    -   id_content
    -   Contenido
    -   id_typeOperation
    -   id_typeLog
    -   Correctos
-   d_Aux TipoLog: Tipo de log
    -   id_typeLog
    -   TipoLog
-   d_Aux TipoOperación
    -   id_typeOperation
    -   Tipo operación

### Órden:

-   d_Orden tramo horario: Tabla auxiliar para realizar ordenado personalizado en el tramo horario.
    -   Tramo horario
    -   Orden tramo horario

### Medidas:

-   Medidas: Registro de medidas calculadas.

Aparte, se genera también la tabla `Dim Calendar` mediante un script en DAX.

## Descripción del dashboard

El dashboard desarrollado dispone de tres pantallas de visualización de datos. Todas las pantallas disponen de elementos de segmentación comunes y sincronizados. Dichos elementos de segmentación son por fecha y por tipo de operación. También se han incluido botones de navegación entre pantallas y botón de limpiar segmentaciones.

### Dashboard principal

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/3af21708-8d40-4a24-baa6-fa1f03b97b55/Untitled.png)

Dispone de los siguientes datos:

-   Gráficas:
    -   Número de operaciones por tipo y tramo horario en formato Treemap.
    -   Tabla de operaciones realizadas por número de semana en formato Matriz.
-   Tarjetas con medidas calculadas:
    -   Total de operaciones realizadas.
    -   Operaciones realizadas en turno de mañana.
    -   Operaciones realizadas en turno de tarde.
    -   Operaciones realizadas en turno de noche.

En esta pantalla, en la tabla de operaciones, se ha añadido una `hover card` que muestra datos de los turnos y categorías en las que se han realizado las operaciones indicadas en cada celda.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/a5cae681-9150-44e7-9f7b-4d470cf255ef/Untitled.png)

### Informe por tipo de operación

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/2aef5bad-dfd9-49c0-9936-d7deb699d7c9/Untitled.png)

Dispone de los siguientes datos:

-   Gráficas:
    -   Número de operaciones por tramo horario y tipo de operación en formato Columnas apiladas.
    -   Número de operaciones por tipo de operación en formato Embudo.
    -   Porcentaje de operaciones por tipo de operación en formato Gráfico de anillos. (No se incluyen las operaciones de registro, login y logout).
-   Tarjetas con medidas calculadas:
    -   Número de operaciones de vehículos.
    -   Número de operaciones de proveedores.
    -   Número de operaciones de gastos.
    -   Porcentaje de error en operaciones realizadas sobre la base de datos.

### Informe por fecha

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/a9d60d0f-892b-4d71-a81b-1a1c5a5a9e1e/Untitled.png)

Dispone de los siguientes datos:

-   Gráficas:
    -   Número de operaciones por día de la semana en formato Columnas apiladas.
    -   Número de operaciones por fecha.
    -   Registro de nuevos usuarios por fecha.
    -   Recuento de operaciones por tipo y número de semana en el año.

### Relaciones entre las diferentes tablas

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/fd07ea12-51ba-4d00-bb69-5d6c7a1d3fcc/Untitled.png)

### Exportación a PDF

Se incluye exportación del dashboard completo en formato PDF.

[Proyecto PowerBi CarCare.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/61f51ecb-82e9-4fe4-9bad-70c506e29965/c0cb5448-ea65-4cb5-a7ca-1f0ce7a1d85e/Proyecto_PowerBi_CarCare.pdf)
