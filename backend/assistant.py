from backend.knowledge import retrieve_snippets
from backend.context_store import store

MAX_CONTEXT_ITEMS = 3

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
        context_strings.append(item["value"])
        context_used.append(item["key"])

    source_text = " ".join(item["content"] for item in snippets)
    answer = f"Segun la base de conocimiento del curso: {source_text}"
    
    if context_strings:
        answer += f" [Contexto aplicado: {' | '.join(context_strings)}]"

    return {
        "user_id": user_id,
        "answer": answer,
        "sources": [item["id"] for item in snippets],
        "context_used": context_used,
    }
