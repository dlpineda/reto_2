# RETO 2. Aplicando Clean Hexagonal 

- Diplomado en Modernización de la Arquitectura de Software y Cloud Computing 
- Profesor: Jorge Valente Fragoso Mora
- Alumno:   David Leonardo Pineda Perez
- Fecha:    2025-sep-18

## Descripción

- API RESTful con Arquitectura Hexagonal. 

## Capas de la estructura de Arquitectura Hexagonal 

```
src/
├── domain/                     # Capa de Dominio
│   ├── entities.py                 - Entidades de negocio
│   └── ports.py                    - Puertos (interfaces)
├── application/                # Capa de Aplicación
│   └── services.py                 - Servicios de aplicación
├── adapters/                   # Capa de Adaptadores
│   ├── inbound/                    - Adaptadores de entrada
│   │   └── user_controller.py
│   └── outbound/                   - Adaptadores de salida
│       └── user_repository.py
├── main.py                     # Punto de entrada FastAPI
├── requirements.txt            * Dependencias
└── test_api.py                 * Script de pruebas
```

## Instalación y Ejecución

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar la API:
```bash
python src/main.py
```

3. Acceder a la documentación:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Pruebas

Ejecutar el script de pruebas:
```bash
python test_api.py
```

## Endpoints

- `POST /users/` - Crear usuario
- `GET /users/` - Obtener todos los usuarios
- `GET /users/{id}` - Obtener usuario por ID