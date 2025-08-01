def solution(num_list, n):
    answer = []
    # append로 하면 리스트 자체가 담기므로
    # extend로 리스트 요소 원소를 하나씩 넣어줌
    answer.extend(num_list[n::])
    answer.extend(num_list[:n:])
    return answer

# 모범답안(리스트끼리 그냥 더해도 됨)
# def solution(num_list, n):
#     return num_list[n:] + num_list[:n]
# def solution(num_list, n):
#     answer = []
#     answer.extend(num_list[n:] + num_list[:n])
#     return answer
