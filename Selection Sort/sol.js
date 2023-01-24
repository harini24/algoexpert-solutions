// O(n*n) time and O(1) space

function selectionSort(array) {
  // Write your code here.
  let startInd = 0;
  while (startInd < array.length) {
    let minInd = startInd;
    for (let i = startInd + 1; i < array.length; i++) {
      if (array[i] < array[minInd]) {
        minInd = i;
      }
    }

    const temp = array[minInd];
    array[minInd] = array[startInd];
    array[startInd] = temp;

    startInd++;
  }
  return array;
}
