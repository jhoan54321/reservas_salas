# Sistema de Reservas Distribuido

## Descripción
Este proyecto implementa un sistema distribuido para la gestión de reservas de salas utilizando FastAPI. Permite crear salas, realizar reservas y consultar información, evitando conflictos como la doble reserva.

---

## Objetivo
Desarrollar una API que gestione un recurso compartido (salas) asegurando que no existan inconsistencias en el sistema.

---

## Tecnologías utilizadas
- Python
- FastAPI
- Uvicorn

---

## Arquitectura
El sistema sigue una arquitectura cliente-servidor:

- Cliente: Usuario que realiza solicitudes HTTP
- Servidor: API desarrollada en FastAPI
- Comunicación: Protocolo HTTP

---

## Endpoints

### Crear sala
POST /salas

Ejemplo:
```json
{
  "nombre": "Sala 1",
  "capacidad": 10
}
### Crear reserva

POST /reservas

Ejemplo:

{
  "sala_id": 1,
  "usuario": "Jhoan",
  "hora": "10:00"
}
Obtener reservas

GET /reservas

Resetear datos

GET /reset

Regla del sistema

Una sala no puede reservarse dos veces en la misma hora.

Flujo del sistema

El cliente envía una solicitud HTTP

La API procesa la información

Se valida la disponibilidad de la sala

Se almacena o retorna la información

Ejecución del proyecto
1. Instalar dependencias
pip install fastapi uvicorn requests
2. Ejecutar el servidor
uvicorn main:app --reload
3. Ejecutar pruebas
python test.py
4. Abrir documentación interactiva

http://127.0.0.1:8000/docs

Pruebas del sistema

Orden de ejecución:

GET /reset

POST /salas

POST /reservas

POST /reservas (duplicada)

GET /reservas

Resultados esperados

Crear sala → 200 OK

Crear reserva → 200 OK

Reserva duplicada → 400 Bad Request

Obtener reservas → 200 OK

Conceptos de Sistemas Distribuidos

Recurso compartido:
Las salas, ya que múltiples usuarios acceden a ellas.

Estado del sistema:
Las reservas almacenadas que indican disponibilidad.

Evidencia de funcionamiento

Se deben incluir capturas de:

Creación de sala

Creación de reserva

Validación de reserva duplicada

Consulta de reservas
