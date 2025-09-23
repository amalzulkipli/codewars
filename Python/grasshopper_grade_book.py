# mine
def get_grade(s1, s2, s3):
    avg = (s1+s2+s3)/3
    return 'A' if avg >= 90 else 'B' if avg >= 80 else 'C' if avg >= 70 else 'D' if avg >= 60 else 'F'

# pythonic
def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')
