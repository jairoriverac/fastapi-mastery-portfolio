"""
SUBTEMA 03: Funciones Avanzadas, *args, **kwargs y Decoradores (@)
-------------------------------------------------------------------
Teoría breve:
Los decoradores son funciones de orden superior que reciben una función,
envuelven su ejecución (añadiendo lógica antes o después) y retornan una nueva función.
FastAPI utiliza decoradores como `@app.get("/ruta")` para interceptar la función del
endpoint y registrarla en el enrutador ASGI con toda su metadata de OpenAPI.
"""

from collections.abc import Callable
import functools
import time
from typing import Any

# 1. *args (tupla de argumentos posicionales variables)
#    **kwargs (diccionario de argumentos con nombre variables)
def flexible_logger(prefix: str, *args: Any, **kwargs: Any) -> None:
    """Acepta cualquier cantidad de argumentos adicionales."""
    print(f"[{prefix.upper()}] Args posicionales: {args} | Claves con nombre: {kwargs}")


# 2. Cómo funciona un decorador por dentro
def measure_execution_time(func: Callable) -> Callable:
    """
    Decorador que mide el tiempo de respuesta de una función.
    @functools.wraps(func) preserva el nombre original y el docstring de la función,
    lo cual es crítico en FastAPI para que Swagger UI no pierda la documentación del endpoint.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        # Ejecuta la función original envuelta
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start_time) * 1000
        print(f"⏱️ [{func.__name__}] Ejecutado en {elapsed:.2f} ms")
        return result

    return wrapper


# 3. Decoradores que aceptan parámetros de configuración (Fábricas de decoradores)
# Así es exactamente como operan `@app.get("/users", tags=["users"])`
def require_role(role_name: str) -> Callable:
    """Fábrica de decoradores que recibe argumentos para configurar el wrapper."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Simulación de contexto de usuario
            current_user_role = kwargs.get("user_role", "guest")
            if current_user_role != role_name:
                raise PermissionError(
                    f"Acceso denegado: Se requiere rol '{role_name}', pero se recibió '{current_user_role}'"
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 4. Aplicación de los decoradores con la sintaxis '@'
@measure_execution_time
def complex_math_computation(limit: int) -> int:
    """Suma acumulativa para simular procesamiento."""
    return sum(i * 2 for i in range(limit))


@require_role("admin")
def delete_database_record(record_id: int, user_role: str = "guest") -> str:
    return f"Registro #{record_id} eliminado exitosamente."


# =====================================================================
# 💡 TIPS DE USO Y BUENAS PRÁCTICAS:
# 1. Siempre usa `@functools.wraps(func)` al escribir decoradores. Sin esto,
#    la función decorada cambiará su nombre a 'wrapper', rompiendo Swagger en FastAPI.
# 2. FastAPI usa decoradores para enrutamiento, pero para seguridad y reglas de negocio
#    la comunidad prefiere `Depends()` en lugar de decoradores propios para facilitar tests.
# =====================================================================

if __name__ == "__main__":
    flexible_logger("worker", 100, 200, status="active", region="us-east-1")

    res = complex_math_computation(500_000)
    print(f"Resultado de cálculo: {res}")

    try:
        # Falla con guest
        delete_database_record(42, user_role="guest")
    except PermissionError as err:
        print(f"Capturado: {err}")

    # Exitoso con admin
    print(delete_database_record(42, user_role="admin"))