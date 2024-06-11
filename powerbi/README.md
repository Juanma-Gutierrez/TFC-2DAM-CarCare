# Dashboard en Power BI

Para el dashboard en Power BI, se utiliza el archivo .CSV exportado desde la aplicación web con permisos de administrador. Este archivo CSV es importado en Power BI para ser transformado y generar las tablas necesarias para mostrar el dashboard desarrollado.

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

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/8d9cb7ec-d647-48e7-a301-140bd4c22934)

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

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/9997782b-6b97-494d-8e32-ec748b3d3cf8)

### Informe por tipo de operación

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/85f52fab-29ba-446f-ba1b-b55b57733f36)

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

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/8161ee58-3f93-4381-98c1-c302a04be6a4)

Dispone de los siguientes datos:

-   Gráficas:
    -   Número de operaciones por día de la semana en formato Columnas apiladas.
    -   Número de operaciones por fecha.
    -   Registro de nuevos usuarios por fecha.
    -   Recuento de operaciones por tipo y número de semana en el año.

### Relaciones entre las diferentes tablas

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/47835620-5dc5-4425-b25f-340f30b8d44e)

### Exportación a PDF

Se incluye exportación del dashboard completo en formato PDF.

[Proyecto PowerBi CarCare.pdf](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/blob/develop/PDF/Proyecto_PowerBi_CarCare.pdf)
