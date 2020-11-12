def test(team, team_size):
    diff_from_theory_best_team = 0
    # 0     1                  2      3           4
    # Open, conscientiousness, extro, agreeable, neuroticism
    personality_perfect = {
        "openness": 7,
        "conscientiousness": 9,
        "extroversion": 5,
        "agreeableness": 7,
        "neuroticism": 1
    }

    # 0        1          2          3        4         5                    6
    # central, self rely, hard work, leisure, morality, delay gratification, wasted time
    work_ethic_perfect = {
        "centrality of work": 2.5,
        "self reliance": 1.5,
        "hard work": 4,
        "leisure": 4,
        "morality": 2.5,
        "delay of gratification": 3,
        "wasted time": 2.5
    }

    # USE KEY, LIKE FOR KEY IN PERSON.PERSONALITY.KEYS TO GRAB ALL VALUES FOR EACH PERSON2

    for key in team[0].personality:
        diff_from_theory_best_team += abs(personality_perfect[key] - mean(team, key, None, team_size))

    for key in team[0].work_ethic:
        diff_from_theory_best_team += abs(work_ethic_perfect[key] - mean(team, None, key, team_size))

    return diff_from_theory_best_team


def mean(team, p_trait, w_trait, team_size):
    if w_trait is None:
        # Calculating mean of Personality Trait
        value = 0
        for person in team:
            value += person.personality[p_trait]
        return value / team_size
    else:
        # Calculating mean of Work Ethic Trait
        value = 0
        for person in team:
            value += person.work_ethic[w_trait]
        return value / team_size
