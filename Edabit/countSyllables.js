function numberSyllables(word) {
  //split the word based on the hyphen count
  let syllableArray = word.split("-");
  return syllableArray.length;
  //return the new array from split (which will equal the number of syllables)
}
