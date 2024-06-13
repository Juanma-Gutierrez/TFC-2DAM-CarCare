# API en Python

Para el proyecto, he desarrollado una API en Python que devolverá marcas y modelos de vehículos. En función de los diferentes endpoints recibirá diferentes respuestas.

La API de la aplicación está alojada en la web [pythonanywhere.com](http://pythonanywhere.com), así como los archivos Json que proporcionan las respuestas, cargando el archivo `flask_app.py` que es donde está la lógica de programación de la API.

![image](https://github.com/Juanma-Gutierrez/TFC-2DAM-CarCare/assets/101201349/73de4e8e-441d-43d4-b74d-2e45e2916461)

Captura de pantalla de la aplicación flask_app.py y de los json alojados en pythonanywhere.com

## Documentación de la API

[Build, Collaborate & Integrate APIs | SwaggerHub](https://app.swaggerhub.com/apis-docs/Juanma-Gutierrez/CarCare.Android.Kotlin.API/1.0.0#/)

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
## Documentación de la aplicación python

La documentación de la aplicación python se encuentra en este repositorio, en documentation/html.

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
"""
@package my_flask_app
Documentation for the Flask application.

This module provides a Flask web application with several endpoints
to retrieve data about cars, motorcycles, vans, and trucks from JSON files.
"""
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

@app.route('/api/cars', methods=['GET'])
def getCars():
    """
    Endpoint to get all cars.

    @return: JSON response with all cars data.
    """
    return jsonify(cars)

@app.route('/api/cars/brands', methods=['GET'])
def getCarsBrands():
    """
    Endpoint to get all car brands.

    @return: JSON response with a list of car brands.
    """
    brands = list(cars["data"].keys())
    return jsonify({"brands": brands})


@app.route('/api/cars/models/<brand>', methods=['GET'])
def getCarsModels(brand):
    """
    Endpoint to get models of a specific car brand.

    @param brand: The brand of the car.
    @return: JSON response with a list of models for the specified brand,
    or an error message if the brand is not found.
    """
    if brand in cars["data"]:
        models = cars["data"][brand]
        return jsonify({"models":models})
    else:
        return jsonify(errorMessage), 400


@app.route('/api/motorcycles', methods=['GET'])
def getMotorcycles():
    """
    Endpoint to get all motorcycles.

    @return: JSON response with all motorcycles data.
    """
    return jsonify(motorcycles)

@app.route('/api/motorcycles/brands', methods=['GET'])
def getMotorcyclesBrands():
    """
    Endpoint to get all motorcycle brands.

    @return: JSON response with a list of motorcycle brands.
    """
    brands = list(motorcycles["data"].keys())
    return jsonify({"brands": brands})

@app.route('/api/motorcycles/models/<brand>', methods=['GET'])
def getMotorcyclesModels(brand):
    """
    Endpoint to get models of a specific motorcycle brand.

    @param brand: The brand of the motorcycle.
    @return: JSON response with a list of models for the specified brand,
    or an error message if the brand is not found.
    """
    if brand in motorcycles["data"]:
        models = motorcycles["data"][brand]
        return jsonify({"models":models})
    else:
        return jsonify(errorMessage), 400


@app.route('/api/vans', methods=['GET'])
def getVans():
    """
    Endpoint to get all vans.

    @return: JSON response with all vans data.
    """
    return jsonify(vans)

@app.route('/api/vans/brands', methods=['GET'])
def get_vans_brands():
    """
    Endpoint to get all van brands.

    @return: JSON response with a list of van brands.
    """
    brands = list(vans["data"].keys())
    return jsonify({"brands": brands})

@app.route('/api/vans/models/<brand>', methods=['GET'])
def getVansModels(brand):
    """
    Endpoint to get models of a specific van brand.

    @param brand: The brand of the van.
    @return: JSON response with a list of models for the specified brand,
    or an error message if the brand is not found.
    """
    if brand in vans["data"]:
        models = vans["data"][brand]
        return jsonify({"models":models})
    else:
        return jsonify(errorMessage), 400


@app.route('/api/trucks', methods=['GET'])
def getTrucks():
    """
    Endpoint to get all trucks.

    @return: JSON response with all trucks data.
    """
    return jsonify(trucks)

@app.route('/api/trucks/brands', methods=['GET'])
def getTrucksBrands():
    """
    Endpoint to get all truck brands.

    @return: JSON response with a list of truck brands.
    """
    brands = list(trucks["data"].keys())
    return jsonify({"brands": brands})


@app.route('/api/trucks/models/<brand>', methods=['GET'])
def getTrucksModels(brand):
    """
    Endpoint to get models of a specific truck brand.

    @param brand: The brand of the truck.
    @return: JSON response with a list of models for the specified brand,
    or an error message if the brand is not found.
    """
    if brand in trucks["data"]:
        models = trucks["data"][brand]
        return jsonify({"models":models})
    else:
        return jsonify(errorMessage), 400


@app.route('/api/brands', methods=['GET'])
def getAllBrands():
    """
    Endpoint to get all brands of all vehicle categories.

    @return: JSON response with a dictionary containing lists of brands for
    cars, motorcycles, vans, and trucks.
    """
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


@app.route('/')
def hello_world():
    """
    Test endpoint.

    @return: Simple 'Hello world!' message.
    """
    return 'Hello world!'

@app.route('/api')
def hello_world_api():
    """
    API test endpoint.

    @return: Simple 'Hello world!' message for the API.
    """
    return 'Hello world!'
```
