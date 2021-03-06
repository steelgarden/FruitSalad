class Fruit:
    fireDamage=0
    damage=0
    coin=True
    immuneFire=False
    def name(self):
        return self.__class__.__name__
    def details(self):
        return "%s: cost=%d damage=%d fireDamage=%d getsCoins=%s immuneFire=%s"%(self.name(), self.cost, self.damage, self.fireDamage, self.coin, self.immuneFire)
    
class BlueBerry(Fruit):
    cost=2
    damage=1

class DragonFruit(Fruit):
    cost=4
    fireDamage=5
    coin=False

class Apple(Fruit):
    cost=5
    damage=4

class Banana(Fruit):
    cost=5
    damage=3
    immuneFire=True

allFruits=[BlueBerry, DragonFruit, Apple, Banana]
    
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
    def addStress(self, amount):
        self.stress+=amount
        if self.stress >= 3:
            self.quarterHearts-=self.stress//3
            self.stress=0
    def chooseFruit(self):
        print(self.name+": it's your turn to choose a fruit!")
        
        for id,fruit in enumerate(self.fruits):
            print(id,fruit.details())
        print('Which fruit do you want to use? ', end='')
        response=input()
        id=int(response)
        self.currentFruit=self.fruits[id]
        print('You have chosen to use '+self.currentFruit.name()+'!')
    
    def action(self):
        for id,player in enumerate(allPlayers):
            print(id,player.name)
        print(self.name+': which player do you want to target with your '+self.currentFruit.name()+'? ', end='')
        response=input()
        id=int(response)
        target=allPlayers[id]
        print('You have chosen to target '+target.name+'!')
        if target.currentFruit.immuneFire:
            damageDone=self.currentFruit.damage
        else:
            damageDone=max(self.currentFruit.damage, self.currentFruit.fireDamage)
        target.quarterHearts -= damageDone
        if self.currentFruit.coin:
            print('How many coins do you want to take (max %d)? '%damageDone, end='')
            response=input()
            try:
                coinsTaken=int(response)
            except:
                print("I don't get it, no coins for you!")
                coinsTaken=0
            if coinsTaken<0 or coinsTaken>damageDone:
                print("Out of bounds, no coins for you!")
                coinsTaken=0
        else:
            coinsTaken=0
        self.coins+=coinsTaken
        self.quarterHearts+=(damageDone-coinsTaken)
        self.addStress(1)
        self.status()
        target.status()

        for id,fruit in enumerate(allFruits):
            print(id,fruit().details())
        print(len(allFruits), "nothing")
        print ("What fruit do you want to buy? ", end='')
        buyInput=input()
        try:
            buyIndex=int(buyInput)
        except:
            buyIndex=-1
        if 0 <= buyIndex < len(allFruits) and allFruits[buyIndex].cost<=self.coins:
            self.fruits.append(allFruits[buyIndex]())
            self.coins -= allFruits[buyIndex].cost
            
p1=Player('Ian')
p2=Player('Ben')
allPlayers=[p1, p2]

while True:
    for p in allPlayers:
        p.chooseFruit()
    for p in allPlayers:
        p.action()
    allPlayers.append(allPlayers.pop(0))
    
        
        
