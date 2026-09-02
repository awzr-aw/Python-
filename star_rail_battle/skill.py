# 此文件用于设计角色
from character import Character_role
class Character(Character_role):
    def __init__(self, name, hp, atk, defen, speed, normal_attack, skill):
        super().__init__(name, hp, atk, defen, speed)
        self.normal_attack = normal_attack
        self.skill = skill
p1 = Character("角色1", 3600, 2500, 840, 120, "普通攻击", "技能1")
normal_attack_s = p1.atk * 1.5
skill_s = p1.atk * 3
print(normal_attack_s)
print(skill_s)
print(p1.normal_attack)

