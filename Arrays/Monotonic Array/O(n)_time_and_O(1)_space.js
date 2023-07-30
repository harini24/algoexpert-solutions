function isMonotonic(array) {
  // Write your code here.
  let nonIncreasing = true;
  let nonDecreasing = true;
  for (let i = 0; i < array.length - 1; i++) {
    if (array[i] < array[i + 1]) nonIncreasing = false;
    if (array[i] > array[i + 1]) nonDecreasing = false;
  }

  return nonDecreasing || nonIncreasing;
}

// Do not edit the line below.
exports.isMonotonic = isMonotonic;
