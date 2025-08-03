# 접미사 배열
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    answer.sort()
    return answer

# 다른 사람의 풀이(return 안에서 다 해결함)
# def solution(my_string):
#   return sorted(my_string[i:] for i in range(len(my_string)))