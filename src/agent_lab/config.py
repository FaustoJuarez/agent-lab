"""Settings tipados con pydantic.

M0 objetivo: centralizar configuracion (API key, modelo, results dir)
leida desde variables de entorno / .env, sin hardcodear nada en el
resto del codigo.

TODO (M0):
- Definir una clase Settings (pydantic BaseSettings o equivalente).
- Cargar OPENAI_API_KEY, AGENTLAB_MODEL, AGENTLAB_RESULTS_DIR.
- Fallar rapido y con mensaje claro si falta una variable requerida.
"""
