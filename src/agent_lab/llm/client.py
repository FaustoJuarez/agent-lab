"""LLMClient: interfaz minima desacoplada del proveedor.

Concepto clave (M0): un LLM no es un agente. Un agente es un sistema
que usa uno o mas modelos dentro de un loop de decision y accion.
Este cliente es la frontera de invocacion del modelo: nada mas.

TODO (M0):
- Definir una interfaz LLMClient con un metodo de generacion basico
  (mensajes con roles -> respuesta + metadata de uso).
- Implementar un adapter concreto sobre el SDK del proveedor (openai).
- Exponer input_tokens, output_tokens, latencia y costo estimado
  como parte del resultado, no como print sueltos.
- Mantener esta capa libre de logica de negocio (eso va en services/
  cuando aparezca en milestones posteriores).
"""
