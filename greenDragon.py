from main import dragon

class greenFlyingDragon(dragon):
    def __init__(self, speed=75, color="", type="", name = "", food = ""):
      dragon.__init__(self, speed=speed, color=color, type=type)
      self.speed = speed
      self.color = "green"
      self.type = "Flying"
      self.name = name
      self.food = "Dragonfruit"
class greenSwimmingDragon(dragon):
    def __init__(self, speed=75, color="", type="", name = "", food = ""):
      dragon.__init__(self, speed=speed, color=color, type=type)
      self.speed = speed
      self.color = "green"
      self.type = "Swimming"
      self.name = name
      self.food = "Kelp"
