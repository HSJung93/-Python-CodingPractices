from itertools import permutations

def solution(numbers):

    biggest = "0"
    for candi in permutations(numbers, len(numbers)):
        maid = "".join( map(str, candi) )
        if int(maid) > int(biggest):
            biggest = maid

    return biggest

print(solution([3, 30, 34, 5, 9]))