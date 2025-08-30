# 홀짝에 따라 다른 값 반환하기
def solution(n):
    answer = 0
    
    if n % 2 != 0:
        for i in range(1, n+1, 2):
            answer += i
    else:
        for i in range(0, n+1, 2):
            answer += i*i
    
    return answer

# 다른 풀이
# 반복문을 하지 않고 sum 함수 사용함. sum 안에 range 함수 사용도 가능하구나
# 그리고 return으로 조건문을 반복하지 않음
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])

