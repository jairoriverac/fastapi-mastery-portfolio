fastapi-mastery-portfolio/
├── README.md # Portada del portafolio, arquitectura, badges y guía de uso
├── pyproject.toml # Configuración unificada (Ruff linter/formatter, Pytest, Mypy)
├── requirements.txt # Dependencias globales del monorepo
├── .env.example # Plantilla de variables (OPENROUTER_API_KEY, DATABASE_URL, JWT_SECRET)
├── .gitignore # Ignorar .venv, **pycache**, .env, .pytest_cache
│
├── 01_python_crash_course/ # MÓDULO 1: Python Express (3.12+) para Senior Devs
│ ├── README.md # Cheat-sheet de sintaxis Pythonic, venv y PEP 8
│ ├── 01_types_and_variables.py # Type hints modernos (| None), Literal, colecciones y unpacking
│ ├── 02_comprehensions_and_generators.py # List/Dict comprehensions, generadores (yield) y lambdas
│ ├── 03_functions_and_decorators.py # \*args, \*\*kwargs, closures y cómo funciona un @decorador por dentro
│ ├── 04_oop_and_dataclasses.py # Clases, herencia, @dataclass, Protocol (Interfaces) y dunder methods
│ ├── 05_async_concurrency.py # Event loop (asyncio), async/await, gather() vs código bloqueante
│ └── 06_hello_fastapi_setup.py # Tu primera instancia FastAPI, comando CLI y exploración de /docs
│
├── 02_fastapi_core_and_pydantic/ # MÓDULO 2: Core de FastAPI y Pydantic v2 (Base del video)
│ ├── README.md # Guía de validación, códigos HTTP, serialización y Swagger UI
│ ├── 01_routing_and_parameters.py # Path params tipados, Query params opcionales y Enum
│ ├── 02_pydantic_models_fields.py # BaseModel, Field(gt, ge, min_length), ConfigDict y field_validator
│ ├── 03_crud_in_memory.py # CRUD completo en memoria, status_code=201 y response_model
│ ├── 04_error_handling.py # HTTPException, respuestas de error custom y Exception Handlers globales
│ └── 05_modular_routers/ # Refactorización profesional con APIRouter (del video)
│ ├── main.py
│ ├── schemas.py
│ ├── storage.py
│ └── routers/
│ └── products.py
│
├── 03_architecture_and_di/ # MÓDULO 3: Inyección de Dependencias, Lifespan y Middlewares
│ ├── README.md # Cómo funciona el grafo de Depends() e inversión de control en FastAPI
│ ├── 01_dependency_injection.py # Depends() en funciones, clases inyectables (**call**) y sub-dependencias
│ ├── 02_middlewares_and_cors.py # Custom Middleware (X-Process-Time), configuración segura de CORS y GZip
│ ├── 03_lifespan_and_settings.py # Variables de entorno tipadas con pydantic-settings y ciclo @asynccontextmanager
│ └── 04_layered_pattern_intro.py # Transición de script monolítico a capas (Router -> Service -> Repository)
│
├── 04_databases_async_orm/ # MÓDULO 4: Persistencia Asíncrona (PostgreSQL + SQLAlchemy 2.0)
│ ├── README.md # Guía de ORM asíncrono, sesiones por petición y migraciones
│ ├── 01_async_engine_session.py # AsyncEngine, async_sessionmaker y dependencia get_db() con yield
│ ├── 02_models_and_relationships.py # DeclarativeBase, Mapped, mapped_column, relaciones 1:N y N:M
│ ├── 03_async_crud_and_pagination.py # Queries asíncronas (select, where, selectinload), transacciones y paginación
│ └── 04_alembic_migrations_guide/ # Configuración de Alembic para autogenerar migraciones de base de datos
│ ├── alembic.ini
│ └── env.py
│
├── 05_security_auth_rbac/ # MÓDULO 5: Autenticación, Autorización (RBAC) y Seguridad
│ ├── README.md # Estándar OAuth2, estructura JWT, hashing seguro y OWASP API Top 10
│ ├── 01_password_hashing.py # Hashing y verificación de contraseñas con Argon2 / Bcrypt (pwdlib)
│ ├── 02_jwt_oauth2_flow.py # OAuth2PasswordBearer, Access/Refresh Tokens y dependencia get_current_user
│ ├── 03_rbac_roles_and_scopes.py # Autorización por roles (Admin, Editor, User) y OAuth2 Scopes
│ └── 04_rate_limiting_and_headers.py # Protección contra fuerza bruta (SlowAPI) y cabeceras de seguridad
│
├── 06_ai_llms_openrouter_and_rag/ # MÓDULO 6: Integración de IA (Local + OpenRouter API + Streaming + RAG)
│ ├── README.md # Arquitectura de LLMs en FastAPI, configuración de OpenRouter y patrones RAG
│ ├── 01_local_llm_httpx.py # Conexión asíncrona con llama.cpp / Ollama usando httpx (ejemplo del video)
│ ├── 02_openrouter_client_and_models.py # Consumo de OpenRouter API (httpx + SDK OpenAI), headers, routing y fallbacks
│ ├── 03_openrouter_structured_outputs.py # Forzar al LLM en OpenRouter a responder JSON validado con esquemas Pydantic
│ ├── 04_streaming_sse_and_websockets.py # StreamingResponse (Server-Sent Events) y WebSockets con tokens en vivo
│ └── 05_rag_knowledge_assistant.py # Sistema RAG: chunking, embeddings, búsqueda vectorial y respuesta vía OpenRouter
│
├── 07_testing_with_pytest/ # MÓDULO 7: Testing Profesional con Pytest y Mocking
│ ├── README.md # Pirámide de testing en FastAPI, fixtures, pruebas asíncronas y cobertura
│ ├── conftest.py # Fixtures reutilizables, cliente HTTP de prueba y BD aislada
│ ├── 01_unit_and_sync_testclient.py # Pruebas rápidas de endpoints, validaciones 422 y reglas de negocio
│ ├── 02_async_tests_httpx.py # Pruebas asíncronas reales con pytest-asyncio y httpx.AsyncClient
│ └── 03_dependency_overrides_mocking.py # Cómo mockear la BD y la API de OpenRouter en tests usando dependency_overrides
│
├── 08_production_docker_deploy/ # MÓDULO 8: Observabilidad, Tareas en 2do Plano, Docker y Despliegue
│ ├── README.md # Checklist de paso a producción, workers ASGI, contenedores y CI/CD
│ ├── 01_structured_logging_and_health.py # Logs estructurados en JSON, Correlation ID y endpoints /healthz y /readyz
│ ├── 02_background_tasks_and_redis.py # BackgroundTasks nativos de FastAPI (envío de emails/logs) y caché con Redis
│ ├── Dockerfile # Imagen Multi-stage ligera, sin privilegios root y con Gunicorn/Uvicorn
│ ├── docker-compose.yml # Orquestación local: API + PostgreSQL + Redis
│ └── github_actions_ci.yml # Pipeline de CI/CD: Linter (Ruff) -> Typecheck (Mypy) -> Pytest -> Docker Build
│
└── 09_capstone_clean_architecture_project/ # MÓDULO 9: PROYECTO FINAL SIMULADO (Todo integrado con Clean Architecture)
├── README.md # Documentación de arquitectura, diagramas, decisiones técnicas (ADRs) y uso
├── Dockerfile
├── docker-compose.yml
├── app/
│ ├── **init**.py
│ ├── main.py # Punto de entrada: ensamblaje de routers, lifespan, middlewares y excepciones
│ │
│ ├── core/ # Configuración transversal
│ │ ├── config.py # Settings centralizados (DB, JWT, OpenRouter API Key, modelo por defecto)
│ │ ├── security.py # Utilidades criptográficas y generación/validación de JWT
│ │ └── exceptions.py # Excepciones base del sistema y mapeo a respuestas HTTP
│ │
│ ├── domain/ # CAPA 1: DOMINIO (Pura, sin dependencias de frameworks ni librerías externas)
│ │ ├── entities/
│ │ │ ├── user.py # Entidad de dominio User y Enum de Roles
│ │ │ └── product.py # Entidad de dominio Product con reglas de negocio (ej. control de stock)
│ │ └── repositories/ # Interfaces (Puertos / Protocols) que la capa de infraestructura debe implementar
│ │ ├── user_repository.py
│ │ ├── product_repository.py
│ │ └── ai_provider_port.py # Contrato abstracto para el proveedor de IA
│ │
│ ├── application/ # CAPA 2: APLICACIÓN (Casos de uso / Orquestación de lógica de negocio)
│ │ ├── dtos/ # Esquemas Pydantic de entrada/salida para comunicar capas
│ │ │ ├── auth_dtos.py
│ │ │ ├── product_dtos.py
│ │ │ └── ai_dtos.py
│ │ └── use_cases/
│ │ ├── auth_use_cases.py # Registro, login y validación de permisos
│ │ ├── product_use_cases.py # CRUD de productos + generación automática de descripción SEO con IA
│ │ └── ai_assistant_use_cases.py # Chatbot de soporte sobre el catálogo en tiempo real (RAG + Streaming)
│ │
│ ├── infrastructure/ # CAPA 3: INFRAESTRUCTURA (Adaptadores concretos: BD, OpenRouter, Caché)
│ │ ├── database/
│ │ │ ├── session.py # Configuración de SQLAlchemy 2.0 Async
│ │ │ └── models.py # Modelos relacionales ORM (Tablas de Users y Products)
│ │ ├── repositories/
│ │ │ ├── sqlalchemy_user_repo.py # Implementación real del repositorio de usuarios en PostgreSQL/SQLite
│ │ │ └── sqlalchemy_product_repo.py # Implementación real del repositorio de productos
│ │ └── external_services/
│ │ └── openrouter_adapter.py # Implementación del puerto de IA conectada a https://openrouter.ai/api/v1
│ │
│ └── presentation/ # CAPA 4: PRESENTACIÓN (Adaptadores HTTP / FastAPI)
│ ├── dependencies.py # Fábrica de inyección de dependencias (conecta Repos + UseCases + Auth)
│ └── routers/
│ ├── auth_router.py # POST /api/v1/auth/register, POST /api/v1/auth/login
│ ├── products_router.py # CRUD /api/v1/products + POST /api/v1/products/{id}/generate-ai-copy
│ └── ai_chat_router.py # POST /api/v1/ai/ask y POST /api/v1/ai/stream (Catálogo + OpenRouter)
│
└── tests/ # Suite de pruebas del proyecto final
├── conftest.py # Inyección de repositorios Fake/In-Memory y Mock de OpenRouter
├── unit/
│ └── test_product_use_cases.py # Prueba la lógica de negocio aislando totalmente la BD y la IA
└── integration/
├── test_products_api.py # Prueba los endpoints HTTP de principio a fin
└── test_ai_chat_api.py # Prueba los endpoints de OpenRouter con respuestas simuladas
