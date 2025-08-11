# 문자열 곱하기
def solution(my_string, k):
    answer = ''
    
    for i in range(k):
        answer += my_string
    
    return answer

# 모범답안(그냥 문자열 * 숫자도 되는구나...)
# def solution(my_string, k):
#   return my_string*k