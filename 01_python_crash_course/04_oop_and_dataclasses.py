"""
SUBTEMA 04: Clases, @dataclass, Protocol (Duck Typing) y Métodos Dunder
----------------------------------------------------------------------
Teoría breve:
En Python, los 'dunder methods' (doble guión bajo como `__init__`, `__call__`) permiten
sobrecargar comportamientos del lenguaje. Implementar `__call__` convierte una instancia
de clase en una función ejecutable, patrón fundamental en FastAPI para crear dependencias
inyectables con estado (ej. clases de verificación de permisos y rate limiting).
"""

from dataclasses import dataclass, field
from typing import Protocol


# 1. Clases clásicas y el método mágico `__call__`
class ApiKeyValidator:
    """
    Clase invocable (*Callable class*).
    Al definir `__call__`, la instancia se puede ejecutar como una función: validator("key123")
    """

    def __init__(self, valid_keys: list[str]) -> None:
        self._valid_keys = set(valid_keys)

    def __call__(self, provided_key: str) -> bool:
        """Permite que FastAPI use esta clase directamente dentro de Depends()."""
        return provided_key in self._valid_keys


# 2. @dataclass: Estructuras de datos ligeras sin boilerplate de __init__ y __repr__
# Es el análogo nativo en la librería estándar de un `record` en C#
@dataclass(frozen=True)  # frozen=True la hace inmutable (solo lectura)
class ServiceEndpoint:
    path: str
    method: str = "GET"
    rate_limit: int = 100
    tags: list[str] = field(default_factory=list)


# 3. Interfaces estructurales con `typing.Protocol` (Duck Typing Estático)
# Si una clase implementa los métodos del Protocol, se considera válida sin heredar explícitamente.
class NotificationSender(Protocol):
    def send(self, recipient: str, message: str) -> bool:
        """Firma requerida por el contrato."""
        ...


# Implementación concreta 1
class EmailSender:
    def send(self, recipient: str, message: str) -> bool:
        print(f"📧 Correo enviado a {recipient}: {message}")
        return True


# Implementación concreta 2
class SlackSender:
    def send(self, recipient: str, message: str) -> bool:
        print(f"💬 Mensaje enviado a canal Slack #{recipient}: {message}")
        return True


def dispatch_alert(sender: NotificationSender, target: str, text: str) -> None:
    """Acepta cualquier objeto que cumpla el contrato de NotificationSender."""
    sender.send(target, text)


# =====================================================================
# 💡 TIPS DE USO Y BUENAS PRÁCTICAS:
# 1. Usa `@dataclass` para objetos internos de tu dominio (lógica de negocio interna).
# 2. Usa `BaseModel` de Pydantic cuando los datos crucen la frontera de la API
#    (validación de requests HTTP entrantes y serialización de respuestas JSON).
# 3. Usa `Protocol` para desacoplar casos de uso de adaptadores en Clean Architecture.
# =====================================================================

if __name__ == "__main__":
    # Prueba de clase invocable (__call__)
    auth_check = ApiKeyValidator(["secret-token-1", "secret-token-2"])
    print(f"¿Token válido?: {auth_check('secret-token-1')}")
    print(f"¿Token inválido?: {auth_check('hacker-token')}")

    # Dataclass inmutable
    endpoint = ServiceEndpoint(path="/api/v1/orders", tags=["orders", "billing"])
    print(f"Endpoint configurado: {endpoint}")

    # Polimorfismo mediante Protocol
    dispatch_alert(EmailSender(), "sre@empresa.com", "Alerta de CPU alta")
    dispatch_alert(SlackSender(), "devops-alerts", "Alerta de latencia")