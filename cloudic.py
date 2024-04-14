from main import lands

class cloudic(lands):
  def __init__(self, name = "", food = "", type = ""):
    lands.__init__(self, name = name, food = food, type = type)
    self.name = "Cloudic"
    self.food = "Skyberries"
    self.type = "Float"