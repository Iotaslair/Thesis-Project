import pims
import itertools
number_of_people_to_create = 5
team_size = 3

people = []

for i in range(number_of_people_to_create):
    people.append(pims.make_person())

teams = itertools.combinations(people, team_size)

best_team = []
best_team_score = 0
for team in teams:
    if (test(team) > best_team_score):
        best_team_score = test(team)
        best_team = team

print("Most Compatible Team: " + str(best_team))
print("Score of best team: " + best_team_score)

