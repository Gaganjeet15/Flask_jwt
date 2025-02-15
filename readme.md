# Flask JWT Authentication Example

A simple Flask app showing how to handle user registration, login, and JWT authentication. Uses in-memory storage instead of a database to keep things simple.

## Features

- User registration with username/password
- Login endpoint that returns JWT tokens
- Protected route that needs authentication
- Password hashing for security
- Simple error handling

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Gaganjeet15/Flask_jwt
   cd app.py
   ```

2. Set up your virtual environment:
   ```bash
   python -m venv venv
   
   # Windows users:
   venv\Scripts\activate
   
   # Mac/Linux users:
   source venv/bin/activate
   ```

3. Install what you need:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```
   Server starts at `http://127.0.0.1:5000`

## API Endpoints

### Register a New User
```bash
POST /register

# Request body:
{
    "username": "testuser",
    "password": "yourpassword123"
}

# Success response:
{
    "message": "User created successfully"
}
```

### Login
```bash
POST /login

# Request body:
{
    "username": "testuser",
    "password": "yourpassword123"
}

# Success response:
{
    "access_token": "eyJhbGciOiJIUzI1NiI..."
}
```

### Access Protected Route
```bash
GET /home
Header: Authorization: Bearer your-jwt-token

# Success response:
{
    "message": "Welcome testuser!",
    "user": "testuser"
}
```

## Testing

You can test the API using Postman or curl:

1. Register a user first:
   ```bash
   curl -X POST http://127.0.0.1:5000/register \
   -H "Content-Type: application/json" \
   -d '{"username": "testuser", "password": "yourpassword123"}'
   ```

2. Login to get a token:
   ```bash
   curl -X POST http://127.0.0.1:5000/login \
   -H "Content-Type: application/json" \
   -d '{"username": "testuser", "password": "yourpassword123"}'
   ```

3. Use the token to access protected routes:
   ```bash
   curl http://127.0.0.1:5000/home \
   -H "Authorization: Bearer your-token-here"
   ```

## Important Notes

- This is a demo app - it stores users in memory, so they'll disappear when you restart

