# Proyecto Examen Final - Módulo 3

Proyecto base para la evaluación práctica del módulo 3. Los requisitos oficiales están en `Enunciado en la serie II de la evaluación final`.

## Inicio rápido

1. Abra la carpeta `ProyectoExamen`.
2. Ejecute las pruebas base.
3. Levante el backend.
4. Abra el frontend para revisar el estado inicial.

## Estructura

| Ruta | Contenido |
|---|---|
| `backend/` | Código del servidor y lógica base del asistente. |
| `frontend/` | Interfaz web estática para interactuar con el backend. |
| `data/` | Base de conocimiento inicial del proyecto. |
| `tests/base/` | Pruebas base que deben pasar desde el inicio. |
| `tests/validation/` | Pruebas de validación de la entrega final. |
| `docs/` | Espacio para documentación técnica y evidencias del estudiante. |

---

## 🚀 Entrega Final: Implementación Context-Aware Generation (CAG)

El proyecto ha sido completado utilizando **Metodología Scrum** mediante iteraciones (Sprints) estructuradas, logrando un 100% de cumplimiento en las pruebas de validación.

### Sprint 1: Persistencia en Memoria
- Se diseñó e implementó la clase `ContextStore` en `backend/context_store.py` usando un diccionario en memoria para almacenar las sesiones e historial del usuario.
- Se implementaron los métodos `save` y `list_for_user`.
- Se validó el correcto funcionamiento de los endpoints de contexto, superando los tests `test_saves_context_for_user` y `test_retrieves_context_for_user`.

### Sprint 2: Integración y Optimización del Asistente
- Se refactorizó `backend/server.py` para instanciar el almacenamiento de manera global.
- En `backend/assistant.py`, se implementó la inyección de contexto. Se diseñó una estrategia de límite de tokens obteniendo únicamente las últimas 3 preferencias del usuario.
- Se introdujo un bloque de **Early Return** para evitar consultas innecesarias a la memoria si el sistema de Recuperación de Información (RAG) no encontraba datos relevantes (`snippets`).
- Se verificó que el test integral `test_ask_uses_context_to_influence_later_response` pasara a estado "Green".

### Refactorización de Arquitectura y UX
- Se refactorizó la inyección de contexto separándola en un **System Prompt** (para guiar el comportamiento y restricciones del LLM mediante CAG) y un **User Prompt** (para el contenido base RAG).
- Se mejoró significativamente la Experiencia de Usuario (UX) en la respuesta autogenerada simulada, utilizando plantillas de lenguaje natural para construir frases fluidas en lugar de mostrar los corchetes o valores "crudos" en la interfaz.

### Actualización del Frontend
- En `frontend/index.html`, se eliminó el placeholder estático y se creó un contenedor dinámico para el Panel CAG (`Historial de Usuario`).
- En `frontend/app.js`, se actualizó `loadContext` para transformar el volcado de JSON raw en elementos de HTML dinámicos, que se renderizan automáticamente cada vez que carga la página o se hace una pregunta.

## Ejecutar pruebas

```bash
# Pruebas Base
./scripts/run_base_tests.sh

# Pruebas de Validación Final (CAG Integrado)
./test.sh
# Todas las validaciones (estado Green) han sido superadas.
```

## Ejecutar el Sistema

```bash
# Levantar el Backend (Puerto 8000)
PYTHONPATH=. python3 -m backend.server

# Levantar el Frontend estático (Puerto 8080)
python -m http.server 8080 --directory frontend
```
El backend queda disponible en `http://127.0.0.1:8000`.
El frontend web para el uso de la aplicación estará en `http://127.0.0.1:8080`.
