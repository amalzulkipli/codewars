// mine
function reverseWords(str) {
  let result = []
  for (let word of str.split(" ")) {
    result.push(word.split("").reverse().join(""));
  }
  return result.join(" ")
}

// clever
function reverseWords(str) {
  return str.split("").reverse().join("").split(" ").reverse().join(" ");
}
