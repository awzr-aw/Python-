# 功能：定义星穹铁道回合制战斗的基础单位类（Character_role 基类与 Character 子类）。
import random


class Character_role:
    """所有战斗单位的基类：名称、血量、攻击力、防御力、速度、普攻与战技方法"""

    def __init__(self, name, hp, atk, defense, speed):
        self.name = name          # 名称
        self.max_hp = hp          # 最大生命值
        self.hp = hp              # 当前生命值
        self.atk = atk            # 攻击力
        self.defense = defense    # 防御力（固定减伤数值）；原文件此处拼写有误，已统一修正为 defense
        self.speed = speed        # 速度

    def is_alive(self):
        """是否存活"""
        return self.hp > 0

    def take_damage(self, damage):
        """受到伤害，减去防御力，但至少造成 1 点伤害"""
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        return actual_damage

    def heal(self, amount):
        """恢复生命值，不超过最大生命值，返回实际恢复量"""
        actual_heal = min(int(amount), self.max_hp - self.hp)
        if actual_heal < 0:
            actual_heal = 0
        self.hp += actual_heal
        return actual_heal

    def attack(self, target):
        """普通攻击，伤害 = 攻击力 + 随机波动（-2~+2）"""
        base_damage = self.atk + random.randint(-2, 2)
        damage = max(1, base_damage)   # 至少 1 点
        actual = target.take_damage(damage)
        print(f"{self.name} 对 {target.name} 发动普通攻击，造成 {actual} 点伤害")
        return actual

    def use_skill(self, target):
        """战技接口，由子类实现；基类默认没有可用战技"""
        print(f"{self.name} 没有可释放的战技")
        return False

    def end_turn(self):
        """回合结束时的清理钩子，子类可重写（例如减少战技冷却）"""

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"


class Character(Character_role):
    """可操作角色类：在基类之上增加战技属性"""

    def __init__(self, name, hp, atk, defense, speed, skill=None):
        super().__init__(name, hp, atk, defense, speed)
        self.skill = skill   # 战技名称或战技对象
