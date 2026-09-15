# Byoung Hartzel L. Kim     9 - Beryllium
# used objectImplemetation.py as a reference/template
class BasketballPlayer:
    def __init__(self, last_name, jersey_num, can_shoot, three_pt_percent):
        # public
        self.last_name = last_name
        self.jersey_num = jersey_num
        self.can_shoot = can_shoot
        # private
        self.__three_pt_percent = three_pt_percent
 
    def shoot(self, made):
        if made:
            self.__three_pt_percent = self.__three_pt_percent + 2
 
    def get_stats(self):
        return self.last_name + " #" + str(self.jersey_num) + " - 3PT: " + str(self.__three_pt_percent) + "%"
 
    def pass_ball(self, teammate):
        print(self.last_name + " passes to " + teammate)

# basketballteam and basketballplayer is both seperated
class BasketballTeam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []  # holds actual BasketballPlayer objects, not just names
 
    def add_player(self, player):
        if len(self.players) < 6:
            self.players.append(player)
        else:
            print(self.team_name + " roster is full")
 
    def list_players(self):
        for player in self.players:
            print(player.get_stats())


# creates one team and 6 players
warriors = BasketballTeam("Warriors")

player1 = BasketballPlayer("Curry", 30, True, 42)
player2 = BasketballPlayer("Thompson", 11, True, 40)
player3 = BasketballPlayer("Green", 23, False, 20)
player4 = BasketballPlayer("Wiggins", 22, True, 38)
player5 = BasketballPlayer("Looney", 5, False, 0)
player6 = BasketballPlayer("Poole", 3, True, 35)

# before
print("BEFORE RELATIONSHIP")
print(warriors.team_name + " has " + str(len(warriors.players)) + " players")

print("BUILDING RELATIONSHIP")
warriors.add_player(player1)
warriors.add_player(player2)
warriors.add_player(player3)
warriors.add_player(player4)
warriors.add_player(player5)
warriors.add_player(player6)

# after
print("AFTER RELATIONSHIP")
print(warriors.team_name + " has " + str(len(warriors.players)) + " players")
print("Related object(s):")
warriors.list_players()