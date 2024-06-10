# API en Python

Para el proyecto, he desarrollado una API en Python que devolverá marcas y modelos de vehículos. En función de los diferentes endpoints recibirá diferentes respuestas.

La API de la aplicación está alojada en la web [pythonanywhere.com](http://pythonanywhere.com), así como los archivos Json que proporcionan las respuestas, cargando el archivo `flask_app.py` que es donde está la lógica de programación de la API.

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/73de4e8e-441d-43d4-b74d-2e45e2916461)

Captura de pantalla de la aplicación flask_app.py y de los json alojados en pythonanywhere.com

## Documentación de la API

[Build, Collaborate & Integrate APIs | SwaggerHub](https://app.swaggerhub.com/apis/Juanma-Gutierrez/CarCare.Android.Kotlin.API/1.0.0)

## Ejemplos de respuestas por categoría:

-   Coches: https://jumang.pythonanywhere.com/api/cars/brands

```
{
  "brands": [
    "Toyota",
    "Ford",
    "Honda",
    ...
  ]
}
```

-   Motocicletas: https://jumang.pythonanywhere.com/api/motorcycles/brands

```
{
  "brands": [
    "Honda",
    "Yamaha",
    "Kawasaki",
    ...
  ]
}
```

-   Furgonetas: https://jumang.pythonanywhere.com/api/vans/brands

```
{
  "brands": [
    "Mercedes-Benz",
    "Ford",
    "Volkswagen",
    ...
  ]
}
```

-   Camiones: https://jumang.pythonanywhere.com/api/trucks/brands

```
{
  "brands": [
    "Volvo",
    "Mercedes-Benz",
    "Scania",
    ...
  ]
}
```

## Ejemplo de respuesta por marca

-   Todos los modelos de coche de la marca Toyota https://jumang.pythonanywhere.com/api/cars/models/Toyota

```
{
  "models": [
    "Camry",
    "Corolla",
    "RAV4",
    ...
  ]
}
```

-   Todos los modelos de motocicleta de la marca Kawasaki https://jumang.pythonanywhere.com/api/motorcycles/models/Kawasaki

```
{
  "models": [
    "Ninja ZX-10R",
    "Ninja ZX-6R",
    "Ninja 400",
    ...
  ]
}
```

## Respuesta errónea

-   En caso de respuesta errónea, se devolverá la siguiente respuesta:
    https://jumang.pythonanywhere.com/api/motorcycles/models/ERROR

```
{
  "message": "Bad request: Invalid brand supply"
}
```

## Problemas encontrados:

Los problemas de CORS, se solucionan de esta manera:

-   Abrir una terminal `bash` en `pythonanywhere`.
-   Instalar `flask-cors`.
   
    ```bash
    pip install flask-cors
    ```
    
-   Con este paquete instalado, se pueden gestionar las CORS para que estén habilitadas para toda la API.

## Código completo de la aplicación Python
```python
from flask import Flask, request, jsonify
from flask_cors import CORS

import json
import os

# Error message
errorMessage = {'message': 'Bad request: Invalid brand supply'}

# Get the path
localPath = os.path.dirname(os.path.abspath(__file__))

# Build paths for each JSON file
path_cars_json = os.path.join(localPath, 'cars.json')
path_motorcycles_json = os.path.join(localPath, 'motorcycles.json')
path_vans_json = os.path.join(localPath, 'vans.json')
path_trucks_json = os.path.join(localPath, 'trucks.json')

# Load cars from JSON file
with open(path_cars_json) as f:
    cars = json.load(f)

# Load motorcycles from JSON file
with open(path_motorcycles_json) as f:
    motorcycles = json.load(f)

# Load vans from JSON file
with open(path_vans_json) as f:
    vans = json.load(f)

# Load trucks from JSON file
with open(path_trucks_json) as f:
    trucks = json.load(f)

app = Flask(__name__)
CORS(app)

# Endpoint to get all cars
@app.route('/api/cars', methods=['GET'])
def getCars():
    return jsonify(cars)

# Endpoint to get all cars brands
@app.route('/api/cars/brands', methods=['GET'])
def getCarsBrands():
    brands = list(cars["data"].keys())
    return jsonify({"brands": brands})

# Endpoint to get models of a specific brand
@app.route('/api/cars/models/<brand>', methods=['GET'])
def getCarsModels(brand):
    if brand in cars["data"]:
        models = cars["data"][brand]
        return jsonify({"models":models})
    else:
        return jsonify(errorMessage), 400

# Endpoint to get all motorcycles
@app.route('/api/motorcycles', methods=['GET'])
def getMotorcycles():
    return jsonify(motorcycles)

# Endpoint to get all motorcycles brands
@app.route('/api/motorcycles/brands', methods=['GET'])
def getMotorcyclesBrands():
    brands = list(motorcycles["data"].keys())
    return jsonify({"brands": brands})

# Endpoint to get models of a specific brand
@app.route('/api/motorcycles/models/<brand>', methods=['GET'])
def getMotorcyclesModels(brand):
    if brand in motorcycles["data"]:
        models = motorcycles["data"][brand]
        return jsonify({"models":models})
    else:
        return jsonify(errorMessage), 400

# Endpoint to get all vans
@app.route('/api/vans', methods=['GET'])
def getVans():
    return jsonify(vans)

# Endpoint to get all vans brands
@app.route('/api/vans/brands', methods=['GET'])
def get_vans_brands():
    brands = list(vans["data"].keys())
    return jsonify({"brands": brands})

# Endpoint to get models of a specific brand
@app.route('/api/vans/models/<brand>', methods=['GET'])
def getVansModels(brand):
    if brand in vans["data"]:
        models = vans["data"][brand]
        return jsonify({"models":models})
    else:
        return jsonify(errorMessage), 400

# Endpoint to get all trucks
@app.route('/api/trucks', methods=['GET'])
def getTrucks():
    return jsonify(trucks)

# Endpoint to get all trucks brands
@app.route('/api/trucks/brands', methods=['GET'])
def getTrucksBrands():
    brands = list(trucks["data"].keys())
    return jsonify({"brands": brands})

# Endpoint to get models of a specific brand
@app.route('/api/trucks/models/<brand>', methods=['GET'])
def getTrucksModels(brand):
    if brand in trucks["data"]:
        models = trucks["data"][brand]
        return jsonify({"models":models})
    else:
        return jsonify(errorMessage), 400

#Endpoint that returns all brands of all vehicle categories
@app.route('/api/brands', methods=['GET'])
def getAllBrands():
    all_brands = {
        "status": "success",
        "data": {
            "cars": list(cars["data"].keys()),
            "motorcycles": list(motorcycles["data"].keys()),
            "vans": list(vans["data"].keys()),
            "trucks": list(trucks["data"].keys())
        }
    }
    return jsonify(all_brands)

# Test endpoint
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/api')
def hello_world_api():
    return 'Hello world!'
```
