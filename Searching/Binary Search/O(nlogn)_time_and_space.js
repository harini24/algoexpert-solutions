function binarySearch(array, target) {
  // Write your code here.
  return findEle(array, 0, array.length - 1, target);
}

const findEle = (array, start, end, target) => {
  if (start > end) return -1;
  const middleInd = Math.floor((end + start) / 2);
  if (array[middleInd] === target) return middleInd;
  else if (array[middleInd] > target)
    return findEle(array, 0, middleInd - 1, target);
  else return findEle(array, middleInd + 1, end, target);
};
