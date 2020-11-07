# code to be saved for https://bigfive-test.com/
# 5fa416aec969250008c6b464
# https://bigfive-test.com/result/5fa416aec969250008c6b464

# The name of this file is a shortened version of
# Person In My Study generator
import random
import names


class Person:
    def __init__(self):
        self.name = names.get_full_name()

        self.personality = {
            "openness": 0,
            "conscientiousness": 0,
            "extroversion": 0,
            "agreeableness": 0,
            "neuroticism": 0
        }

        self.work_ethic = {
            "centrality of work": 0,
            "self reliance": 0,
            "hard work": 0,
            "leisure": 0,
            "morality": 0,
            "delay of gratification": 0,
            "wasted time": 0
        }

    def __str__(self):
        return "Name: " + str(self.name) + "\n" + \
               "Personality: " + str(self.personality) + "\n" + \
               "Work Ethic: " + str(self.work_ethic)


def make_person():
    x = Person()
    for trait in x.personality.keys():
        x.personality[trait] = random.randint(0, 10)
    for trait in x.work_ethic.keys():
        x.work_ethic[trait] = random.randint(0, 5)
    return x
