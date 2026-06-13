# Registro de Prompts - Implementación de CAG
**Proyecto:** `proyecto_final_IA_PERSONALIZADO`

Este archivo documenta los prompts exactos utilizados para guiar a la IA durante el desarrollo, implementación y refactorización del módulo Context-Augmented Generation (CAG), utilizando metodología Scrum y TDD.

---

## Fase Inicial: Diagnóstico del Sistema

### Prompt 1: Verificación de funcionalidad del proyecto
> En base al archivo readme.md quiero que ejecutes el proyecto, lo dejes levantado y realices todas las pruebas necesarias para asegurar que este funcionando el 100% del proyecto proyecto_final_IA_PERSONALIZADO

---

## Sprint 1: Persistencia en Memoria

### Prompt 2: Propuesta de diseño
> Bien, el entorno está verificado y funcionando correctamente. Vamos a iniciar con la fase de persistencia del módulo CAG utilizaremos métodologia scrum y lo dividiremos en 2 sprints haciendo commits.
> Como primer paso, requiero que diseñes la clase ContextStore en el archivo backend/context_store.py. Esta clase debe gestionar el historial de sesiones en memoria, incluyendo métodos para agregar contextos (add_context) y para recuperar el historial completo de un usuario específico (list_for_user).
> Muéstrame primero el código de este diseño para revisarlo antes de proceder con la implementación y el versionado.

### Prompt 3: Implementación del componente ContextStore
> Diseño aprobado. Procede con la implementación de la clase ContextStore en backend/context_store.py con el diseño acordado. Ejecuta las pruebas de validación (tests/validation) para asegurar que el sistema se mantiene estable.
> Una vez confirmada la estabilidad, genera el mensaje de commit siguiendo estrictamente el estándar Conventional Commits (ej. feat(backend): ...).
> No ejecutes el commit automáticamente proporcióname primero el mensaje para que yo lo revise y ejecute manualmente.

---

## Sprint 2: Integración y Optimización del Asistente

### Prompt 4: Estrategia de rendimiento y límite de tokens
> Ya he realizado el commit del ContextStore. Ahora, procederemos a la integración en backend/assistant.py y backend/server.py.
> Antes de realizar cambios, necesito que analices la función answer_question en assistant.py y los endpoints en server.py. Mi preocupación es el rendimiento: inyectar un contexto histórico largo en cada consulta podría aumentar la latencia o exceder los tokens permitidos si no se gestiona bien.
> Proponme una estrategia para:
> Filtrar o limitar el contexto recuperado desde store.list_for_user(user_id) antes de inyectarlo en el prompt del asistente (por ejemplo, tomar solo los últimos N registros). Determinar en qué parte del flujo de assistant.py es más eficiente realizar esta inyección.
> Muéstrame tu propuesta lógica antes de proceder con la modificación del código.

### Prompt 5: Autorización e implementación de la estrategia
> Adelante, autorizo la implementación bajo esta estrategia. Te doy el visto bueno para proceder:
> Aplica la lógica de filtrado y el flujo Early Return en backend/assistant.py.
> Ejecuta la suite completa de pruebas incluyendo el test de integración (test_ask_uses_context_to_influence_later_response) para asegurar que ahora pase a estado "Green".
> Una vez confirmado, genera el mensaje de commit siguiendo el estándar Conventional Commits (tipo feat o refactor con scope backend/assistant).

---

## Fase Final: Refactorización y Experiencia de Usuario (UX)

### Prompt 6: Problemas encontrados en UI (Refactorización)
> He revisado el comportamiento en el frontend y la experiencia de usuario (UX) es deficiente. La inyección del contexto en assistant.py se sigue viendo como un volcado de variables crudas (ej. [Contexto aplicado: ...]). Como arquitecto de esta solución, no apruebo esta salida visual.
> Requiero que modifiques la forma en que se construye generated_answer. Elimina la concatenación literal de arreglos con corchetes o paréntesis. En su lugar, implementa una lógica que construya una respuesta fluida en lenguaje natural. Por ejemplo, la estructura debe ser similar a: 'Tomando en cuenta que [valores del contexto], la información solicitada es: [source_text]'.
> Asegúrate de que esta nueva cadena siga conteniendo los valores del contexto para que la aserción de los tests unitarios pase exitosamente (estado Green), pero que en el frontend se lea como la respuesta de un asistente inteligente real. Proporcióname el bloque de código corregido para assistant.py.

### Prompt 7: Cambios en Frontend para visualización dinámica
> El backend del módulo CAG ya está completamente implementado, optimizado y superó todas las pruebas unitarias. Sin embargo, revisando el frontend, noto que el panel lateral sigue mostrando el texto por defecto del repositorio base: 'Este panel es un punto de partida. Debe mostrar contexto guardado cuando implementes /api/context.' y muestra un arreglo vacío para el usuario 'student-01'.
> Requiero que analices el código del frontend (los archivos estáticos HTML o JS). Necesito que implementes la lógica en JavaScript para:
> 1. Consumir el endpoint GET /api/context pasando el user_id activo (ej. 'student-01').
> 2. Eliminar el mensaje de placeholder.
> 3. Renderizar dinámicamente en el panel las claves y valores del contexto que devuelva el backend de forma visualmente limpia.
> Muéstrame el código JavaScript/HTML que debo modificar para integrar esta vista.
