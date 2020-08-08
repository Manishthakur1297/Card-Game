import random

class Game:
    # Intialize Cards and Players
    def __init__(self, n):
        self.size = n
        self.card_names = {1: "A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}
        self.card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
        self.card_quantity = dict()
        self.players = [["_" for i in range(3)] for j in range(n)]

    # Distribute cards to players
    def distributeCards(self):
        for i in range(self.size):
            for j in range(3):
                self.players[i][j] = self.findUniqueCard()

    # Find Unique Random Card
    def findUniqueCard(self):
        value = random.randint(1,13)
        card_name = self.card_names[value]
        if card_name in self.card_quantity:
            if self.card_quantity[card_name] < 4:
                self.card_quantity[card_name] += 1
            else:
                self.findUniqueCard()
        else:
            self.card_quantity[card_name] = 1
        return card_name

    # Print Players Cards
    def printCards(self):
        for i,player in enumerate(self.players):
            print("Player",i+1,":",player)

    # Condition 1 -> 3 cards of the same number like 3,3,3
    def condition1(self,player):
        if len(set(player))==1:
            return True
        return False

    # Condition 2 -> Numbers in order like 4,5,6
    def condition2(self,player):
        player = sorted([self.card_values[i] for i in player])
        if player[0]+1==player[1] and player[1]+1==player[2]:
            return True
        return False

    # Condition 3 -> Pair of Cards like two Kings or two 10s
    def condition3(self, player):
        player = sorted([self.card_values[i] for i in player])
        if player[0] == player[1] or player[1] == player[2]:
            return True
        return False

    # Condition 4 -> Maximum Sum of All 3 cards Win
    def condition4(self, players):
        sm = []
        for i,player in enumerate(players):
            tmp = 0
            for j in player:
                tmp+=self.card_values[j]
            sm.append(tmp)
        print("\n=====Players Card Sum =====")
        print(sm)
        mx = max(sm)
        if sm.count(mx)==1:
            return sm.index(mx)
        else:
            filter_players = [i for i in range(len(sm)) if sm[i] == mx]
            return self.tieWinner(filter_players)

    # Winner Function -> Check Each condition One by One
    def winner(self):
        tmp = [0]*self.size
        tmp_count = {}
        for i,v in enumerate(self.players):
            if self.condition1(v):
                tmp[i] = 1
                if '1' not in tmp_count:
                    tmp_count['1'] = 1
                else:
                    tmp_count['1'] += 1
            elif self.condition2(v):
                tmp[i] = 2
                if '2' not in tmp_count:
                    tmp_count['2'] = 1
                else:
                    tmp_count['2'] += 1

            elif self.condition3(v):
                tmp[i] = 3
                if '3' not in tmp_count:
                    tmp_count['3'] = 1
                else:
                    tmp_count['3'] += 1
        if sum(tmp)==0:
            return self.condition4(self.players)
        else:
            if '1' in tmp_count:
                if tmp_count['1']>1:
                    filter_players = [i for i in range(len(tmp)) if tmp[i] == 1]
                    return self.tieWinner(filter_players)
                else:
                    return tmp.index(1)
            elif '2' in tmp_count:
                if tmp_count['2']>1:
                    filter_players = [i for i in range(len(tmp)) if tmp[i] == 2]
                    return self.tieWinner(filter_players)
                else:
                    return tmp.index(2)
            elif '3' in tmp_count:
                if tmp_count['3'] > 1:
                    filter_players = [i for i in range(len(tmp)) if tmp[i] == 3]
                    return self.tieWinner(filter_players)
                else:
                    return tmp.index(3)

    # Tie Winner -> Draws New Cards till Winner declared
    def tieWinner(self, players):
        print("\n===== Tie Condition =======\n")
        print("=== Players Tie Indexes ====")
        print(players)
        arr = [0] * len(players)
        mx = -1
        for i in range(len(players)):
            card_name = self.findUniqueCard()
            card_value = self.card_values[card_name]
            if card_name=='A':
                arr[i] = 14
            else:
                arr[i] = card_value
            if mx<arr[i]:
                mx = arr[i]
        print("\n==== New Cards Drawn for Each Tie Player ====");
        print(arr)
        count = arr.count(mx)
        if count==1:
            return players[arr.index(mx)]
        else:
            filter_players = [players[i] for i in range(len(players)) if arr[i] == mx]
            return self.tieWinner(filter_players)

# Game Object
if __name__ == '__main__':
    card = Game(4)
    card.distributeCards()
    card.printCards()
    print("\nPlayer",card.winner()+1,"Wins!!")






