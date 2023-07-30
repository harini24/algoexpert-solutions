function arrayOfProducts(array) {
  // Write your code here.
  let post = 1;
  let pre = 1;
  let ret = new Array(array.length).fill(1);

  for (let i = 0; i < array.length; i++) {
    ret[i] = ret[i] * pre;
    pre = pre * array[i];
    ret[array.length - i - 1] = ret[array.length - i - 1] * post;
    post = post * array[array.length - i - 1];
  }
  return ret;
}
