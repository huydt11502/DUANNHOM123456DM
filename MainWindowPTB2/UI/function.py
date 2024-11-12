import math


def calc_PTB2(a,b,c):
    if a == 0:
        if b == 0 and c == 0:
            return "Infinity"
        elif b == 0 and c != 0:
            return "No solution"
        else:
            x = -c / b
            #print(f"{b}x+{c}=0")
            return x
    else:
        delta = math.pow(b, 2) - 4 * a * c
        if delta < 0:
            return "No solution"
        elif delta == 0:
            x = -b / (2 * a)
            return x
        else:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            return x1, x2
