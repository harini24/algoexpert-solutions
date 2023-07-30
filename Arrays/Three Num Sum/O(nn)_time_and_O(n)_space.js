function threeNumberSum(array, targetSum) {
  // Write your code here.
  array.sort((a, b) => a - b);
  let triplets = [];
  for (let ind = 0; ind < array.length; ind++) {
    let remainingSum = targetSum - array[ind];
    let left = ind + 1;
    let right = array.length - 1;
    while (left < right) {
      if (array[left] + array[right] == remainingSum) {
        triplets.push([array[ind], array[left], array[right]]);
        left += 1;
        right -= 1;
      } else if (array[left] + array[right] > remainingSum) right -= 1;
      else left += 1;
    }
  }
  return triplets;
}

// Do not edit the line below.
exports.threeNumberSum = threeNumberSum;
