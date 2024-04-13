from main import dragon

class blueFlyingDragon(dragon):
    def __init__(self, speed=75, color="", type="", name = "", food = ""):
      dragon.__init__(self, speed=speed, color=color, type=type)
      self.speed = speed
      self.color = "blue"
      self.type = "Flying"
      self.name = name
      self.food = "Dragonfruit"
class blueSwimmingDragon(dragon):
    def __init__(self, speed=75, color="", type="", name = "", food = ""):
      dragon.__init__(self, speed=speed, color=color, type=type)
      self.speed = speed
      self.color = "blue"
      self.type = "Swimming"
      self.name = name
      self.food = "Kelp"
