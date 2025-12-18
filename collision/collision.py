class RectCorrectError(Exception):
    pass

def isCorrectRect(rect):
    x1, y1 = rect[0]
    x2, y2 = rect[1]
    return x1 < x2 and y1 < y2

def isCollisionRect(first, second):
    if not isCorrectRect(first):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(second):
        raise RectCorrectError("2й прямоугольник некоректный")

    x1, y1 = first[0]
    x2, y2 = first[1]
    x3, y3 = second[0]
    x4, y4 = second[1]

    if x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4:
        return False
    return True
 
def intersectionAreaRect(first, second):
    if not isCorrectRect(first) or not isCorrectRect(second):
        raise ValueError("Некорректный прямоугольник")

    if not isCollisionRect(first, second):
        return 0

    x1, y1 = first[0]
    x2, y2 = first[1]
    x3, y3 = second[0]
    x4, y4 = second[1]

    left = max(x1, x3)
    right = min(x2, x4)
    bottom = max(y1, y3)
    top = min(y2, y4)

    return (right - left) * (top - bottom)

print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))