function sortedSquaredArray(array) {
    // Write your code here.
    const sortedSquares = new Array(array.length).fill(0)
    for (let ind=0;ind<array.length; ind++){
      sortedSquares[ind] = array[ind] * array[ind]
    }
    sortedSquares.sort((a,b)=>a-b)
    return sortedSquares;
  }