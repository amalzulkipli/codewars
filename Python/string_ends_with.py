# my sol
def solution(text, ending):
    return True if text[-(len(ending))::] == ending else False

# pythonic
def solution(string, ending):
    return string.endswith(ending)
