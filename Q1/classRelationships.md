# 𝘾𝙡𝙖𝙨𝙨 𝙍𝙚𝙡𝙖𝙩𝙞𝙤𝙣𝙨𝙝𝙞𝙥𝙨: 𝘼𝙨𝙨𝙤𝙘𝙞𝙖𝙩𝙞𝙤𝙣 𝙖𝙣𝙙 𝙈𝙪𝙡𝙩𝙞𝙥𝙡𝙞𝙘𝙞𝙩𝙮
## 𝘗𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘞𝘰𝘳𝘬
[OOP Act 1](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/BerylliumSportsKIM.md)
[OOP Act 2](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/classAttributesMethods.md)

## 𝘌𝘹𝘪𝘴𝘵𝘪𝘯𝘨 𝘊𝘭𝘢𝘴𝘴
```text
Class: Basketball Player
Description: My original class was Sports, and I picked Basketball. While creating OOP Act 2,
I remembered that Basketball is played by players, so I added BasketballPlayer as a new class.
A Basketball player has many data (like 2pt Shooting % or 3pt Shooting %) and also has many methods (like Shooting or Dribbling).
```

## 𝘕𝘦𝘸 𝘙𝘦𝘭𝘢𝘵𝘦𝘥 𝘊𝘭𝘢𝘴𝘴
```text
Class: Basketball Team
Description: I've decided to add BasketballTeam as a new class because it is related to BasketballPlayer.
Without a basketball team, how would a Basketball game go?
In a BasketballTeam, you could add up to 6 players, the 5 players as starters and the remaining 1 is a bench warmer.
```

## 𝘈𝘴𝘴𝘰𝘤𝘪𝘢𝘵𝘪𝘰𝘯
```text
Relationship: Team to players
Explanation: Basketball is played by 5 players, each on a team. Teams are important in the game because many people play
the game and there is only 2 Basketball rims in a team.
There must be a way to make the 10 players play together, competitively but still grouped together.
```

## 𝘔𝘶𝘭𝘵𝘪𝘱𝘭𝘪𝘤𝘪𝘵𝘺
```text
Multiplicity: 1 : 6
Explanation: Every 1 BasketballTeam, there are 6 players.
```

## 𝘜𝘔𝘓 𝘊𝘭𝘢𝘴𝘴 𝘙𝘦𝘭𝘢𝘵𝘪𝘰𝘯𝘴𝘩𝘪𝘱 𝘋𝘪𝘢𝘨𝘳𝘢𝘮
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## 𝘗𝘺𝘵𝘩𝘰𝘯 𝘐𝘮𝘱𝘭𝘦𝘮𝘦𝘯𝘵𝘢𝘵𝘪𝘰𝘯
[View Python Source](classRelationships.py)

## 𝘛𝘦𝘴𝘵 𝘙𝘶𝘯
![Relationship Test Run](images/relationshipTestRun.png)

## 𝘖𝘣𝘫𝘦𝘤𝘵 𝘙𝘦𝘭𝘢𝘵𝘪𝘰𝘯𝘴𝘩𝘪𝘱 𝘋𝘪𝘢𝘨𝘳𝘢𝘮
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## 𝘈𝘯𝘢𝘭𝘺𝘴𝘪𝘴
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
