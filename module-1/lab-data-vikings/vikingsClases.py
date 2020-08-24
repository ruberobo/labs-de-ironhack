
# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack (self):
        return self.strength

    def receiveDamage(self,x):
        self.health = self.health -x

# Viking


class Viking (Soldier):
    def __init__ (self, name,health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self,x):
        self.health = self.health-x
        if self.health>0:
            return f'{self.name} has received {x} points of damage'
        else:
            return f'{self.name} has died in act of combat'


    def battleCry(self):
        return f'Odin Owns You All!'

# Saxon

class Saxon(Soldier):
    def receiveDamage(self,x):
        self.health = self.health-x
        if self.health>0:
            return f'A Saxon has received {x} points of damage'
        else:
            return f'A Saxon has died in combat'
    

# War


class War():

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,V):
        self.vikingArmy.append(V)

    def addSaxon(self,S):
        self.saxonArmy.append(S)

    def vikingAttack(self):
        a = random.choice(self.saxonArmy)
        v=(random.choice(self.vikingArmy))
        b = a.receiveDamage(v.strength)

        if a.health<=0:
            self.saxonArmy.remove(a)

        return b

    def saxonAttack(self):
        c = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)
        d = c.receiveDamage(s.strength)

        if c.health<=0:
            self.vikingArmy.remove(c)

        return d


    def showStatus(self):

        if len(self.saxonArmy)==0:
            return f'Vikings have won the war of the century!'
        if len(self.vikingArmy)==0:
            return f'Saxons have fought for their lives and survive another day...'
        if len(self.saxonArmy)!=0 and len(self.vikingArmy)!=0:
            return f'Vikings and Saxons are still in the thick of battle.'
