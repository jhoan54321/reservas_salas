import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def print_response(nombre, response):
    try:
        print(nombre, response.status_code, response.json())
    except:
        print(nombre, response.status_code, response.text)

# Resetear datos
def reset():
    url = f"{BASE_URL}/reset"
    response = requests.get(url)
    print_response("Reset:", response)

# Crear sala
def crear_sala():
    url = f"{BASE_URL}/salas"
    data = {
        "nombre": "Sala 1",
        "capacidad": 10
    }
    response = requests.post(url, json=data)
    print_response("Crear sala:", response)

# Crear reserva válida
def crear_reserva():
    url = f"{BASE_URL}/reservas"
    data = {
        "sala_id": 1,
        "usuario": "Jhoan",
        "hora": "10:00"
    }
    response = requests.post(url, json=data)
    print_response("Crear reserva:", response)

# Intentar reserva duplicada
def reserva_duplicada():
    url = f"{BASE_URL}/reservas"
    data = {
        "sala_id": 1,
        "usuario": "Pedro",
        "hora": "10:00"
    }
    response = requests.post(url, json=data)
    print_response("Reserva duplicada:", response)

# Consultar reservas
def obtener_reservas():
    url = f"{BASE_URL}/reservas"
    response = requests.get(url)
    print_response("Reservas:", response)

if __name__ == "__main__":
    reset()
    time.sleep(0.5)

    crear_sala()
    time.sleep(0.5)

    crear_reserva()
    time.sleep(0.5)

    reserva_duplicada()
    time.sleep(0.5)

    obtener_reservas()