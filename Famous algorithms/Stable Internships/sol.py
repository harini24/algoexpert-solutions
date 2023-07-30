# O(n^2) time and space
def stableInternships(interns, teams):
    # Write your code here.
    unmached = list(range(len(interns)))
    teamsPref = [{intern:ind for ind,intern in enumerate(team)} for team in teams]

    pref = [0]*len(interns)
    pairs={}

    while unmached:
        intern = unmached.pop()
        team = interns[intern][pref[intern]]
        pref[intern]+=1

        if team not in pairs:
            pairs[team] = intern
        else:
            if teamsPref[team][intern]<teamsPref[team][pairs[team]]:
                unmached.append(pairs[team])
                pairs[team] = intern
            else:
                unmached.append(intern)
    return [[y,x] for x,y in pairs.items()]