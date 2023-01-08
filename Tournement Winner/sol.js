// O(n) time and O(k) space 
// n - number of competitions
// k - number of teams

function tournamentWinner(competitions, results) {
    // Write your code here.
    let currentBestTeam = ''
    const scores={[currentBestTeam]:0}
    for (let ind = 0;ind<competitions.length;ind++){
      let winner = results[ind]
      const [homeTeam, awayTeam] = competitions[ind]
      let winningTeam = winner === 1 ? homeTeam : awayTeam;
  
      updateScores(scores,3,winningTeam)
  
      if (scores[currentBestTeam] < scores[winningTeam]) currentBestTeam = winningTeam
      
    }
    return currentBestTeam;
  }
  
  const updateScores = (scores, points, team) => {
    if (!(team in scores)) scores[team]=0
    scores[team]+=points
  }