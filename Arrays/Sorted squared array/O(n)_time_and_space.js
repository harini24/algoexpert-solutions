function sortedSquaredArray(array) {
    // Write your code here.
    const sortedSquares = new Array(array.length).fill(0)
    let smallerInd = 0 
    let largerInd= array.length-1
    for (let ind=array.length-1;ind>=0; ind--){
      let smallerVal=array[smallerInd]
      let largerVal= array [largerInd]
      if (Math.abs(smallerVal)>Math.abs(largerVal)){
        sortedSquares[ind] = smallerVal * smallerVal
        smallerInd++
      }else{
        sortedSquares[ind] = largerVal * largerVal
        largerInd--
      }
    }
    return sortedSquares;
  }