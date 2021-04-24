def test_mean(team, team_size):
    diff_from_theory_best_team = 0

    personality_perfect = {
        "openness": 8,
        "conscientiousness": 9,
        "extroversion": 5,
        "agreeableness": 8,
        "neuroticism": 1
    }

    work_ethic_perfect = {
        "centrality of work": 4,
        "self reliance": 3.5,
        "hard work": 4,
        "leisure": 4,
        "morality": 3.5,
        "delay of gratification": 4,
        "wasted time": 4
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
    # and Personality and Team Performance: A Meta-Analysis
    for person in team:
        if person.personality["conscientiousness"] < 6:
            tests_failed += 1
            break
        else:
            pass

    # Tests that people have low Neuroticism
    # Came from: The Big Five Personality Dimensions and Job Performance: A Meta-Analysis
    # Actually goes against The Big Five Personality Dimensions and Job Performance: A Meta-Analysis
    for person in team:
        if person.personality["neuroticism"] < 4:
            tests_failed += 1
            break
        else:
            pass

    # Tests that people have low self reliance
    # Came from: What Makes A Great Software Engineer?
    # With wanting SEs to Ask for help

    # Interviews with SEs said that having high self reliance
    # is a good thing but not to the point that they don't ask for help

    for person in team:
        if person.work_ethic["self reliance"] >= 3 && person.work_ethic["self reliance"] < 5:
            tests_failed += 1
            break
        else:
            pass

    # Write a test that makes sure there is high agreeableness and everyone has agreeableness above a certain amount
    # Came from: Personality and Team Performance: A Meta-Analysis
    # So having everyone be high is a good thing
    # Also want to make a test to test the average conscientiousness score is high as well based on the same paper


    return tests_failed
