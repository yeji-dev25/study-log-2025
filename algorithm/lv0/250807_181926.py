# 수 조작하기1
def solution(n, control):
    
    for i in range(len(control)):
        if control[i] == "w":
            n += 1
        elif control[i] == "s":
            n -= 1
        elif control[i] == "d":
            n += 10
        elif control[i] == "a":
            n -= 10
    
    return n

# 모범답안(사전으로 zip 함수를 사용해 하나씩 짝지어준 다음 비교해서 문자열을 더해준다.)
# def solution(n, control):
#   key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
#   return n + sum([key[c] for c in control])