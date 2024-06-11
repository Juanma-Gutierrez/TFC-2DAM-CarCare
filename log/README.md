# Gestión de datos del Log

El log generado con las operaciones realizadas en nuestra aplicación, tanto web como Android, siguen este modelo de datos:

```mermaid
classDiagram
    class LogType {
        <<enumeration>>
        INFO
        ERROR
    }

    class OperationLog {
        <<enumeration>>
        CREATE_USER
        LOGIN
        LOGOUT
        VEHICLE
        PROVIDER
        SPENT
    }

    class ItemLog {
        String dateTime
        LogType type
        OperationLog operationLog
        String currentUser
        String uid
        String content
        +toString(): String
    }

    ItemLog --> LogType
    ItemLog --> OperationLog
```

De este modo, tendremos para cada operación realizada sobre las colecciones Vehicle, Provider, Spent y además las operaciones de Login, Logout y Create_User.

La salida tendría esta estructura:

```
[
    {
        content: "Edition of vehicle successfully"
        currentUser: "juanma@gmail.com"
        dateTime: "2024-06-01T20:34:17.410Z"
        operationLog: "VEHICLE"
        type: "INFO"
        uid: "KrmRWiE1pMMDsBoSFWJvZ8y4ouN2"
    },
    {
        content: "Login successfully"
        currentUser: "juanma@gmail.com"
        dateTime: "2024-06-02T14:00:07.509Z"
        operationLog: "LOGIN"
        type: "INFO"
        uid: "KrmRWiE1pMMDsBoSFWJvZ8y4ouN2"
    }, ...
]
```

Estos datos pueden ser extraídos a formato CSV para ser procesados posteriormente mediante Power BI para generar el dashboard de gestión de la aplicación para los usuarios con rol de administrador.

Formato del archivo .CSV:

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/bee739b6-6e7a-4089-80ed-1460c3bdba40)
