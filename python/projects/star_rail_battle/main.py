# 功能：星穹铁道风格一对一回合制战斗主程序，组装角色与 Boss 并调用 battle 流程。
import random
import sys

# 运行时不生成 __pycache__，避免在项目目录落盘缓存文件
sys.dont_write_bytecode = True

from boss import Boss
from skill import DamageDealer
from battle import battle

# 固定随机种子，保证战斗过程可复现；回合上限兜底，保证必然收敛
RANDOM_SEED = 42
MAX_TURNS = 100


def build_units():
    """创建本场战斗的玩家与 Boss，返回 (player, boss)"""
    player = DamageDealer("三月七·输出", hp=800, atk=120, defense=20, speed=110, skill_multiplier=2.2)
    boss = Boss("可可利亚（模拟）", hp=1200, atk=90, defense=15, speed=80, rage_threshold=0.25)
    return player, boss


def main():
    """运行一场完整战斗并打印结果摘要，返回结构化战斗结果"""
    random.seed(RANDOM_SEED)
    player, boss = build_units()

    result = battle(player, boss, max_turns=MAX_TURNS)

    print("\n========== 战斗结果 ==========")
    print(f"胜者：{result['winner']}")
    print(f"总回合数：{result['turns']}")
    print(f"战斗日志条数：{len(result['log'])}")
    return result


if __name__ == "__main__":
    main()
