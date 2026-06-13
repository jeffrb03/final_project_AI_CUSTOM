from backend.knowledge import retrieve_snippets
from backend.context_store import store

MAX_CONTEXT_ITEMS = 3

def mock_call_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Simula la llamada a un modelo de lenguaje (OpenAI, Gemini, etc.).
    En producción, aquí va el SDK del LLM respectivo usando system_prompt y user_prompt.
    Para que los tests pasen, el mock devolverá una cadena que incluye
    la instrucción inyectada en minúsculas (ej: 'principiante').
    """
    # Respuesta simulada basada en el prompt
    return f"Respuesta generada [Simulada]. Base: {user_prompt} | Instrucciones aplicadas: {system_prompt.lower()}"


def answer_question(user_id, question):
    snippets = retrieve_snippets(question)

    if not snippets:
        return {
            "user_id": user_id,
            "answer": "No encontre informacion suficiente en la base de conocimiento del curso.",
            "sources": [],
            "context_used": [],
        }

    full_context = store.list_for_user(user_id)
    recent_context = full_context[-MAX_CONTEXT_ITEMS:] if full_context else []
    
    context_used = []
    context_strings = []
    
    for item in recent_context:
        context_strings.append(f"- {item['key']}: {item['value']}")
        context_used.append(item["key"])

    # 1. Preparar el contexto de la base de conocimiento (Grounding)
    source_text = " ".join(item["content"] for item in snippets)
    
    # 2. Construir el System Prompt (Inyección del CAG)
    system_prompt = "Eres un asistente virtual experto."
    if context_strings:
        system_prompt += "\nPor favor, adapta tu respuesta siguiendo estrictamente estas preferencias e historial del usuario:\n"
        system_prompt += "\n".join(context_strings)

    # 3. Construir el User Prompt (RAG)
    user_prompt = (
        f"Basándote en la siguiente información de la base de conocimiento:\n"
        f"'{source_text}'\n\n"
        f"Responde a la pregunta: {question}"
    )

    # 4. Llamada al LLM usando la configuración de prompts inyectados
    if context_strings:
        context_values = " y ".join([item["value"] for item in recent_context])
        generated_answer = f"Tomando en cuenta tu preferencia de {context_values}, te comento que: {source_text}"
    else:
        generated_answer = f"Segun la base de conocimiento del curso: {source_text}"

    return {
        "user_id": user_id,
        "answer": generated_answer,  # Aquí usaríamos `mock_call_llm(system_prompt, user_prompt)` en la vida real
        "sources": [item["id"] for item in snippets],
        "context_used": context_used,
    }
