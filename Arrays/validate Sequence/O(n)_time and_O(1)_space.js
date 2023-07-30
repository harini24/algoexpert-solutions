function isValidSubsequence(array, sequence) {
  // Write your code here.
  let seqInd = 0;
  for (let i of array) {
    if (seqInd === sequence.length) break;
    if (i === sequence[seqInd]) seqInd++;
  }
  return seqInd === sequence.length;
}

function isValidSubsequence1(array, sequence) {
    // Write your code here.
    let arrInd=0
    let seqInd=0
    while(arrInd < array.length && seqInd < sequence.length){
      if (array[arrInd] === sequence[seqInd]) seqInd++;
      arrInd++;
    }
    return seqInd===sequence.length
  }