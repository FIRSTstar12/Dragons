class user():
  def __init__(self, name="", bondedDragons = [], foodTypes = []):
    self.name = name
    self.bondedDragons = bondedDragons
    self.foodTypes = foodTypes

class dragon():
  def __init__(self, speed = 75, color = "", type = ""):
    self.speed = speed
    self.color = color
    self.type = type
class lands():
  def __init__(self, name = "", food = "", type = ""):
    self.name = name
    self.type = type
