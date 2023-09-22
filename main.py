from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from methods import get_data

app = Flask(__name__)

# Configure Flask-JWT-Extended
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to your secret key
jwt = JWTManager(app)

@app.route('/peoples', methods=['GET'])
@jwt_required  # Protect this route with JWT authentication
def get_peoples():
    peoples = get_data('people')
    return jsonify(peoples)


@app.route('/planets', methods=['GET'])
@jwt_required  # Protect this route with JWT authentication
def get_planets():
    planets = get_data('planets')
    return jsonify(planets)

@app.route('/starships', methods=['GET'])
@jwt_required  # Protect this route with JWT authentication
def get_starships():
    starships = get_data('starships')
    return jsonify(starships)

@app.route('/films', methods=['GET'])
@jwt_required  # Protect this route with JWT authentication
def get_films():
    films = get_data('films')
    return jsonify(films)

items = []
@app.route('/items', methods=['POST'])
@jwt_required  # Protect this route with JWT authentication
def add_item():
    data = request.get_json()
    if 'name' in data:
        new_item = {'name': data['name']}
        items.append(new_item)
        return jsonify({'message': 'Item added successfully'}), 201
    else:
        return jsonify({'error': 'Name is required'}), 400


# Route for obtaining a JWT token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    # In a real application, you would perform actual authentication here
    # For simplicity, let's assume the username and password are hardcoded
    if username == 'user' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
