# my solution
def solution(s):
    result = ""
    
    for letter in s:
        if letter == letter.upper():
            result += f" {letter}" 
        else:
            result += letter
    return result

#better pythonic
def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr