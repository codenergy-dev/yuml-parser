class Pipeline:
  def __init__(self, name: str, function: str, group: str, args: dict = None):
    self.name = name
    self.function = function
    self.group = group
    self.args: dict = args if args else {}
    self.fanIn: list[str] = []
    self.fanOut: list[str] = []