# 0905
# 점프와 순간이동
def solution(n):
    cnt = 0
    while n > 0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            cnt += 1
    return cnt

print(solution(5000))