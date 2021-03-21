teams = ['Germany', 'Ukraine']
scores = [-4, 0]


def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        x = teams[0]
    elif scores[0] == scores[1]:
        return "At match " + teams[0] + " - " + teams[1] + ", teams played draw."
    else:
        x = teams[1]
    return "At match " + teams[0] + " - " + teams[1] + ", " + x + " won!"
    # return f"At match {teams[0]} - {teams[1]}, {'teams played draw.' if scores[0] == scores[1] else teams[scores.index(max(scores))] + ' won!'}"

print(uefa_euro_2016(teams, scores))
