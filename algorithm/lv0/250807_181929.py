# 원소들의 곱과 합
def solution(num_list):
    answer = 0
    total = 0
    mul = 1
    
    for i in num_list:
        total += i
        mul *= i
    
    if mul < total*total: answer = 1
    
    return answer
