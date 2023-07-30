function minimumWaitingTime(queries) {
  // Write your code here.
  queries.sort((a, b) => a - b);
  minWaitingTime = 0;
  for (let i = 0; i < queries.length; i++) {
    let currentValue = queries[i];
    let remainingQueries = queries.length - i - 1;
    minWaitingTime += currentValue * remainingQueries;
  }
  return minWaitingTime;
}

function minimumWaitingTime(queries) {
  // Write your code here.
  queries.sort((a, b) => a - b);
  let currentSum = 0;
  let previousSum = 0;
  for (let query of queries) {
    currentSum += previousSum;
    previousSum += query;
  }
  return currentSum;
}
