// O(n+m) time and O(c) space
// n - number of characters
// m - length of document
// c - number of unique chars in characters

function generateDocument(characters, document) {
  // Write your code here.
  const charCounts = {};

  for (let char of characters) {
    if (!(char in charCounts)) {
      charCounts[char] = 0;
    }
    charCounts[char]++;
  }

  console.log(charCounts);
  for (let char of document) {
    if (!(char in charCounts) || charCounts[char] === 0) return false;
    charCounts[char]--;
  }

  return true;
}
