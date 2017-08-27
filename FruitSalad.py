class Player:
    def __init__(self, name):
        self.quarterHearts = 40
        self.coins=0
        self.fruits=['blueberry']
        self.name=name
    def status(self):
        print('Current status for '+self.name)
        print('Hearts = ',self.quarterHearts/4)
        print('Coins = ',self.coins)
    def action(self):
        print(self.name+": it's your turn!")
        
        for id,name in enumerate(self.fruits):
            print(id,name)
        print('Which fruit do you want to use? ', end='')
        response=input()
        id=int(response)
        print('You have chosen to use '+self.fruits[id]+'!')
        for id,player in enumerate(allPlayers):
            print(id,player.name)
        print('Which player do you want to target? ', end='')
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
        self.status()
        target.status()
        print()
        
p1=Player('Ian')
p2=Player('Ben')
allPlayers=[p1, p2]

while True:
    for p in allPlayers:
        p.action()
        
        
