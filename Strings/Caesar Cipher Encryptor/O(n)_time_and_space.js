function caesarCipherEncryptor(string, key) {
  // Write your code here.
  let newLetters = [];
  key %= 26;
  for (let char of string) {
    newLetters.push(getNewLetter(char, key));
  }
  return newLetters.join("");
}

function getNewLetter(letter, key) {
  let newLetterCode = letter.charCodeAt() + key;
  return newLetterCode <= 122
    ? String.fromCharCode(newLetterCode)
    : String.fromCharCode(96 + newLetterCode);
}
