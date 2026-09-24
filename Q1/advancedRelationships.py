# Byoung Hartzel L. Kim            9 - Beryllium

# the parent class
class Sport:
    def __init__(self, sport_name, name, age):
        self.sport_name = sport_name
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name}, {self.age} years old, plays {self.sport_name}")

    def train(self):
        print(f"{self.name} is training for {self.sport_name}.")


# the child class
class BasketballPlayer(Sport):
    def __init__(self, name, age, jersey_number, position):
        super().__init__("Basketball", name, age)   # use the parent's __init__
        self.jersey_number = jersey_number
        self.position = position
        self.points = 0

    def score_points(self, amount):
        self.points += amount
        print(f"{self.name} scored {amount} points.")


# team class
class BasketballTeam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []            # the team does NOT create the players

    def add_player(self, player):
        if len(self.players) < 6:    # 1 team : 6 players
            self.players.append(player)
            print(f"{player.name} joined {self.team_name}.")
        else:
            print(f"Team is full! {player.name} cannot join.")

    def show_players(self):
        print(f"Players of {self.team_name}:")
        for player in self.players:
            print(f"  #{player.jersey_number} {player.name} - {player.position}")


# main run
if __name__ == "__main__":
    # players are created first
    p1 = BasketballPlayer("Marco Reyes", 15, 7, "Point Guard")
    p2 = BasketballPlayer("Jun Santos", 15, 11, "Shooting Guard")
    p3 = BasketballPlayer("Paolo Cruz", 16, 23, "Small Forward")
    p4 = BasketballPlayer("Ken Dizon", 15, 5, "Power Forward")
    p5 = BasketballPlayer("Rico Lim", 16, 30, "Center")
    p6 = BasketballPlayer("Gio Tan", 15, 9, "Guard")
    p7 = BasketballPlayer("Leo Ramos", 16, 14, "Forward")

    team = BasketballTeam("Naga Warriors")

    print("=== TEST 1: INHERITANCE ===")
    print("sport_name from Sport:", p1.sport_name)
    print("name from Sport:", p1.name)
    p1.show_info() # method from Sport
    p1.train() # method from Sport
    p1.score_points(12) # method from BasketballPlayer

    print()
    print("=== TEST 2: AGGREGATION (1 team : 6 players) ===")
    team.add_player(p1)
    team.add_player(p2)
    team.add_player(p3)
    team.add_player(p4)
    team.add_player(p5)
    team.add_player(p6)
    team.add_player(p7) # 7th player, should be rejected
    print()
    team.show_players()

    print()
    print("=== TEST 3: PLAYER STILL EXISTS WITHOUT THE TEAM ===")
    del team
    print("Team deleted. The player is still here:")
    p1.show_info()
