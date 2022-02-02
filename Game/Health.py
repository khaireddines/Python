class Health:
    def __init__(self, health):
        self.health = health

    def UsePotion(self):
        pass

    def GetHealth(self):
        print(f'Remaining health: {self.health}')


