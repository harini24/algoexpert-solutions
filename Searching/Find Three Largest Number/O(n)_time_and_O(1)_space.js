function findThreeLargestNumbers(array) {
    // Write your code here.
    let maxxx = -Infinity
    let maxx = -Infinity
    let max = -Infinity
  
    for (let val of array){
      if(val>maxxx){
        max=maxx
        maxx=maxxx
        maxxx=val
      } else if(val>maxx){
        max=maxx
        maxx=val
      } else if(val>max){
        max=val
      }
    }
    return [max,maxx,maxxx]
  }