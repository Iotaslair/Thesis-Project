import pims
import itertools

people = []
for i in range(4):
    people.append(pims.make_person())

teams = itertools.combinations(people, 3)

