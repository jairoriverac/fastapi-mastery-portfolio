# 🚀 FastAPI & Modern Python Mastery Portfolio

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-E92063?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)
[![Ruff](https://img.shields.io/badge/Linter-Ruff-FCC21B?style=flat&logo=ruff&logoColor=black)](https://astral.sh/ruff)
[![OpenRouter](https://img.shields.io/badge/AI-OpenRouter-6366F1?style=flat)](https://openrouter.ai)
[![Clean Architecture](https://img.shields.io/badge/Architecture-Clean-brightgreen?style=flat)]()

Portafolio práctico y ruta de estudio estructurada sobre **FastAPI**, **Python moderno (3.12+)**, patrones de **Clean Architecture**, integración con modelos de IA vía **OpenRouter**, persistencia asíncrona y despliegues orientados a producción.

Este repositorio está organizado como un **monorepo progresivo**. Cada módulo es autocontenido, cuenta con su propia documentación teórica concisa (`README.md`), ejemplos ejecutables en `.py` y suites de pruebas automatizadas con `pytest`.

---

## 🗺️ Mapa de Ruta del Portafolio

1. **`01_python_crash_course/`**: Sintaxis Pythonic moderna, Type Hints, decoradores, asincronía (`asyncio`) y primer endpoint.
2. **`02_fastapi_core_and_pydantic/`**: Routing, parámetros de URL/Query, validación estricta con Pydantic v2, CRUD en memoria, manejo de errores y modularización con `APIRouter`.
3. **`03_architecture_and_di/`**: Grafo de Inyección de Dependencias (`Depends`), middlewares, ciclo `lifespan` y configuración tipada.
4. **`04_databases_async_orm/`**: PostgreSQL asíncrono con SQLAlchemy 2.0 (`AsyncSession`), relaciones y migraciones con Alembic.
5. **`05_security_auth_rbac/`**: Autenticación OAuth2 con JWT, hashing Argon2/Bcrypt, control de acceso basado en roles (RBAC) y Rate Limiting.
6. **`06_ai_llms_openrouter_and_rag/`**: Integración con OpenRouter API (Claude, GPT, DeepSeek), Structured Outputs forzados a esquemas Pydantic, streaming SSE y mini pipeline RAG.
7. **`07_testing_with_pytest/`**: Testing unitario y de integración, `TestClient`, `AsyncClient`, fixtures y `dependency_overrides`.
8. **`08_production_docker_deploy/`**: Observabilidad estructurada, tareas en segundo plano (`BackgroundTasks`), Docker multi-stage, Docker Compose y GitHub Actions.
9. **`09_capstone_clean_architecture_project/`**: Proyecto final simulado integrando todas las capas bajo Clean Architecture (Domain -> Application -> Infrastructure -> Presentation).

---

## ⚡ Guía Rápida de Instalación y Ejecución

```bash
# 1. Clonar el repositorio
git clone [https://github.com/tu-usuario/fastapi-mastery-portfolio.git](https://github.com/tu-usuario/fastapi-mastery-portfolio.git)
cd fastapi-mastery-portfolio

# 2. Crear y activar el entorno virtual
python -m venv .venv
source .venv/bin/activate       # En Linux/macOS
# .venv\Scripts\Activate.ps1    # En Windows PowerShell

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Copiar variables de entorno
cp .env.example .env

# 5. Formatear y validar calidad del código con Ruff
ruff check .
ruff format .

# 6. Ejecutar todas las pruebas
pytest
```
