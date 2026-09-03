# 此文件用于设计关卡
# 最小战斗参考：输出角色 vs Boss
# 仅演示核心机制，不涉及复杂技能、状态、速度等，你可以在此基础上扩充

import random
import time

# ---------- 角色基类（可复用） ----------
class Character:
    """所有战斗单位的基类"""
    def __init__(self, name, hp, atk, defense):
        self.name = name          # 名称
        self.max_hp = hp          # 最大生命值
        self.hp = hp              # 当前生命值
        self.atk = atk            # 攻击力
        self.defense = defense    # 防御力（减伤系数，这里用固定减伤数值）

    def is_alive(self):
        """是否存活"""
        return self.hp > 0

    def take_damage(self, damage):
        """受到伤害，减去防御力，但至少造成1点伤害"""
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        return actual_damage

    def attack(self, target):
        """普通攻击，伤害 = 攻击力 + 随机波动（-2~+2）"""
        base_damage = self.atk + random.randint(-2, 2)
        damage = max(1, base_damage)   # 至少1点
        actual = target.take_damage(damage)
        print(f"{self.name} 对 {target.name} 发动普通攻击，造成 {actual} 点伤害")
        return actual

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"


# ---------- 输出型角色（继承自Character） ----------
class DamageDealer(Character):
    """输出位，额外拥有一个爆发技能"""
    def __init__(self, name, hp, atk, defense, skill_multiplier=1.8):
        super().__init__(name, hp, atk, defense)
        self.skill_multiplier = skill_multiplier   # 技能倍率
        self.skill_cooldown = 0                    # 技能冷却回合数（0表示可用）

    def use_skill(self, target):
        """爆发技能：造成攻击力 * 倍率 的伤害，冷却2回合"""
        if self.skill_cooldown > 0:
            print(f"{self.name} 的技能还在冷却中（剩余{self.skill_cooldown}回合）")
            return False   # 技能未释放成功

        damage = int(self.atk * self.skill_multiplier) + random.randint(-3, 3)
        damage = max(1, damage)
        actual = target.take_damage(damage)
        print(f"{self.name} 释放爆发技能，对 {target.name} 造成 {actual} 点伤害！")
        self.skill_cooldown = 2   # 进入冷却
        return True

    def end_turn(self):
        """每回合结束时调用，减少冷却"""
        if self.skill_cooldown > 0:
            self.skill_cooldown -= 1

    # 重写攻击方法，可以增加一点特色（可选），这里保持一样


# ---------- Boss类 ----------
class Boss(Character):
    """Boss，拥有更强的血量和攻击，可能带有特殊技能（此处只放一个激怒）"""
    def __init__(self, name, hp, atk, defense, rage_threshold=0.3):
        super().__init__(name, hp, atk, defense)
        self.rage_threshold = rage_threshold   # 血量低于此比例时进入激怒状态
        self.is_raged = False

    def take_damage(self, damage):
        """重写受伤方法，检测血量触发激怒"""
        actual = super().take_damage(damage)
        # 检查是否进入激怒状态
        if not self.is_raged and self.hp / self.max_hp <= self.rage_threshold:
            self.is_raged = True
            print(f"⚠️ {self.name} 被激怒了！攻击力提升！")
            self.atk = int(self.atk * 1.5)   # 攻击力提升50%
        return actual

    def boss_attack(self, target):
        """Boss的普通攻击，若激怒则额外附带一次追加攻击"""
        print(f"{self.name} 发动攻击！")
        self.attack(target)   # 普通攻击
        if self.is_raged:
            print(f"{self.name} 因激怒追加一次攻击！")
            self.attack(target)   # 额外攻击


# ---------- 战斗流程函数 ----------
def battle(player, boss):
    """执行一场回合制战斗，返回胜者"""
    print("========== 战斗开始 ==========")
    print(f"{player}  VS  {boss}")
    print("-------------------------------")

    turn = 1
    while player.is_alive() and boss.is_alive():
        print(f"\n--- 第 {turn} 回合 ---")
        # 玩家回合
        print(f"当前状态：{player}")
        print(f"Boss状态：{boss}")
        # 玩家选择行动（这里为了演示简单，用随机选择，实际你可以改为输入）
        action = random.choice(["attack", "skill"])
        if action == "attack":
            player.attack(boss)
        else:  # skill
            success = player.use_skill(boss)
            if not success:
                # 如果技能冷却，则自动改为普通攻击
                print(f"{player.name} 改为普通攻击")
                player.attack(boss)

        # 检查Boss是否死亡
        if not boss.is_alive():
            print(f"\n🎉 {boss.name} 被击败！{player.name} 获胜！")
            break

        # Boss回合（模拟AI）
        print(f"\n{player.name} 状态：{player}")
        print(f"{boss.name} 状态：{boss}")
        boss.boss_attack(player)

        # 检查玩家是否死亡
        if not player.is_alive():
            print(f"\n💀 {player.name} 被击败！{boss.name} 获胜！")
            break

        # 回合结束清理（冷却减少）
        player.end_turn()
        turn += 1
        time.sleep(0.5)   # 让战斗有节奏感

    print("========== 战斗结束 ==========")


# ---------- 主程序 ----------
if __name__ == "__main__":
    # 创建角色：输出位（名字、HP、攻击、防御、技能倍率）
    my_player = DamageDealer("三月七·输出", hp=800, atk=120, defense=20, skill_multiplier=2.2)

    # 创建Boss
    boss_enemy = Boss("可可利亚（模拟）", hp=1200, atk=90, defense=15, rage_threshold=0.25)

    # 开始战斗
    battle(my_player, boss_enemy)