# O(n) time and O(k) space 
# n - number of competitions
# k - number of teams

def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam=""
    scores = {currentBestTeam:0}
    for ind,competition in enumerate(competitions):
        winner = results[ind]
        homeTeam,awayTeam = competition
        winningTeam = homeTeam if winner==1 else awayTeam
        updateScores(scores,3,winningTeam)
        if scores[currentBestTeam] < scores[winningTeam]:
            currentBestTeam=winningTeam
        print(scores)
    return currentBestTeam

def updateScores(scores,val,team):
    if team not in scores:
        scores[team]=0
    scores[team]+=val