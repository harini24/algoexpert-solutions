// Time - O(n) best O(n*n) avg and worst
// space - O(1)

function bubbleSort(array) {
  // Write your code here.
  let isSorted = false;
  while (!isSorted) {
    isSorted = true;
    for (let i = 0; i < array.length; i++) {
      if (array[i] > array[i + 1]) {
        temp = array[i + 1];
        array[i + 1] = array[i];
        array[i] = temp;
        isSorted = false;
      }
    }
  }
  return array;
}
