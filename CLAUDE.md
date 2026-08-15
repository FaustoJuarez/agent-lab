# AgentLab — guía de trabajo para Claude Code

AgentLab es un repositorio evolutivo único: un Research & Knowledge Agent
construido incrementalmente, milestone a milestone, desde un LLM baseline
(M0) hasta producción (M13). No se construyen catorce demos aisladas.

## Regla pedagógica fundamental

**No agregues una tecnología porque sea popular.** Antes de introducir un
framework o dependencia nueva, tenés que poder describir:
1. el fallo concreto de la arquitectura actual que la motiva,
2. las alternativas consideradas,
3. el costo que introduce,
4. la métrica con la que se decidirá si valió la pena.

Si no puedo articular estos cuatro puntos, no se agrega la dependencia
todavía, aunque el milestone "la permita" más adelante.

## Ciclo de cada milestone

1. Observar una limitación concreta (no una tecnología).
2. Formular el problema sin mencionar la tecnología.
3. Construir un modelo mental.
4. Implementar el mecanismo **explícitamente**, a mano, antes de usar
   un framework para eso.
5. Instrumentarlo y probarlo (tests + logging de tokens/latencia/costo
   cuando aplique).
6. Recién ahí, si reduce complejidad accidental, introducir el framework.
7. Ejecutar un experimento *paired* contra el baseline anterior.
8. Documentar la decisión en `docs/decisions.md` (ADR).
9. Registrar el experimento en `docs/experiments.md`.
10. Commit + git tag (ver convención abajo).
11. Avanzar solo cuando se pueda explicar qué se aprendió — no antes.

## No te adelantes

No crear `agents/`, `graph/`, `memory/`, `planning/`, etc. hasta que el
milestone correspondiente justifique su existencia. La estructura final
(ver `docs/architecture.md`) es un horizonte, no un punto de partida.
Si te pido algo que salta milestones, avisame antes de implementarlo.

## Dependencias: introducirlas progresivamente

No instalar todo desde M0. Tabla completa de referencia (ver PDF fuente,
Appendix B, para versiones exactas):

| Package | Milestone | Motivo |
|---|---|---|
| openai, pydantic, pytest | M0 | Provider boundary, config/schemas, testing desde el baseline |
| pymupdf, numpy, qdrant-client | M1 | PDF parsing, cosine baseline transparente, vector store |
| langchain, langchain-openai | M2-M3 | Primitivas / tools |
| langgraph | M4 | Control flow stateful |
| langgraph-checkpoint-sqlite | M6 | Threads locales durables |
| Postgres adapters | M13 | Persistencia de producción |

## Convención de commits y tags

Un tag por milestone cerrado:
```
v0.0-llm-baseline
v0.1-basic-rag
v0.2-advanced-retrieval
v0.3-tools
v0.4-langgraph-fundamentals
v0.5-agentic-rag
v0.6-short-term-memory
v0.7-long-term-memory
v0.8-memory-retrieval
v0.9-agentic-memory
v1.0-planning
v1.1-multi-agent
v1.2-evaluation
v1.3-production
```

## Regla de dependencia interna (arquitectura horizonte)

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

El graph puede coordinar dominios; el dominio no debería importar el
graph. Esto permite testear retrieval/memory sin compilar un workflow
completo.

## Dataset de evaluación

Crece con el sistema, no se espera a M12. Cada milestone agrega labels
nuevos al dataset en `evals/datasets/`. Ver progresión completa en
`docs/architecture.md` / PDF fuente (sección "Dataset de evaluación que
crece con el sistema").

## Run manifests

Todo resultado de experimento debe poder asociarse a un manifest
reproducible (git_commit, git_tag, dataset_version, corpus_hash,
index_hash, model, config). **Si un resultado no tiene manifest, es una
observación, no un experimento reproducible.**

## Cómo quiero que trabajes conmigo

- Antes de escribir código de un milestone nuevo, resumime en 3-4
  líneas: el problema que resolvemos, el modelo mental, y qué vamos a
  implementar explícitamente antes de usar un framework.
- Al cerrar un milestone: proponeme el ADR, el registro de experimento,
  y el mensaje de commit + tag — no los hagas sin mostrármelos primero.
- Si detectás que estamos "adelantando" una capa de la arquitectura
  final antes de tiempo, decímelo aunque yo no lo haya notado.
- Priorizá tests y observabilidad (tokens, latencia, costo) desde M0,
  no como afterthought.

## Estado actual del proyecto

- Milestone activo: **M0 - Foundations & LLM Baseline**
- Repo inicial creado (ver estructura en `README.md`), sin tags todavía.
- Próximo tag esperado: `v0.0-llm-baseline`
