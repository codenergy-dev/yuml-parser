import ast

def parse_value(value: str):
  value = value.strip()
  if value.lower() in ("true", "false"):
    return value.lower() == "true"
  if value.lower() == "none":
    return None
  try:
    evaluated = ast.literal_eval(value)
    if isinstance(evaluated, (list, dict, tuple)):
      return evaluated
  except (ValueError, SyntaxError):
      pass
  try:
    if '.' in value:
      return float(value)
    return int(value)
  except ValueError:
    return value  # fallback to string