from main import dragon

class redFlyingDragon(dragon):
  def __init__(self, speed=75, color="", type="", name = "", food = ""):
    dragon.__init__(self, speed=speed, color=color, type=type)
    self.speed = speed
    self.color = "red"
    self.type = "Flying"
    self.name = name
    self.food = "dragonfruit"
class redSwimmingDragon(dragon):
  def __init__(self, speed=75, color="", type="", name = "", food = ""):
    dragon.__init__(self, speed=speed, color=color, type=type)
    self.speed = speed
    self.color = "red"
    self.type = "Swimming"
    self.name = name
    self.food = "Kelp"
