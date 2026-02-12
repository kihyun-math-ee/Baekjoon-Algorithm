from random import *

# Normal unit
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} unit is created.")

    def move(self, location):
        print(f"[Ground unit move]")
        print(f"{self.name} : move in direction to {location}. [speed {self.speed}]")

    def damaged(self, damage):
        # FIX 1: Changed {self.damage} to {damage} (argument)
        print(f"{self.name} : got damaged {damage}.")
        self.hp -= damage
        print(f"{self.name} : current Hp is {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} : is destroyed.")   

# Attackunit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : attack in direction to {location}. [Damage {self.damage}]")

# Marine
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    # Stimpack : move speed and attack speed boost up, self hp 10 decrease
    def Stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : uses stimpack. (hp 10 decrease)")
        else:
            print(f"{self.name} : hp is not enough to use stimpack.")

# Tank
class Tank(AttackUnit):
    # Seize mode : fix tank at ground, higher damage, not movable.
    seize_developed = False # whether Seize developed

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # not Seize mode -> seize mode
        if self.seize_mode == False:
            print(f"{self.name} : changes to seize mode.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f"{self.name} : releases seize mode.")
            self.damage //= 2
            self.seize_mode = False

# Dropship : Air unit, transport aircraft. able to transport Marine / Firebat / Tank. no attack

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : fly in direction to {location}. [speed {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # pretends ground speed == 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False # Clocking mode (released)

    # FIX 2: Un-indented this method (it was inside __init__)
    def clocking(self):
        if self.clocked == True: # Clocking mode -> release Clocking mode
            print(f"{self.name} : releases clocking mode.")
            self.clocked = False
        else: # released Clocking mode -> Clocking mode
            print(f"{self.name} : sets clocking mode.")
            self.clocked = True

def game_start():
    print("[Alert] new game starts.")

def game_over():
    print("Player : gg") # good game
    print("[Player] leaves the game")

# ------------------------------------------------------------
# Game Execution
# ------------------------------------------------------------
game_start()

# creates 3 units of marine 
m1 = Marine()
m2 = Marine()
m3 = Marine()

# creates 2 units of tank
t1 = Tank()
t2 = Tank()

#creates 1 unit of wraith
w1 = Wraith()

# Unit batch processing ()
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# all units move
print("\n[Move Units]")
for unit in attack_units:
    unit.move("1 O`clock")

# Tank seize mode developed
Tank.seize_developed = True
print("\n[Alert] tank seize mode development is complete.")

# ready on attack mode (Marine : stimpack, Tank : seize mode, Wraith : clocking)
print("\n[Activate Skills]")
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.Stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# all units attack
print("\n[Attack]")
for unit in attack_units:
    unit.attack("1 O`clock")

# all units damaged
print("\n[Battle Result]")
for unit in attack_units:
    unit.damaged(randint(5, 20)) # damaged in random (5 ~ 19)

# game over
game_over()