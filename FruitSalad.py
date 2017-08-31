class BlueBerry:
    cost=2
    fireDamage=0
    damage=1
    coin=True
    immuneFire=False

class DragonFruit:
    cost=4
    fireDamage=5
    damage=0
    coin=False
    immuneFire=False

class Apple:
    cost=5
    fireDamage=0
    damage=4
    coin=True
    immuneFire=False

class Banana:
    cost=5
    fireDamage=0
    damage=3
    coin=True
    immuneFire=True

def fruitName(f):
    return f.__class__.__name__
    
class Player:
    def __init__(self, name):
        self.quarterHearts = 40
        self.coins=0
        self.fruits=[BlueBerry()]
        self.name=name
        self.stress=0
    def status(self):
        print('Current status for '+self.name)
        print('Hearts = ',self.quarterHearts/4)
        print('Coins = ',self.coins)
        print('Stress = ',self.stress)
    def chooseFruit(self):
        print(self.name+": it's your turn to choose a fruit!")
        
        for id,fruit in enumerate(self.fruits):
            print(id,fruitName(fruit))
        print('Which fruit do you want to use? ', end='')
        response=input()
        id=int(response)
        self.currentFruit=self.fruits[id]
        print('You have chosen to use '+fruitName(self.currentFruit)+'!')
    
    def action(self):
        for id,player in enumerate(allPlayers):
            print(id,player.name)
        print(self.name+': which player do you want to target with your '+fruitName(self.currentFruit)+'? ', end='')
        response=input()
        id=int(response)
        target=allPlayers[id]
        print('You have chosen to target '+target.name+'!')
        target.quarterHearts = target.quarterHearts-1
        print('Do you want to gain a coin (c) or a quarter heart (h)? ',end='')
        response=input()
        if response=='c':
            self.coins=self.coins+1
        elif response=='h':
            self.quarterHearts+=1
        else:
            print("haha, you can't type so you don't get anything!!!")
        self.stress+=1
        if self.stress==3:
            self.quarterHearts-=1
            self.stress=0
        self.status()
        target.status()
        print()
        
p1=Player('Ian')
p2=Player('Ben')
allPlayers=[p1, p2]

while True:
    for p in allPlayers:
        p.chooseFruit()
    for p in allPlayers:
        p.action()
    allPlayers.append(allPlayers.pop(0))
    
        
        
