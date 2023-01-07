function twoNumberSum(array, targetSum) {
  // Write your code here.
  array.sort((a, b) => a - b);
  let left = 0;
  let right = array.length - 1;
  while (left < right) {
    const leftVal = array[left];
    const rightVal = array[right];
    if (leftVal + rightVal === targetSum) {
      return [leftVal, rightVal];
    } else if (leftVal + rightVal < targetSum) {
      left++;
    } else {
      right--;
    }
  }
  return [];
}
