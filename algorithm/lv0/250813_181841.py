# 꼬리 문자열
def solution(str_list, ex):
    answer = ''
    
    for i in str_list:
        if ex not in i:
            answer += i
    
    return answer

# 모범답안(join 함수를 생각은 했으나 문자열을 어떻게 만들지는 생각 못함)
# def solution(str_list, ex):
#     return ''.join([i for i in str_list if ex not in i])
