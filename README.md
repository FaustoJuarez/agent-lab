# AgentLab

LLM, agents, RAG, memory, multiagent concepts building from foundation structures to more complex systems.

Research & Knowledge Agent construido incrementalmente desde primeros principios.

Ver `CLAUDE.md` para la metodología de trabajo con Claude Code.
Ver `docs/architecture.md`, `docs/decisions.md` y `docs/experiments.md` para el estado del proyecto milestone a milestone.

## Setup

​```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\Activate.ps1   # Windows PowerShell

python -m pip install --upgrade pip
pip install -e ".[dev]"

cp .env.example .env   # completar OPENAI_API_KEY
​```

## Comandos

​```bash
python -m agent_lab.main          # ejecutar CLI
pytest tests/unit                 # unit tests
pytest tests/integration          # integración
​```

## Estado actual

- Milestone activo: **M0 - Foundations & LLM Baseline**
- Último tag: (ninguno todavía — el primer tag será `v0.0-llm-baseline`)