def test_mean(team, team_size):
    diff_from_theory_best_team = 0

    personality_perfect = {
        "openness": 7,
        "conscientiousness": 9,
        "extroversion": 5,
        "agreeableness": 7,
        "neuroticism": 1
    }

    work_ethic_perfect = {
        "centrality of work": 2.5,
        "self reliance": 1.5,
        "hard work": 4,
        "leisure": 4,
        "morality": 2.5,
        "delay of gratification": 3,
        "wasted time": 2.5
    }
    # Goes through each key in personality, gets the mean for this specific team and subtracts it from the perfect
    # value for that trait
    for key in team[0].personality:
        diff_from_theory_best_team += abs(personality_perfect[key] - mean(team, key, None, team_size))
    # Same as above with work ethic
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


# Idea for this test is to have it where there is a ton of if statements that check if teams have these certain things
# Like 1 Extrovert and 1 introvert
def test_rules(team):
    tests_failed = 0
    # Tests that 20-40% extroverts are on this team
    # Came from: Composition, Process, and Performance in Self-Managed Groups: The Role of Personality
    extro_count = 0
    intro_count = 0
    for person in team:
        if person.personality["extroversion"] > 5:
            extro_count += 1
        if person.personality["extroversion"] <= 5:
            intro_count += 1
    # This line tests that the value is between .2 and .4
    if .2 <= extro_count / (intro_count + extro_count) <= .4:
        pass
    else:
        tests_failed += 1

    # Tests that everyone is high in Conscientiousness
    # Really limits my possibilities for teams
    # Came from: Conscientiousness and Performance of Sales Representatives: Test of the
    # Mediating Effects of Goal Setting
    # and The Big Five Personality Dimensions and Job Performance: A Meta-Analysis
    for person in team:
        if person.personality["conscientiousness"] < 6:
            tests_failed += 1
            break
        else:
            pass

    # Tests that people have low Neuroticism
    # Came from: The Big Five Personality Dimensions and Job Performance: A Meta-Analysis
    for person in team:
        if person.personality["neuroticism"] < 4:
            tests_failed += 1
            break
        else:
            pass

    # Tests that people have low self reliance
    # Came from: What Makes A Great Software Engineer?
    # With wanting SEs to Ask for help
    for person in team:
        if person.work_ethic["self reliance"] <= 3:
            tests_failed += 1
            break
        else:
            pass

    return tests_failed
