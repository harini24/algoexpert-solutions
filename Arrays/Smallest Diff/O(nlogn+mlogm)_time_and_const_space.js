function smallestDifference(arrayOne, arrayTwo) {
  // Write your code here.
  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);
  let ind1 = 0;
  let ind2 = 0;
  let currentDiff = Infinity;
  let smallestDiff = Infinity;
  let pair = [];

  console.log(arrayOne, arrayTwo);
  while (ind1 < arrayOne.length && ind2 < arrayTwo.length) {
    let num1 = arrayOne[ind1];
    let num2 = arrayTwo[ind2];

    if (num1 < num2) {
      currentDiff = num2 - num1;
      ind1++;
    } else if (num1 > num2) {
      currentDiff = num1 - num2;
      ind2++;
    } else {
      return [num1, num2];
    }

    if (currentDiff < smallestDiff) {
      smallestDiff = currentDiff;
      pair = [num1, num2];
    }
  }

  return pair;
}

// Do not edit the line below.
exports.smallestDifference = smallestDifference;
