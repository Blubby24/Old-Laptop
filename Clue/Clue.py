import random

class game:
    def __init__(self, playerCount):
        self.suspects = ['Mrs. White', 'Mrs. Peacock', 'Professor Plum', 'Colonel Mustard', 'Miss Scarlett', 'Reverend Green', 'Mr. Boddy']
        self.rooms = ['Ballroom', 'Billiard Room', 'Conservatory', 'Dining Room', 'Hall', 'Kitchen','Lounge', 'Library', 'Study']
        self.weapons = ['Knife', 'Revolver', 'Rope', 'Wrench', 'Candlestick', 'Lead pipe']
        self.answer = {'Suspect': self.suspects.pop(random.randrange(0,len(self.suspects))), 'Weapon': self.weapons.pop(random.randrange(0,len(self.weapons))), 'Room': self.rooms.pop(random.randrange(0,len(self.rooms)))}
        self.playerCount = playerCount
        self.playerList = []

    def getGuess(self, room):
        Guess = {}
        W = ''
        for w in self.weapons:
            W += w + ' '
        print(W)
        print('What weapon?')
        weapon = input()
        S = ''
        for s in self.suspects:
            S += s + ' '
        print(S)
        print('Who did it?')
        criminal = input()
        Guess = {'Suspect': criminal, 'Weapon': weapon, 'Room': room}
        print('Is this your guess? y/n')
        print(Guess)
        if not input() == 'y':
            self.getGuess(room)
        return Guess

    def checkGuess(self, guess):
        if guess['Suspect'] == self.answer['Suspect'] and guess['Room'] == self.answer['Room'] and guess['Weapon'] == self.answer['Weapon']:
            print('You win')
            return True
        print('You lose')
        return False
   
    def SetNoteBooks(self):
        ClueNum = len(self.weapons) + len(self.suspects) + len(self.rooms)
        remander = ClueNum % self.playerCount
        clues = [self.suspects, self.weapons, self.rooms]
        faceUp = []
        noSus = False
        noWep = False
        noR = False
        playerNotebooks = []
        for i in range(remander):
            faceUp.append(clues[random.randrange(0, 3)].pop(random.randrange(0,len(clues[random.randrange(0, 3)]))))
            print('Popped ' + faceUp[i])
        for i in range(self.playerCount):
            notebook = []
            for j in range(int((ClueNum-remander)/self.playerCount)):
                if self.weapons == [] and noWep == False:
                    clues.pop(clues.index([]))
                    noWep = True
                if self.suspects == [] and noSus == False:
                    clues.pop(clues.index([]))
                    noSus = True
                if self.rooms == [] and noR == False:
                    clues.pop(clues.index([]))
                    noR = True
                whichlist = random.randrange(0, len(clues))
                notebook.append(clues[whichlist].pop(random.randrange(0,len(clues[whichlist]))))
            playerNotebooks.append(notebook)
        return playerNotebooks

    def takeTurn(self, player):
        print('What room do you want to see?')
        R = ''
        for r in self.rooms:
            R += r + ' '
        print(R)
        room = input()
        player.room = room
        print('What player do you want to ask?')
        playerNumber = int(input())
        guess = self.getGuess(room)
        checked = []
        total = 0
        if guess['Suspect'] in self.playerList[playerNumber].notebook:
            checked.append(guess['Suspect'])
            total += 1
        if guess['Weapon'] in self.playerList[playerNumber].notebook:
            checked.append(guess['Weapon'])
            total += 1
        if guess['Room'] in self.playerList[playerNumber].notebook:
            checked.append(guess['Room'])
            total += 1
        if total > 0:
            return checked[random.randrange(0, total)]
        else:
            print('They do not have any')
       
    def YouWantToBall(self, player):
        print('Do you want to make a Guess y/n')
        if input() == 'y':
            return self.checkGuess(self.getGuess(player.room))
        return 1 
               

class Player():
    def __init__(self, game, num, notebook):
        self.PlayerNumber = num
        self.game = game
        self.room = ''
        self.notebook = notebook

players = []
playerCount = 0
print('How many players')
playerCount = int(input())
Clue = game(playerCount)
Sus = Clue.suspects.copy()
Wep = Clue.weapons.copy()
Rooms = Clue.rooms.copy()
Notebooks = Clue.SetNoteBooks()
for i in range(playerCount):
    players.append(Player(Clue, i, Notebooks[i]))
    print(players[i].notebook)
Clue.playerList = players
Clue.suspects = Sus
Clue.weapons = Wep
Clue.rooms = Rooms
print(Clue.answer)
popped = -1
while True:
    p = 0
    for i in range(len(Clue.playerList)):
        if not popped == -1:
            if popped > len(Clue.playerList):
                popped = 0
            i = popped
            popped = -1
           
        print('Your turn player ' + str(Clue.playerList[i].PlayerNumber))
        print(Clue.takeTurn(Clue.playerList[i]))
        ballOrNot = Clue.YouWantToBall(Clue.playerList[i])
        if  ballOrNot == True:
            print('You win player ' + str(Clue.playerList[i].PlayerNumber))
            break
        if ballOrNot == False:
            p = Clue.playerList[i].PlayerNumber
            break 
    Clue.playerList.pop(p)
    popped = p


#Clue.checkGuess(Clue.getGuess())