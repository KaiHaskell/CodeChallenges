// Implement functionality to reverse an input string. Print out the reversed string.
// For example, given a string "cool", print out the string "looc".
// You may use whatever programming language you'd like.
// Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

//take a string as an input
const reverseString = (str) => {
  //split the string land return it as a new array
  let splitString = str.split("");
  // take the split string and .reverse it
  let reverseArr = splitString.reverse();
  // join the reversed array
  let reverseStr = reverseArr.join(" ");

  return reverseStr;
};

const str = "Hello world!";

console.log(reverseString(str));
