"""
SUBTEMA 05: Asincronía Cooperativa y Event Loop (`asyncio`)
-----------------------------------------------------------
Teoría breve:
Python corre en un solo hilo con el GIL (Global Interpreter Lock). La asincronía con
`async def` y `await` implementa concurrencia cooperativa mediante un Event Loop.
Cuando un endpoint hace una llamada I/O (consulta a PostgreSQL, llamada a OpenRouter API),
cede el control (`await`), permitiendo que el servidor atienda miles de peticiones
concurrentes en el mismo worker sin bloquearse.

⚠️ Regla de oro en FastAPI:
- Si haces I/O asíncrono (httpx, asyncpg), usa `async def`.
- Si usas librerías síncronas bloqueantes (requests, time.sleep), usa `def` tradicional:
  FastAPI automáticamente enviará las funciones `def` a un ThreadPool separado para no congelar el Event Loop.
"""

import asyncio
import time


# Simulación de tarea I/O asíncrona (ej. consulta HTTP a un LLM en OpenRouter)
async def fetch_llm_response(prompt_id: int, latency_seconds: float) -> dict[str, str | int]:
    print(f"🤖 [Task {prompt_id}] Enviando consulta al modelo...")
    # asyncio.sleep cede el control al Event Loop (NO bloquea el hilo)
    await asyncio.sleep(latency_seconds)
    print(f"✅ [Task {prompt_id}] Respuesta recibida.")
    return {"id": prompt_id, "status": "completed"}


# Simulación de tarea bloqueante síncrona
def blocking_legacy_io() -> str:
    # time.sleep CONGELA el hilo completo
    time.sleep(1.0)
    return "Operación síncrona completada"


async def main_demo() -> None:
    print("--- 1. Ejecución Secuencial (Lenta) ---")
    start = time.perf_counter()
    await fetch_llm_response(1, 0.5)
    await fetch_llm_response(2, 0.5)
    print(f"Tiempo total secuencial: {(time.perf_counter() - start):.2f}s")

    print("\n--- 2. Concurrencia con asyncio.gather (Rápida) ---")
    start = time.perf_counter()
    # Ejecuta múltiples corrutinas concurrentemente en el mismo hilo
    results = await asyncio.gather(
        fetch_llm_response(3, 0.5),
        fetch_llm_response(4, 0.5),
        fetch_llm_response(5, 0.5),
    )
    print(f"Resultados concurrentes: {results}")
    print(f"Tiempo total concurrente: {(time.perf_counter() - start):.2f}s (Casi 0.5s)")

    print("\n--- 3. Ejecución segura de código bloqueante en hilo secundario ---")
    # asyncio.to_thread evita congelar el Event Loop al llamar librerías heredadas
    legacy_result = await asyncio.to_thread(blocking_legacy_io)
    print(f"Resultado en hilo seguro: {legacy_result}")


# =====================================================================
# 💡 TIPS DE USO Y BUENAS PRÁCTICAS:
# 1. NUNCA uses `time.sleep()` ni `requests.get()` dentro de un `async def` en FastAPI.
#    Congelarás todos los requests de todos los clientes concurrentes.
# 2. Usa `httpx.AsyncClient` para llamadas HTTP externas y `asyncpg` para PostgreSQL.
# =====================================================================

if __name__ == "__main__":
    # Inicia el Event Loop de Python
    asyncio.run(main_demo())