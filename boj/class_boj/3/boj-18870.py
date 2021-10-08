"""
5
2 4 -10 4 -9

2 3 0 3 1

6
1000 999 1000 999 1000 999

1 0 1 0 1 0
"""

import sys


def solve():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    ordered = []

    for i, num in enumerate(arr):
        ordered.append((num, i))

    ordered.sort(key=lambda x: x[0])

    ans = [0] * N

    # [(-10, 2), (-9, 4), (2, 0), (4, 1), (4, 3)]
    #      0        1        2       3       4

    prev = -1
    cnt = -1

    for order, num_set in enumerate(ordered):
        num, index = num_set

        if num != prev:
            cnt += 1

        ans[index] = cnt
        prev = num

    return " ".join([str(x) for x in ans])


if __name__ == "__main__":
    print(solve())
