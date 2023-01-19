def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_3_scores = []

    scores.sort()
    top_3_scores = len(scores[0])

    return top_3_scores

def sort_high_to_low(scores):
    scores.sort()
    scores.reverse()
    return scores