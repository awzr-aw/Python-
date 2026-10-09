# 功能：回合制战斗流程，battle(player, boss) 返回结构化战斗结果供程序与测试调用。
import random


def battle(player, boss, max_turns=100, seed=None, verbose=True):
    """执行一场一对一回合制战斗，返回结构化结果。

    - 玩家回合随机选择普攻/战技，战技冷却时自动改为普攻
    - 回合上限 max_turns（默认 100），超时双方均存活则判平局，避免死循环
    - 返回 {"winner": 胜者名称（平局为 "平局"）, "turns": 实际回合数, "log": [战斗文字日志]}
    """
    if seed is not None:
        random.seed(seed)   # 固定随机种子，保证战斗过程可复现

    log = []

    def say(message):
        """同时记录日志并按需打印"""
        log.append(message)
        if verbose:
            print(message)

    say("========== 战斗开始 ==========")
    say(f"{player}  VS  {boss}")
    say("-------------------------------")

    turn = 0
    while turn < max_turns and player.is_alive() and boss.is_alive():
        turn += 1
        say(f"\n--- 第 {turn} 回合 ---")
        say(f"当前状态：{player}")
        say(f"Boss状态：{boss}")

        # 玩家回合（演示用随机选择，实际可改为输入）
        action = random.choice(["attack", "skill"])
        if action == "skill":
            if not player.use_skill(boss):
                say(f"{player.name} 改为普通攻击")
                player.attack(boss)
        else:
            player.attack(boss)

        # 检查 Boss 是否死亡
        if not boss.is_alive():
            say(f"\n{boss.name} 被击败！{player.name} 获胜！")
            break

        # Boss 回合（模拟 AI）
        say(f"\n{player.name} 状态：{player}")
        say(f"{boss.name} 状态：{boss}")
        boss.boss_attack(player)

        # 检查玩家是否死亡
        if not player.is_alive():
            say(f"\n{player.name} 被击败！{boss.name} 获胜！")
            break

        player.end_turn()   # 回合结束清理（减少技能冷却）

    if player.is_alive() and boss.is_alive():
        winner = "平局"
        say(f"\n已达到回合上限 {max_turns} 回合，双方均存活，判定为平局。")
    elif player.is_alive():
        winner = player.name
    else:
        winner = boss.name

    say("========== 战斗结束 ==========")
    return {"winner": winner, "turns": turn, "log": log}


if __name__ == "__main__":
    # 演示：固定随机种子，保证每次运行结果一致且必然收敛
    import sys

    sys.dont_write_bytecode = True   # 不落盘缓存

    from units import Character
    from boss import Boss
    from skill import DamageDealer

    player = DamageDealer("三月七·输出", hp=800, atk=120, defense=20, speed=110, skill_multiplier=2.2)
    boss = Boss("可可利亚（模拟）", hp=1200, atk=90, defense=15, speed=80, rage_threshold=0.25)

    result = battle(player, boss, seed=42)
    print(f"\n战斗结果：胜者={result['winner']}，回合数={result['turns']}，日志条数={len(result['log'])}")

    # 平局保护验证：双方都打不动对方时，靠回合上限收敛而不是死循环
    wall_a = Character("铁壁A", hp=1000, atk=1, defense=9999, speed=10)
    wall_b = Boss("铁壁Boss", hp=1000, atk=1, defense=9999, speed=10)
    draw_result = battle(wall_a, wall_b, max_turns=5, seed=1, verbose=False)
    print(f"平局保护验证：胜者={draw_result['winner']}，回合数={draw_result['turns']}")
