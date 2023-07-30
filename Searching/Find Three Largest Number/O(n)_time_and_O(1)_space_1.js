function findThreeLargestNumbers(array) {
    // Write your code here.
    let ret=[null,null,null]
    for (let val of array)
      updateLargest(ret,val)
    return ret
  }
  
  function updateLargest(ret,val){
    if (!ret[2] || val>ret[2]){
      shiftAndUpdate(ret,val,2)
    }else  if (!ret[1] || val>ret[1]){
      shiftAndUpdate(ret,val,1)
    } else  if (!ret[0] || val>ret[0]){
      shiftAndUpdate(ret,val,0)
    }
  }
  
  function shiftAndUpdate(ret,val,ind){
    for (let i=0;i<ind+1;i++){
      if(ind==i){
        ret[i]=val
      }else{
        ret[i]=ret[i+1]
      }
    }
  }
  