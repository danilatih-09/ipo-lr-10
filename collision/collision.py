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

print(isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)]))    