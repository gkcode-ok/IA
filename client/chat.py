#!/usr/bin/env python3
"""Cliente de chat para Open WebUI (API compatible con OpenAI) con llama3.2:3b.

Uso:
  export OPENWEBUI_URL=http://srv1490900.hstgr.cloud:3000
  export OPENWEBUI_API_KEY=sk-xxxxxxxx
  python3 client/chat.py "Hola, quien eres?"
"""
import json
import os
import sys
import urllib.error
import urllib.request

BASE_URL = os.environ.get("OPENWEBUI_URL", "http://srv1490900.hstgr.cloud:3000").rstrip("/")
API_KEY = os.environ.get("OPENWEBUI_API_KEY", "")
MODEL = os.environ.get("OPENWEBUI_MODEL", "llama3.2:3b")


def chat(messages, model=MODEL):
    """Envia el historial de mensajes y devuelve el texto de respuesta."""
    if not API_KEY:
        raise SystemExit("Falta la variable OPENWEBUI_API_KEY")
    payload = json.dumps({"model": model, "messages": messages, "stream": False}).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/api/chat/completions",
        data=payload,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as err:
        raise SystemExit(f"HTTP {err.code}: {err.read().decode(errors='replace')}")
    return data["choices"][0]["message"]["content"]


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Uso: python3 client/chat.py "tu pregunta"')
    print(chat([{"role": "user", "content": " ".join(sys.argv[1:])}]))


if __name__ == "__main__":
    main()
