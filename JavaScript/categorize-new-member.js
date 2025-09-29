# mine
function openOrSenior(data){
  let result = []
  for (const [age, handicap] of data) {
    if (age > 54 && handicap > 7) {
      result.push("Senior")
    } else {
      result.push("Open")
    }
  }
  return result
}

# better
function openOrSenior(data){
  return data.map(([age, handicap]) => (age > 54 && handicap > 7) ? 'Senior' : 'Open');
}
