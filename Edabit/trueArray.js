function countTrue(arr) {
  // if the array is empty, return 0
  if (arr.length == 0) {
    return 0;
  }
  //filter through the array, removing false values
  let trueArray = arr.filter((isTrue) => isTrue === true);
  //return the new array's length, which should be == to the number of true
  return trueArray.length;
}
