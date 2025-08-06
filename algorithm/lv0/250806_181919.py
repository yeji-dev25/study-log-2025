# 부분 문자열 이어 붙여 문자열 만들기
def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0: 
            n //= 2
            answer.append(n)
        else:
            n = 3 * n + 1
            answer.append(n)
    return answer
