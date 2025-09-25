// mine
function countBy(x, n) {
  let z = []
  for (let i = x; i < x*(n+1); i+=x) {
    z.push(i)
  }
  return z
}

