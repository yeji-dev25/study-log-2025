# n개 간격의 원소들
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer

# 모범답안(리스트에서 간격만큼 빼오는건 그냥 슬라이싱 문법이 편함)
# def solution(num_list, n):
#   return num_list[::n]