# my solution
def count_smileys(arr):
    counter = 0
    
    v_eyes = [":", ";"]
    v_nose = ["-", "~"]
    v_mouth = [")", "D"]
    
    for face in arr:
        if len(face) == 2:
            eyes, mouth = face[0], face[1]
            if (eyes in v_eyes) and (mouth in v_mouth):
                counter += 1
        elif len(face) == 3:
            eyes, nose, mouth = face[0], face[1], face[2]
            if (eyes in v_eyes) and (nose in v_nose) and (mouth in v_mouth):
                counter += 1
    return counter

# pythonic
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

# pythonic
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
