//Create a function that takes two strings
// and returns true if the first string ends with the second string;
// otherwise return false.

function checkEnding(str1, str2) {
  //get the length of string2,
  //then slice that amount off of string1 and compare.
  let twoLength = str2.length;

  let matchingString = str1.slice(-twoLength);

  if (matchingString == str2) {
    return true;
  }
  return false;
}
