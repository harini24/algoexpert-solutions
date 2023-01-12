function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
  // Write your code here.
  redShirtSpeeds.sort((a, b) => a - b);
  fastest
    ? blueShirtSpeeds.sort((a, b) => b - a)
    : blueShirtSpeeds.sort((a, b) => a - b);
  let sum = 0;
  for (let i = 0; i < blueShirtSpeeds.length; i++) {
    sum +=
      blueShirtSpeeds[i] > redShirtSpeeds[i]
        ? blueShirtSpeeds[i]
        : redShirtSpeeds[i];
  }
  return sum;
}
