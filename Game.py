class character:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage =damage
        self.speed = speed
    def take_damage(self,amount):
        self.health -=amount
class Lunar_Lancer(character):
    def __init__(self,health,damage,speed):
        super().__init__(health,damage,speed)
        self.speed_modifier=1.2
    def Speed_up(self, amount):
        ModAmount=amount*self.speed_modifier
        super().Speed_up(ModAmount)

class Dracolyte(character):
    def __init__(self,health,damage,speed):
        super().__init__(health,damage,speed)
        self.armor_modifier=0.90
    def take_damage(self, amount):
        ModAmount=amount*self.armor_modifier
        super().take_damage(ModAmount)

class Shadow_Hunter(character):
    def __init__(self,health,damage,speed):
        super().__init__(health,damage,speed)
        self.armor_modifier=0.90
    def take_damage(self, amount):
        ModAmount=amount*self.armor_modifier
        super().take_damage(ModAmount)

class Neon_Ninja(character):
    def __init__(self,health,damage,speed):
        super().__init__(health,damage,speed)
        self.armor_modifier=0.90
    def take_damage(self, amount):
        ModAmount=amount*self.armor_modifier
        super().take_damage(ModAmount)
