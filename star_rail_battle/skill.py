# 此文件用于设计角色
from character import Character_role
class Character(Character_role):
    def __init__(self, name, hp, atk, defen, speed):
        super().__init__(name, hp, atk, defen, speed)

# class Healer(Character):
#     def use_skill(self, target):
#         heal_amount = self.max_hp * 0.15 + self.atk * 0.3
#         actual_heal = target.heal(heal_amount)
#         print(f"{self.name} 治疗了 {target.name}，恢复了 {actual_heal:.0f} 点生命值")

class DPS(Character):
    def use_skill(self, target_boos):
        normal_damage = self.atk * 1.5
        print(f"{self.name} 使用了技能，对 {target_boos.name} 造成了 {normal_damage:.0f} 点伤害")
p1 = DPS("P1", 3600, 2400, 840, 120)
p1.use_skill(p1) # 输出：P1 使用了技能，对 P1 造成了 75.0 点伤害


