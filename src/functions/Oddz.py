team1_vote = []
team2_vote = []
check = 0
i = 0

while check == 0:
    team1_vote.append(int(input("team1")))
    if team1_vote[-1] == 0:
        team1_vote.pop(-1)
        check = 1
    i += 1
        
i = 0

while check == 1:
    team2_vote.append(int(input("team2")))
    if team2_vote[-1] == 0:
        team2_vote.pop(-1)
        check = 2
    i += 1
    
team1_after = team1_vote.copy()
team2_after = team2_vote.copy()
    
team1_len = len(team1_vote)
team2_len = len(team2_vote)
    
team1_sum = sum(team1_vote)
team2_sum = sum(team2_vote)

LEN = team1_len + team2_len
SUM = team1_sum + team2_sum

team1_ratio = 1 / (team1_len / LEN)
team2_ratio = 1 / (team2_len / LEN)
    

winner = int(input("winner"))

if winner == 1:
    for i in range(team1_len):
        team1_after[i] = int(team1_after[i] * team1_ratio)
        print("team1_after -> " + str(team1_after[i]))
    for i in range(team2_len):
        team2_after[i] = 0
        print("team2_after -> " + str(team2_after[i]))

if winner == 2:
    for i in range(team1_len):
        team1_after[i] = 0
        print("team1_after -> " + str(team1_after[i]))
    for i in range(team2_len):
        team2_after[i] = int(team2_after[i] * team2_ratio)
        print("team2_after -> " + str(team2_after[i]))

print("team1_sum -> " + str(team1_sum))
print("team2_sum -> " + str(team2_sum))
print("team1_len -> " + str(team1_len))
print("team2_len -> " + str(team2_len))
print("team1_rat -> " + str(team1_ratio))
print("team2_rat -> " + str(team2_ratio))
