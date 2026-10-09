# 功能：定义角色战技类（爆发输出 DamageDealer/DPS、治疗 Healer）与技能倍率、冷却规则。
import random
import sys

# 运行时不生成 __pycache__，避免在项目目录落盘缓存文件
sys.dont_write_bytecode = True

from units import Character

# ==================== 技能规则 ====================
SKILL_COOLDOWN = 2          # 释放战技后进入的冷却回合数
DPS_SKILL_MULTIPLIER = 1.8  # 输出位战技倍率：伤害 = 攻击力 * 倍率
HEALER_HEAL_RATIO = 0.15    # 治疗量 = 最大生命值 * 该比例 + 攻击力 * 0.3


class DamageDealer(Character):
    """输出位：战技造成 攻击力 * 倍率 的伤害，冷却 2 回合"""

    def __init__(self, name, hp, atk, defense, speed=100, skill_multiplier=1.8):
        super().__init__(name, hp, atk, defense, speed, skill="爆发战技")
        self.skill_multiplier = skill_multiplier   # 技能倍率
        self.skill_cooldown = 0                    # 技能冷却回合数（0 表示可用）

    def use_skill(self, target):
        """爆发技能：造成攻击力 * 倍率 的伤害并进入冷却；冷却中返回 False"""
        if self.skill_cooldown > 0:
            print(f"{self.name} 的战技还在冷却中（剩余 {self.skill_cooldown} 回合）")
            return False   # 技能未释放成功

        damage = int(self.atk * self.skill_multiplier) + random.randint(-3, 3)
        damage = max(1, damage)
        actual = target.take_damage(damage)
        print(f"{self.name} 释放爆发战技，对 {target.name} 造成 {actual} 点伤害！")
        self.skill_cooldown = SKILL_COOLDOWN   # 进入冷却
        return True

    def end_turn(self):
        """每回合结束时调用，减少冷却"""
        if self.skill_cooldown > 0:
            self.skill_cooldown -= 1


class DPS(DamageDealer):
    """纯输出角色：默认使用更高的战技倍率"""

    def __init__(self, name, hp, atk, defense, speed=110, skill_multiplier=DPS_SKILL_MULTIPLIER):
        super().__init__(name, hp, atk, defense, speed, skill_multiplier)
        self.skill = "强力一击"


class Healer(Character):
    """治疗位：战技为队友恢复生命值，冷却 2 回合"""

    def __init__(self, name, hp, atk, defense, speed=90):
        super().__init__(name, hp, atk, defense, speed, skill="治疗")
        self.skill_cooldown = 0

    def use_skill(self, target):
        """治疗战技：为队友恢复生命值，冷却中返回 False"""
        if self.skill_cooldown > 0:
            print(f"{self.name} 的战技还在冷却中（剩余 {self.skill_cooldown} 回合）")
            return False

        heal_amount = self.max_hp * HEALER_HEAL_RATIO + self.atk * 0.3
        actual_heal = target.heal(heal_amount)
        print(f"{self.name} 治疗了 {target.name}，恢复了 {actual_heal} 点生命值")
        self.skill_cooldown = SKILL_COOLDOWN
        return True

    def end_turn(self):
        """每回合结束时调用，减少冷却"""
        if self.skill_cooldown > 0:
            self.skill_cooldown -= 1


if __name__ == "__main__":
    # 小演示：输出位与治疗位对训练假人释放战技（不再有“自己打自己”的硬编码调用）
    dummy = Character("训练假人", hp=3000, atk=500, defense=10, speed=50)
    p1 = DPS("P1", hp=3600, atk=2400, defense=840, speed=120)
    healer = Healer("奶妈", hp=2000, atk=300, defense=100, speed=90)

    dummy.attack(p1)          # 假人先打一下 P1
    p1.use_skill(dummy)       # P1 释放战技
    p1.use_skill(dummy)       # 冷却中，释放失败并返回 False
    healer.use_skill(p1)      # 奶妈治疗 P1
    print(p1)
    print(dummy)
