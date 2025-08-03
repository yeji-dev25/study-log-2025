# 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = 0
    n = my_string.find(is_prefix)
    if n == 0: answer = 1
    return answer

# 모범답안(my_string을 is_prefix 길이만큼 잘라서 is_prefixx와 같은지 비교하는 함수이다.)
# def solution(my_string, is_prefix):
#   if my_string[:len(is_prefix)]==is_prefix:return 1
#   return 0