// O(n*m) time and space
// n - number of words
// m - length of longest word in word

function semordnilap(words) {
  // Write your code here.
  const wordsSet = new Set(words);
  const semordnilaps = [];

  for (let word of words) {
    const reversed = word.split("").reverse().join("");
    console.log(word, reversed, wordsSet, wordsSet.has(reversed));
    if (wordsSet.has(reversed)) {
      console.log(word, wordsSet);
      semordnilaps.push([word, reversed]);
      wordsSet.delete(word);
      wordsSet.delete(reversed);
    }
  }
  return semordnilaps;
}
