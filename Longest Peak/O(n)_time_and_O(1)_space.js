function longestPeak(array) {
  // Write your code here. ans=0
  let i = 1;
  let ans = 0;
  while (i < array.length - 1) {
    let isPeak = array[i] > array[i - 1] && array[i] > array[i + 1];
    if (!isPeak) {
      i++;
      continue;
    }
    let left = i - 2;
    let right = i + 2;
    while (left >= 0 && array[left] < array[left + 1]) left -= 1;
    while (right < array.length && array[right] < array[right - 1]) right += 1;

    currLength = right - left - 1;
    if (currLength > ans) ans = currLength;

    i = right;
  }
  return ans;
}
