from Game.Health import Health
from Game.Impact import Impact
from Game.Skills import Skill


class Character(Health, Impact, Skill):
    def __init__(self, health, damage, *skills):
        Health.__init__(self, health)
        Impact.__init__(self, damage)
        Skill.__init__(self, *skills)
