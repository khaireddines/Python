class Skill:
    def __init__(self, *skills):
        self.skills = skills
        self.pointsInSkills = {x: 1 for x in skills}

    def GetSkills(self):
        print(self.skills)

    def GetASkill(self):
        skill = input('name of the skill ? \n')
        try:
            print({self.skills[self.skills.index(skill)]: self.pointsInSkills[skill]})
        except:
            print('skill doesn\'t exist')

    def AddPointToASkill(self):
        skill = input('name of the skill ? \n')
        try:
            self.pointsInSkills[skill] += 1
        except:
            print('skill doesn\'t exist')

    def ShowPointsInSkills(self):
        print(self.pointsInSkills)

    def AddASkillIfNotExist(self):
        skill = input('name of the skill ? \n')
        self.skills += (skill,)
        self.pointsInSkills[skill] = 1
