function classPhotos(redShirtHeights, blueShirtHeights) {
  // Write your code here.
  redShirtHeights.sort((a, b) => a - b);
  blueShirtHeights.sort((a, b) => a - b);
  const topRow = redShirtHeights[0] > blueShirtHeights[0] ? "RED" : "BLUE";
  for (let i = 0; i < redShirtHeights.length; i++) {
    const redStudent = redShirtHeights[i];
    const blueStudent = blueShirtHeights[i];
    if (topRow === "RED" && blueStudent >= redStudent) return false;
    if (topRow === "BLUE" && blueStudent <= redStudent) return false;
  }
  return true;
}
