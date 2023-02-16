function firstDuplicateValue(array) {
  // Write your code here.
  for (let val of array) {
    let absValue = Math.abs(val);
    if (array[absValue - 1] < 0) return absValue;
    array[absValue - 1] *= -1;
  }

  return -1;
}
