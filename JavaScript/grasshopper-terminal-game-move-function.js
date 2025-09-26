// mine
function move (position, roll) {
  return position+roll*2
}

// one liner
const move = (position, roll) => position + roll * 2

// honorable mention (wtf?)
const move=(_,$,_$)=>(_+[_$=-~[],++_$][-~[]]*$)
