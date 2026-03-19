from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

salas = []
reservas = []

# Modelos (esto evita errores de datos)
class Sala(BaseModel):
    nombre: str
    capacidad: int

class Reserva(BaseModel):
    sala_id: int
    usuario: str
    hora: str

# Resetear datos
@app.get("/reset")
def reset():
    salas.clear()
    reservas.clear()
    return {"mensaje": "Datos reiniciados"}

# Crear sala
@app.post("/salas")
def crear_sala(sala: Sala):
    nueva_sala = {
        "id": len(salas) + 1,
        "nombre": sala.nombre,
        "capacidad": sala.capacidad
    }

    salas.append(nueva_sala)

    return {"mensaje": "Sala creada", "sala": nueva_sala}

# Crear reserva
@app.post("/reservas")
def crear_reserva(reserva: Reserva):

    # Verificar que la sala exista
    if not any(s["id"] == reserva.sala_id for s in salas):
        raise HTTPException(status_code=404, detail="Sala no existe")

    # Verificar duplicado
    for r in reservas:
        if r["sala_id"] == reserva.sala_id and r["hora"] == reserva.hora:
            raise HTTPException(status_code=400, detail="Sala ya reservada en esa hora")

    nueva_reserva = {
        "id": len(reservas) + 1,
        "sala_id": reserva.sala_id,
        "usuario": reserva.usuario,
        "hora": reserva.hora
    }

    reservas.append(nueva_reserva)

    return {"mensaje": "Reserva creada", "reserva": nueva_reserva}

# Obtener reservas
@app.get("/reservas")
def obtener_reservas():
    return reservas