# 주사위 게임 1
def solution(a, b):
    answer = max(a,b) - min(a,b)
    
    if a % 2 != 0 and b % 2 != 0:
        answer = a**2 + b**2
    elif a % 2 != 0 or b % 2 != 0:
        answer = 2 * (a+b)
    
    return answer

# 절댓값은 그냥 함수 abs 사용하면 됨
# ex) abs(a-b)
