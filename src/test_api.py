import requests
import json

BASE_URL = "http://localhost:8000"

def test_create_user():
    print("=== Prueba POST - Crear Usuario ===")
    user_data = {
        "name": "Juan Perez",
        "email": "juan@example.com"
    }
    
    response = requests.post(f"{BASE_URL}/users/", json=user_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.json()

def test_get_all_users():
    print("\n=== Prueba GET - Obtener Todos los Usuarios ===")
    response = requests.get(f"{BASE_URL}/users/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_get_user_by_id(user_id):
    print(f"\n=== Prueba GET - Obtener Usuario por ID {user_id} ===")
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    try:
        # Crear usuario
        user = test_create_user()
        
        # Obtener todos los usuarios
        test_get_all_users()
        
        # Obtener usuario por ID
        if 'id' in user:
            test_get_user_by_id(user['id'])
            
    except requests.exceptions.ConnectionError:
        print("Error: No se puede conectar al servidor. Asegúrate de que la API esté ejecutándose en http://localhost:8000")