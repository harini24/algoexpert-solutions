function twoNumberSum(array, targetSum) {
  // Write your code here.
  let nums = {};
  for (let i of array) {
    if (targetSum - i in nums) {
      return [i, targetSum - i];
    } else {
      nums[i] = true;
    }
  }
  return [];
}
