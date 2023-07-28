function firstNonRepeatingCharacter(string) {
  // Write your code here.
  charCount = {};
  for (let char of string) {
    if (!(char in charCount)) charCount[char] = 0;
    charCount[char]++;
  }

  for (let ind = 0; ind < string.length; ind++) {
    const char = string[ind];
    if (charCount[char] == 1) return ind;
  }

  return -1;
}
