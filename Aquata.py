from main import lands

class aquata(lands):
  def __init__(self, name = "", food = "", type = ""):
    lands.__init__(self, name = name, food = food, type = type)
    self.name = "Aqutata"
    self.food = "Seaweed"
    self.type = "Float"