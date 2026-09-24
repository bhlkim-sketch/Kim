# Advanced Class Relationships

## Previous Activities
[(classAttributes)](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/classAttributesMethods.md)
[(classRelationships)](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/classRelationships.md)

## Existing System Description:
My system is about basketball. In Part III I had the class **Sport** and a related class **BasketballTeam**. One team has 6 players (multiplicity 1 : 6).

The problem: the general information (sport name, name, age) and the basketball-only information (jersey number, position, points) were all mixed together. Also, the team only had a simple association with its players. It did not show that the players can still exist without the team.

In this activity I fixed this by using **inheritance** (BasketballPlayer IS-A Sport) and **aggregation** (BasketballTeam HAS-A BasketballPlayer).

## Inheritance Relationship
Parent: `Sport`
Child: `BasketballPlayer`
Explanation: A BasketballPlayer is a kind of Sport player. It already has a sport name, a name, and an age from `Sport`. The child only adds the things that are special to basketball: `jersey_number`, `position`, and `points`. It uses `super().__init__()` so I do not have to write the parent's code again.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: **Aggregation** (weak HAS-A), multiplicity 1 : 6
Explanation: The team does not make its own players. The players are created first, and then added to the team with `add_player()`. If the team is deleted, the players still exist. That is why it is aggregation and not composition. The team can only have 6 players, so the 7th player is rejected.

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:

**1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.**
I chose `BasketballPlayer` as the child of `Sport`. A basketball player is a more specific kind of sport player. Every basketball player has a sport name, a name, and an age, and those are already in `Sport`. So the child only needs to add the basketball parts like jersey number and position.

**2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.**
`BasketballPlayer` did not have to write `sport_name`, `name`, and `age` again. It gets them by calling `super().__init__()`. It also reuses the `show_info()` and `train()` methods from `Sport`. If I make another child class, like `VolleyballPlayer`, it can reuse the same code too.

**3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.**
It is aggregation because the team does not create the players. The players are made first and then added to the team using `add_player()`. In my test, I deleted the team and the player `p1` still worked. This means the players can live without the team, so it is a weak HAS-A.

**4. What is the difference between Association from Part III and the advanced relationship you implemented?**
Association only shows that two classes are connected, like a team and its players. Aggregation and inheritance tell us more. Inheritance says one class is a type of another class and shares its code. Aggregation says the team holds players that can still exist by themselves.

**5. How does your design follow the DRY principle?**
DRY means "Don't Repeat Yourself." I put the shared information in one class, `Sport`, so I did not copy it into `BasketballPlayer`. The team code for adding and showing players is only written once in `BasketballTeam`. If I need to change something general, I only change it in one place.
