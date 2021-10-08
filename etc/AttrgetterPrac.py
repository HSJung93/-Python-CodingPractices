MixedTuples = [
    ("b", 2, "나"),
    ("a", 2, "나"),
    ("b", 1, "나"),
    ("a", 1, "나"),
    ("b", 2, "가"),
    ("a", 2, "가"),
    ("b", 1, "가"),
    ("a", 1, "가")
]

class Mixed:
    def __init__(self, eng, num, kor):
        self.eng = eng
        self.num = num
        self.kor = kor
        
    def __repr__(self):
        return repr((self.eng, self.num, self.kor))
    
MixedObjects = [
    Mixed("b", 2, "나"),
    Mixed("a", 2, "나"),
    Mixed("b", 1, "나"),
    Mixed("a", 1, "나"),
    Mixed("b", 2, "가"),
    Mixed("a", 2, "가"),
    Mixed("b", 1, "가"),
    Mixed("a", 1, "가")
]
        
MixedTuples.sort(key=lambda x:x[2])
MixedTuples.sort(key=lambda x:x[1])
MixedTuples.sort(key=lambda x:x[0])

print("0번째-1번재-2번째 요소 순 정렬 :")
print(MixedTuples)
print()

MixedObjects.sort(key=lambda x:x.kor)
MixedObjects.sort(key=lambda x:x.num)
MixedObjects.sort(key=lambda x:x.eng)

print("한국어-숫자-영어 순 정렬 :")
print(MixedObjects)
print()

from operator import itemgetter, attrgetter

MixedTuples.sort(key=itemgetter(1, 2, 0))

print("1번째-2번재-0번째 요소 순 정렬 :")
print(MixedTuples)
print()

MixedObjects.sort(key=attrgetter("num", "eng", "kor"))

print("숫자-영어-한국어 순 정렬 :")
print(MixedObjects)
