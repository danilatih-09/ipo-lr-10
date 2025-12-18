class RectCorrectError(Exception):
    pass

def isCorrectRect(rect):
    x1, y1 = rect[0]
    x2, y2 = rect[1]
    return x1 < x2 and y1 < y2

print(isCorrectRect([(-7, 9),(3, 6)]))