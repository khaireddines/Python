from Player import Player
from collections import deque
newPlayer = Player(200, 900, 'dark', 'frost')
while 1:
    action = input('what type of action you need to do \n')
    switcher = {
        1: newPlayer.GetHealth,
        2: newPlayer.GetSkills,
        3: newPlayer.GetASkill,
        4: newPlayer.GetSpecificDmgPropriety,
        5: newPlayer.GetDmg,
        6: newPlayer.GotDmg,
        7: newPlayer.UsePotion,
        8: newPlayer.AddASkillIfNotExist,
        9: newPlayer.AddPointToASkill,
        10: newPlayer.ShowPointsInSkills
    }
    func = switcher.get(int(action), lambda: "Invalid Action")
    func()
