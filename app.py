from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)


# Set the access token expiry to 5 minutes
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)

jwt = JWTManager(app)

# Mock database to store users (just for testing purposes)
users_db = {}  # username: hashed_password

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    # Get username and password from the request
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"msg": "Hey, you need to provide both username and password!"}), 400

    # Check if the username already exists
    if username in users_db:
        return jsonify({"msg": "Oops, that username is already taken!"}), 400

    # Hash the password and store it in the mock DB
    users_db[username] = generate_password_hash(password)  # Storing hashed password for security
    return jsonify({"msg": "User registered successfully!"}), 201

# Route to log in a user
@app.route('/login', methods=['POST'])
def login():
    # Get username and password from the request
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required!"}), 400

    # Check if the user exists and the password is correct
    if username not in users_db or not check_password_hash(users_db[username], password):
        return jsonify({"msg": "Invalid username or password"}), 401

    # Generate an access token for the user (expires in 5 minutes)
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Protected route - only accessible with a valid JWT token
@app.route('/home', methods=['GET'])
@jwt_required()
def home():
    current_user = get_jwt_identity()  # Get the identity of the current user from the token
    return jsonify(logged_in_as=current_user, message="Welcome to your dashboard!")

# Run the app
# if __name__ == '__main__':
#     app.run(debug=True)  # Debug mode is on for development purposes
    
if __name__ == '__main__':
    print("Script is running!")
    app.run(debug=True, port=5000)