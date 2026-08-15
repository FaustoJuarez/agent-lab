"""AgentLab CLI entry point.

M0 objetivo: un CLI deliberadamente pequeño y observable que haga
visible la unidad minima del sistema (una llamada a un modelo),
antes de introducir cualquier framework de agentes.

TODO (M0):
- Leer input del usuario (arg o stdin).
- Construir mensajes con roles (system/user).
- Invocar LLMClient (ver llm/client.py).
- Registrar input_tokens, output_tokens, latencia y costo por request.
- Persistir cada corrida en un log reproducible (ver experiments/results/).
"""


def main() -> None:
    raise NotImplementedError("M0: implementar el loop request -> model -> response")


if __name__ == "__main__":
    main()
