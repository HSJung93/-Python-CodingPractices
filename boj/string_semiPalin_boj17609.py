import sys

def isPalin(w, l, r):
    while l < r:
        if w[l] == w[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

def isPalinOrSemiPalin(w, l, r):
    while l < r:
        if w[l] == w[r]:
            l += 1
            r -= 1
        else:
            del_left = isPalin(w, l+1, r)
            del_right = isPalin(w, l, r-1)
            if del_left or del_right:
                return 1
            else:
                return 2
    return 0 
            

for _ in range(int(sys.stdin.readline().rstrip())):
    w = sys.stdin.readline().rstrip()
    l = 0
    r = len(w) - 1
    check = isPalinOrSemiPalin(w, l, r)
    print(check)