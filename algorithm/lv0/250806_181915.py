# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer

# 모범답안(my_string[idx]를 돌리고 []로 묶어서 리스트 형태로 만들어준다음 join으로 합침)
# def solution(my_string, index_list):
#   return ''.join([my_string[idx] for idx in index_list])