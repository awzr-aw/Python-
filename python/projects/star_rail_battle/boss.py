# 功能：定义 Boss 类，包含怒气/激怒机制与激怒后的追加攻击。
import sys

# 运行时不生成 __pycache__，避免在项目目录落盘缓存文件
sys.dont_write_bytecode = True

from units import Character


class Boss(Character):
    """Boss：血量与攻击更高，血量低于阈值时进入激怒状态，激怒后普攻附带一次追加攻击"""

    def __init__(self, name, hp, atk, defense, speed=80, rage_threshold=0.3, rage_multiplier=1.5):
        super().__init__(name, hp, atk, defense, speed)
        self.rage_threshold = rage_threshold    # 血量低于此比例时进入激怒状态
        self.rage_multiplier = rage_multiplier  # 激怒后的攻击力倍率
        self.is_raged = False                   # 是否已激怒

    def take_damage(self, damage):
        """重写受伤方法，检测血量触发激怒"""
        actual = super().take_damage(damage)
        # 检查是否进入激怒状态
        if not self.is_raged and self.max_hp > 0 and self.hp / self.max_hp <= self.rage_threshold:
            self.is_raged = True
            print(f"警告：{self.name} 被激怒了！攻击力提升！")
            self.atk = int(self.atk * self.rage_multiplier)   # 攻击力提升
        return actual

    def boss_attack(self, target):
        """Boss 的普通攻击，若处于激怒状态则追加一次攻击"""
        print(f"{self.name} 发动攻击！")
        self.attack(target)
        if self.is_raged and target.is_alive():
            print(f"{self.name} 因激怒追加一次攻击！")
            self.attack(target)


if __name__ == "__main__":
    # 小演示：Boss 攻击训练假人，展示激怒与追加攻击
    dummy = Character("训练假人", hp=500, atk=10, defense=5, speed=50)
    demo_boss = Boss("演示Boss", hp=1000, atk=80, defense=10, rage_threshold=0.9)
    demo_boss.take_damage(200)      # 触发激怒
    demo_boss.boss_attack(dummy)
    print(dummy)
