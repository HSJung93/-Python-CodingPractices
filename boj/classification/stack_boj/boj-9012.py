"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

NO
NO
YES
NO
YES
NO

3
((
))
())(()

NO
NO
NO
"""
# import sys
# N = int(sys.stdin.readline())


def isValid(string):
    st = []
    for char in string:
        if char == "(":
            st.append(char)
        else:
            if len(st) == 0:
                return "NO"
            else:
                st.pop()

    if len(st) != 0:
        return "NO"

    return "YES"


# ans = []
# for _ in range(N):
#     s = sys.stdin.readline()
#     ans.append(isValid(s))

# for a in ans:
#     print(a)

print(isValid("((()()(()))(((())))()"))
