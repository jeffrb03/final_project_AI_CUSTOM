const askForm = document.querySelector("#ask-form");
const answerOutput = document.querySelector("#answer-output");
const contextOutput = document.querySelector("#context-output");

const API_BASE_URL = "http://127.0.0.1:8000";

askForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(askForm);
  const payload = {
    user_id: formData.get("user_id"),
    question: formData.get("question"),
  };

  answerOutput.textContent = "Consultando...";

  try {
    const response = await fetch(`${API_BASE_URL}/api/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const result = await response.json();
    answerOutput.textContent = JSON.stringify(result, null, 2);
    await loadContext(payload.user_id);
  } catch (error) {
    answerOutput.textContent = `No se pudo conectar con el backend: ${error.message}`;
  }
});

async function loadContext(userId) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/context?user_id=${encodeURIComponent(userId)}`);
    
    if (!response.ok) throw new Error("Error en la petición");
    
    const result = await response.json();
    const contextItems = result.context || [];
    
    if (contextItems.length === 0) {
      contextOutput.innerHTML = "<em>Sin contexto guardado para este usuario.</em>";
      return;
    }
    
    // Renderizamos las claves y valores dinámicamente
    contextOutput.innerHTML = "";
    contextItems.forEach(item => {
      const p = document.createElement("p");
      p.innerHTML = `<strong style="color: var(--primary-color)">${item.key}:</strong> ${item.value}`;
      p.style.margin = "0.5rem 0";
      contextOutput.appendChild(p);
    });
    
  } catch (error) {
    contextOutput.innerHTML = "<em>El modulo CAG aún no está disponible o hubo un error.</em>";
  }
}

// Cargar el contexto del usuario inicial apenas cargue la página
const initialUserId = document.querySelector("#user-id").value;
loadContext(initialUserId);
