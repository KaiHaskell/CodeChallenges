// The Code tab has a code which attempts to add a clone of an array to itself.
// There is no error message, but the results are not as expected. Can you fix the code?

let basicArray = [1, 2, 3];

function clone(arr) {
  let arr2 = [...arr];
  arr.push(arr2);
  return arr;
}

clone(basicArray);
