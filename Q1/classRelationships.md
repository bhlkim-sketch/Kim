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
![Class Relationship Diagram](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/Images/classRelationshipDiagram.png)

## 𝘗𝘺𝘵𝘩𝘰𝘯 𝘐𝘮𝘱𝘭𝘦𝘮𝘦𝘯𝘵𝘢𝘵𝘪𝘰𝘯
[View Python Source](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/classRelationships.py)

## 𝘛𝘦𝘴𝘵 𝘙𝘶𝘯
![Relationship Test Run](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/Images/Relationshiptestrun.png)

## 𝘖𝘣𝘫𝘦𝘤𝘵 𝘙𝘦𝘭𝘢𝘵𝘪𝘰𝘯𝘴𝘩𝘪𝘱 𝘋𝘪𝘢𝘨𝘳𝘢𝘮
![Object Relationship Diagram](https://github.com/bhlkim-sketch/Kim/blob/main/Q1/Images/objectRelationshipDiagram.png)

## 𝘈𝘯𝘢𝘭𝘺𝘴𝘪𝘴
### What is the association between your two classes?
- They are both important in the sport. The team needs players and the players need a team. 
### What multiplicity did you choose and why?
- 1 : 6 because in each team, there is at least 5 players and 1 bench player.
### How did you implement the relationship in Python?
- The players attribute inside BasketballTeam is a list. The add_player() method appends a BasketballPlayer object to that list, and list_players() loops through self.players and calls get_stats() on each one to prove they're real objects.
### Why did you store an object reference instead of copying its data?
- If I had only stored player.last_name as a string inside the team, the team would have no way to reach the player's other data.
### If your relationship uses many, why is a list appropriate?
- A list is appropriate because a team doesn't have just one player, it has several, and the number can vary.
