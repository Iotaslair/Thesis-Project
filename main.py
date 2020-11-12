import pims
import itertools
import tester

number_of_people_to_create = 5
team_size = 3

people = []

for i in range(number_of_people_to_create):
    people.append(pims.make_person())

teams = itertools.combinations(people, team_size)

best_team_dict = {}

for team in teams:
    score = tester.test(team, team_size)
    best_team_dict[score] = team

# Get out all scores, sort them, then use the best scores from the dict to print the teams
# This is used to get the best teams
scores = []
for score in best_team_dict:
    scores.append(score)
scores = sorted(scores)

print("A lower score is better because it is considered to be closer to the perfect team")
print("A score of 0 is considered to be the perfect team")
for i in range(3):
    print("Team # " + str(i + 1))
    team_string = ""
    for person in best_team_dict[scores[i]]:
        team_string += str(person) + "\n"
    print("Score: " + str(scores[i]))
    print(team_string)
