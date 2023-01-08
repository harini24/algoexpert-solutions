// O(nlogn) time and O(1) space

function nonConstructibleChange(coins) {
  // Write your code here.
  coins.sort((a, b) => a - b);
  let minConstructibleChange = 0;
  for (let coin of coins) {
    if (coin > minConstructibleChange + 1) break;
    minConstructibleChange += coin;
  }
  return minConstructibleChange + 1;
}
