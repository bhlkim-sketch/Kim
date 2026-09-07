# Class Attributes and Methods
Byoung Hartzel L. Kim       9 - Beryllium

## Previous Design
```text
| Link to my previous activity: |
```
+ https://github.com/bhlkim-sketch/Kim/blob/main/Q1/BerylliumSportsKIM.md

## Design Revision
```text
| Changes from my previous design: |
+ Renamed the class from the general "Sports" to BasketballPlayer, since all of the properties I created only describes one player, not the sport as a whole.
+ Combined the "Shoot form" pseudocode into a real method called shoot() that updates the player's shooting percentage instead of leaving it as a separate parameter block.
+ Kept the same overall context and all seven original properties and four original methods, just renamed a few for clearer Python syntax.
```

## Visibility Decisions
```text
Attribute	        Data Type	        Visibility	        Reason
last_name	        string	            Public	            Needed for only display and identification (scoreboards, rosters), doesn't need protection at all
jersey_num	        int	                Public	            Also just identification info, already safe to read/set directly
two_pt_percent	    int                	Private	            Should only change through the shoot() method's logic, not be set to any random value from outside that just messes up the code
three_pt_percent	int	                Private	            Shooting stats should only update through valid gameplay actions and stats
```

## Updated UML Class Diagram
+ Text version:
```text
+--------------------------------------------+
|              BasketballPlayer               |
+--------------------------------------------+
| + last_name : string                        |
| + jersey_num : int                          |
| + can_dribble : boolean                     |
| + can_shoot : boolean                       |
| - two_pt_percent : int                      |
| - three_pt_percent : int                    |
| - ingame_iq : int                            |
+--------------------------------------------+
| + shoot(shot_type : string)                  |
| + get_shooting_stats()                       |
| + pass_ball(teammate_name : string)          |
| + play_defense()                             |
+--------------------------------------------+
```
+ Image version link: https://github.com/bhlkim-sketch/Kim/blob/main/Q1/Images/classDiagramUML.png
+ Object diagram link: https://github.com/bhlkim-sketch/Kim/blob/main/Q1/Images/objectDiagramUML.png
+ Object implementation Python code link: https://github.com/bhlkim-sketch/Kim/blob/main/Q1/objectImplementationKimUML.py
+ Proof of creating Class diagram: https://github.com/bhlkim-sketch/Kim/blob/main/Q1/Images/proofUML.png
+ Texting of python code: https://github.com/bhlkim-sketch/Kim/blob/main/Q1/Images/UMLOOPpart2Proof.png

## Analysis
```text
1. Why did you make your chosen attribute private?

+ I made three_pt_percent and two_pt_percent private because a shooting percentage cannot be changed by another random number outside shooting. If this was public, a part of the code could accidentally set it to something like 150% or a negative number, which makes no sense for a stat at all.

2. Which method changes the state of your object?

+ The shoot() method changes the state of the object. Depending on the shot_type parameter passed in, it increases either the private two_pt_percent or three_pt_percent attribute by a small amount, simulating the player getting slightly better after taking shots.

3. How did your two objects demonstrate that instances are independent?

+ In my test run, I only called object1.shoot("3pt") twice. Object 1's three_pt_percent went from 42% to 46%, but Object 2's stats stayed exactly the same the whole time. This shows that even though both objects came from the same BasketballPlayer class, each one stores its own separate copy of the attributes.

What is the difference between your class diagram and your object diagram?

+ The class diagram shows the blueprint. It lists the attribute names and their data types without any actual values, because it describes every possible BasketballPlayer in general. The object diagram shows two specific instances, object1 and object2, with their real, current values, because it's showing the actual state of those objects after Step 7.
```
