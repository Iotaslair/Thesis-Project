import pims
import itertools

people = []
for i in range(4):
    people.append(pims.make_person())

teams = itertools.combinations(people, 3)
best_team = []
best_team_score = 0
for team in teams:
    if (test(team) > best_team_score):
        best_team_score = test(team)
        best_team = team

print("Most Compatible Team: " + str(best_team))
print("Score of best team: " + best_team_score)

