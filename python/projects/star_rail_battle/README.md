# 星穹铁道回合制战斗

## 项目简介

文字版一对一回合制战斗：角色可选择普攻或战技，Boss 血量低于阈值会进入激怒状态并追加攻击。战斗有 100 回合上限，超时判平局，保证必然收敛。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `units.py` | `Character_role` 基类与 `Character` 子类（`name/max_hp/hp/atk/defense/speed`） |
| `skill.py` | 战技类：`DamageDealer` / `DPS`（爆发伤害，冷却 2 回合）、`Healer`（治疗） |
| `boss.py` | `Boss` 类：怒气/激怒机制与 `boss_attack(target)` 追加攻击 |
| `battle.py` | `battle(player, boss, max_turns=100, seed=None) -> {"winner", "turns", "log"}` |
| `main.py` | 入口：用固定随机种子组装并运行一场完整战斗 |

`battle()` 除打印过程外还返回结构化结果，便于测试与复用；全程无 `time.sleep()`。

## 运行命令

```bash
python python/projects/star_rail_battle/main.py
python python/projects/star_rail_battle/battle.py
python python/projects/star_rail_battle/skill.py
```

均无需输入（stdin），固定随机种子，不会在仓库内产生新文件。

## 学到什么

- 用继承组织战斗单位，公共行为放在基类、战技放在子类
- 战斗流程返回结构化结果（胜者/回合数/日志），而不是只 print
- 给循环加回合上限，避免“双方都打不死”的死循环
