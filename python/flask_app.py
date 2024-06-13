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