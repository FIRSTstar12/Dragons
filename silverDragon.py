from main import dragon

class goldFlyingDragon(dragon):
    def __init__(self, speed=75, color="", type="", name = "", food = ""):
      dragon.__init__(self, speed=speed, color=color, type=type)
      self.speed = speed
      self.color = "silver"
      self.type = "Flying"
      self.name = name
      self.food = "Dragonfruit"
class goldSwimmingDragon(dragon):
    def __init__(self, speed=75, color="", type="", name = "", food = ""):
      dragon.__init__(self, speed=speed, color=color, type=type)
      self.speed = speed
      self.color = "silver"
      self.type = "Swimming"
      self.name = name
      self.food = "Kelp"
