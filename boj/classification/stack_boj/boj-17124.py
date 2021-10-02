def binary(num, B, l, r):
    if r - l <= 1:
        return l
    mid = (l+r) // 2
    if num < B[mid]:
        return binary(num, B, l, mid)
    else:
        return binary(num, B, mid, r)


def findMin(d):
    curr = d[2]
    rst = 2
    if d[1] <= curr:
        curr = d[1]
        rst = 1
    if d[0] <= curr:
        curr = d[0]
        rst = 0
    return rst


def solve():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    B.sort()
    s = 0
    for num in A:
        p = binary(num, B, 0, M)
        d = []
        d.append(abs(B[p-1]-num))
        d.append(abs(B[p]-num))
        d.append(abs(B[(p+1) % M]-num))
        idx = findMin(d)
        s += B[p+idx-1]
    print(s)


T = int(input())
for _ in range(T):
    solve()
