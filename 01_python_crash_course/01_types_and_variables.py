"""
SUBTEMA 01: Declaraciones, Colecciones y Type Hints Modernos (Python 3.10 - 3.12+)
----------------------------------------------------------------------------------
Teoría breve:
A diferencia de lenguajes compilados, el intérprete de Python no valida tipos en tiempo
de compilación. Sin embargo, FastAPI lee estas anotaciones en runtime mediante reflexión
(__annotations__) para validar payloads entrantes con Pydantic y generar esquemas OpenAPI.
"""

from typing import Any, Literal

# 1. Variables primitivas con Type Hints explícitos
service_name: str = "Orders Microservice"
http_port: int = 8080
cpu_threshold: float = 85.5
is_healthy: bool = True

# 2. Unión de tipos y valores nulos (Sintaxis moderna con '|')
# En lugar del antiguo `Optional[str]`, usamos `str | None`
database_url: str | None = None
unique_id: int | str = "ORD-99823"  # Acepta tanto entero como string

# 3. Tipos Literales (Enum ligero para restringir opciones)
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]
current_log_level: LogLevel = "INFO"

# 4. Colecciones nativas fuertemente tipadas
endpoints_whitelist: list[str] = ["/health", "/metrics", "/docs"]
status_codes: set[int] = {200, 201, 204, 400, 404, 500}
coordinates: tuple[float, float] = (-0.1807, -78.4678)  # Tupla inmutable

# Diccionario tipado (Clave: Valor)
# En FastAPI, retornar un dict se traduce automáticamente a un JSON 200 OK.
server_metadata: dict[str, Any] = {
    "name": service_name,
    "port": http_port,
    "active": is_healthy,
    "tags": ["core", "payments"],
}

# 5. Unpacking (Desestructuración) idiomático
latitude, longitude = coordinates  # Desestructuración posicional de tupla
first_endpoint, *other_endpoints = endpoints_whitelist  # Rest pattern (*)

# Fusión de diccionarios (Spread operator en Python es '**')
base_headers = {"Content-Type": "application/json"}
auth_headers = {**base_headers, "Authorization": "Bearer token_abc"}


def format_status_report(
    service: str,
    port: int,
    status: bool,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Ejemplo de función con argumentos posicionales, tipos y valor por defecto."""
    return {
        "status": "UP" if status else "DOWN",  # Operador ternario en Python
        "target": f"{service}:{port}",  # f-string (interpolación rápida)
        "extra": metadata or {},
    }


# =====================================================================
# 💡 TIPS DE USO Y BUENAS PRÁCTICAS:
# 1. NUNCA uses un tipo mutable (`list` o `dict`) como valor por defecto en una función:
#    ❌ def bad_func(items: list[str] = []): items.append("x") -> Se comparte en memoria!
#    ✅ def good_func(items: list[str] | None = None): items = items or []
# 2. Usa siempre f-strings: `f"{var}"` es mucho más rápido que `"%s" % var` o `.format()`.
# =====================================================================

if __name__ == "__main__":
    print(f"Auth Headers: {auth_headers}")
    report = format_status_report(service_name, http_port, is_healthy, server_metadata)
    print(f"Reporte generado: {report}")