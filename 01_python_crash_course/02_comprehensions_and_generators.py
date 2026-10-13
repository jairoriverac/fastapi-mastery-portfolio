"""
SUBTEMA 02: List/Dict Comprehensions y Generadores (yield)
----------------------------------------------------------
Teoría breve:
Las 'comprehensions' permiten transformar colecciones de forma concisa y rápida
(optimizadas en C por el intérprete).
Los 'generadores' usan la palabra clave `yield` para producir elementos bajo demanda
(evaluación perezosa / Lazy Evaluation). En FastAPI, `yield` es el pilar para gestionar
el ciclo de vida de recursos (abrir conexión a BD, cederla al endpoint, cerrarla al salir).
"""

from collections.abc import Generator

# Lista de datos crudos simulando un catálogo
raw_products = [
    {"id": 1, "name": "Monitor 4K", "price": 450.0, "category": "tech"},
    {"id": 2, "name": "Mouse Vertical", "price": 45.0, "category": "ergonomics"},
    {"id": 3, "name": "Teclado Mecánico", "price": 120.0, "category": "tech"},
    {"id": 4, "name": "Escritorio Elevable", "price": 380.0, "category": "furniture"},
]

# 1. List Comprehension: Filtrado y transformación en una sola línea
# Sintaxis: [expresión for item in iterable if condición]
tech_product_names: list[str] = [
    p["name"] for p in raw_products if p["category"] == "tech"
]

# 2. Dict Comprehension: Crear mapas indexados al vuelo (Indexación O(1))
# Útil en FastAPI para crear cachés rápidas en memoria o buscar por ID
product_by_id: dict[int, dict] = {p["id"]: p for p in raw_products}

# 3. Set Comprehension: Extraer valores únicos sin duplicados
unique_categories: set[str] = {p["category"] for p in raw_products}

# 4. Generadores y `yield`: Evaluación perezosa (No almacena todo en RAM)
# Simulación de un stream de registros o lectura de archivos gigantes
def batch_streamer(items: list[dict], batch_size: int = 2) -> Generator[list[dict], None, None]:
    """Generador que produce lotes bajo demanda."""
    for i in range(0, len(items), batch_size):
        # 'yield' suspende la función y devuelve el lote actual.
        # En la siguiente iteración, la función continúa desde esta línea exacta.
        yield items[i : i + batch_size]


# 5. Patrón de ciclo de vida de recursos con yield (Precursor de Depends en FastAPI)
def database_session_simulator() -> Generator[str, None, None]:
    """Simula apertura de conexión, entrega a la lógica y cierre garantizado."""
    print("[DB Simulator] 🔌 Abriendo conexión a la base de datos...")
    session = "SESSION_ACTIVA_#42"
    try:
        yield session  # FastAPI entrega esta sesión a la función del endpoint
    finally:
        print("[DB Simulator] 🔒 Cerrando conexión y liberando pool...")


# =====================================================================
# 💡 TIPS DE USO Y BUENAS PRÁCTICAS:
# 1. Si tu comprehension tiene más de un `for` o condiciones complejas anidadas,
#    escríbela como un bucle tradicional por legibilidad.
# 2. Usa generadores cuando proceses archivos de logs o consultas de miles de registros
#    para mantener el consumo de memoria en O(1) en vez de O(N).
# =====================================================================

if __name__ == "__main__":
    print(f"Productos Tech: {tech_product_names}")
    print(f"Index por ID: {product_by_id.keys()}")
    print(f"Categorías únicas: {unique_categories}")

    print("\n--- Ejecución del generador por lotes ---")
    for batch in batch_streamer(raw_products, batch_size=2):
        print(f"Lote recibido: {[item['name'] for item in batch]}")

    print("\n--- Ciclo de vida simulado con yield ---")
    session_gen = database_session_simulator()
    conn = next(session_gen)
    print(f"Trabajando con: {conn}")
    try:
        next(session_gen)
    except StopIteration:
        pass  # El generador completó el bloque finally