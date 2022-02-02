from Game.Character import Character


class Player(Character):
    def __init__(self, health, damage, *skills):
        Character.__init__(self, health, damage, *skills)

    def __str__(self):
        return f'my Health: {self.health}, i deal {self.damage}, and my skills are {self.skills}'
