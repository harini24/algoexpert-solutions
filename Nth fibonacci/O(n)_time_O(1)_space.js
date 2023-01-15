function getNthFib(n) {
  // Write your code here.
  let lastVal = 0;
  let secondLastVal = 1;
  for (let i = 2; i <= n; i++) {
    let temp = lastVal + secondLastVal;
    secondLastVal = lastVal;
    lastVal = temp;
  }
  return lastVal;
}

// Do not edit the line below.
exports.getNthFib = getNthFib;
