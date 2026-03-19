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

