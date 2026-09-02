# 此文件夹用于设计简单的文字版回合制游戏，游戏参考崩坏星穹铁道的设定
# 定义 Character_role 基类：血量、攻击力、防御力、速度、普攻和战技方法
class Character_role:
    def __init__(self, name, hp, atk, defen, speed):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defen = defen
        self.speed = speed
# 在另一文件中定义 Character_role 的子类：角色类
class Character(Character_role):
    def __init__(self, name, hp, atk, defen, speed, skill):
        super().__init__(name, hp, atk, defen, speed)
        self.skill = skill

    
