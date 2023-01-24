function runLengthEncoding(string) {
  // Write your code here.
  ret = [];
  count = 0;
  word = string[0];
  for (let char of string) {
    if (count === 9 || char !== word) {
      ret.push(count.toString());
      ret.push(word);
      word = char;
      count = 0;
    }
    count += 1;
  }
  ret.push(count.toString());
  ret.push(word);

  return ret.join("");
}
