# 0823
# 두 정수 사이의 합
def solution(a, b):
    if a > b: a, b = b, a
    return sum([i for i in range(a, b+1)])