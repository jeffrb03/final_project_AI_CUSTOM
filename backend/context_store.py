"""Módulo para persistencia del Context-Aware Generation (CAG) en memoria."""

class ContextStore:
    def __init__(self):
        # Almacenamiento en memoria. Estructura:
        # {
        #    "user_id": [ {"key": "pref", "value": "xyz"}, ... ]
        # }
        self._store = {}

    def save(self, user_id, key, value):
        """
        Agrega o actualiza un contexto para un usuario específico.
        """
        if user_id not in self._store:
            self._store[user_id] = []
            
        # Si la clave ya existe para el usuario, actualizamos su valor. 
        # Si no, la agregamos al historial.
        for item in self._store[user_id]:
            if item["key"] == key:
                item["value"] = value
                return True
                
        self._store[user_id].append({"key": key, "value": value})
        return True

    def list_for_user(self, user_id):
        """
        Recupera el historial completo de contextos de un usuario específico.
        Retorna una lista vacía si el usuario no tiene contexto guardado.
        """
        return self._store.get(user_id, [])

# Instancia global para ser importada desde server.py y assistant.py
store = ContextStore()
