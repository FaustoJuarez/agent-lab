# Architecture

Este documento describe la arquitectura **actual** del sistema, no la arquitectura final. Se actualiza al cerrar cada milestone.

## M0 - Foundations & LLM Baseline

_Pendiente de completar tras implementar M0._

Componentes esperados:
- `LLMClient`: interfaz mínima desacoplada del proveedor.
- Registro de ejecuciones (input/output tokens, latencia, costo).
- Dataset de evaluación inicial (10-15 ejemplos: `question`, `expected_topics`).

## Regla de dependencia interna (horizonte, no punto de partida)

```
domain/types
   ↑
adapters (LLM, vector DB, store)
   ↑
services (retrieval, memory, tools)
   ↑
graph/orchestration
   ↑
API/CLI
```

El graph puede coordinar dominios; el dominio no debería importar el graph.
