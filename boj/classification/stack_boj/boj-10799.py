import sys


def calc(parens):
    sticks = 0
    prev = ""
    count = 0
    for p in parens:
        if p == "(":
            sticks += 1
        elif prev == "(":
            sticks -= 1
            count += sticks
        else:
            count += 1
            sticks -= 1
        prev = p

    return count


string = sys.stdin.readline().rstrip()

print(calc(string))
