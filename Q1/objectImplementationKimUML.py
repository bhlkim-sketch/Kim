# for the class if basketball player 

# Byoung Hartzel L. Kim   9 - Beryllium
class BasketballPlayer:
    # for the object blueprint
    def __init__(self, last_name, jersey_num, can_dribble, can_shoot, two_pt_percent, three_pt_percent, ingame_iq):
        self.last_name = last_name
        self.jersey_num = jersey_num
        self.can_dribble = can_dribble
        self.can_shoot = can_shoot

        self.__two_pt_percent = two_pt_percent
        self.__three_pt_percent = three_pt_percent
        self.__ingame_iq = ingame_iq
    # for the shots, if he can shoot or not
    def shoot(self, shot_type):
        if not self.can_shoot:
            print(self.last_name + " can't shoot yet")
            return

        if shot_type == "2pt":
            self.__two_pt_percent += 2
        elif shot_type == "3pt":
            self.__three_pt_percent += 2
    # stats of shots
    def get_shooting_stats(self):
        return self.last_name + " #" + str(self.jersey_num) + " - 2PT: " + str(self.__two_pt_percent) + "% 3PT: " + str(self.__three_pt_percent) + "%"
    # if their passing is good
    def pass_ball(self, teammate_name):
        print(self.last_name + " passes the ball to " + teammate_name)
    # if their defense is good
    def play_defense(self):
        print(self.last_name + " plays defense")

# objects shown at the images
object1 = BasketballPlayer("Curry", 30, True, True, 50, 42, 95)
object2 = BasketballPlayer("Green", 23, True, False, 45, 20, 90)

print("--- BEFORE ---")
print("Object 1:", object1.get_shooting_stats())
print("Object 2:", object2.get_shooting_stats())

print("Performing action on Object 1...")
object1.shoot("3pt")
object1.shoot("3pt")
object1.pass_ball("Thompson")

print("--- AFTER ---")
print("Object 1:", object1.get_shooting_stats())
print("Object 2:", object2.get_shooting_stats())
