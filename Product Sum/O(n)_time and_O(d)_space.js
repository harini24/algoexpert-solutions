function productSum(array, depth = 1) {
  // Write your code here.
  const sum = array.reduce((acc, e) => {
    if (Array.isArray(e)) return acc + productSum(e, depth + 1);
    return acc + e;
  }, 0);
  return sum * depth;
}
