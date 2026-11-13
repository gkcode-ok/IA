# IA - Ollama + Open WebUI en VPS

Stack en `docker-compose.yml`: Ollama (modelo llama3.2:3b), Open WebUI (chat, puerto 3000) y documentacion OpenAPI 3.0 (Swagger UI, puerto 8081).

## Levantar
    cp .env.example .env   # poner WEBUI_SECRET_KEY
    docker compose up -d

## Cliente Python
Crear la API key en Open WebUI (Ajustes > Cuenta > Claves API), luego:

    export OPENWEBUI_URL=http://srv1490900.hstgr.cloud:3000
    export OPENWEBUI_API_KEY=<tu clave>
    python3 client/chat.py "Hola, quien eres?"

Documentacion: `docs/openapi.yaml`.
