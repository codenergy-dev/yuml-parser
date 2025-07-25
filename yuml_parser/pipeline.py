class Pipeline:
  def __init__(self, name: str, function: str, args: dict = None):
    self.name = name
    self.function = function
    self.args: dict = args if args else {}
    self.fanIn: list[str] = []
    self.fanOut: list[str] = []