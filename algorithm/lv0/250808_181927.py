# 마지막 두 원소
def solution(num_list):
    answer = num_list
    if num_list[len(num_list)-1] > num_list[len(num_list)-2]:
        answer.append(num_list[len(num_list)-1] - num_list[len(num_list)-2])
    else: answer.append(num_list[len(num_list)-1] * 2)
    return answer

# 모범답안(배열을 뒤에서부터 셀때는 -를 붙여주면 됨)
# def solution(num_list):
#     answer = num_list
#     if num_list[-1] > num_list[-2]:
#         answer.append(num_list[-1] - num_list[-2])
#     else: answer.append(num_list[-1] * 2)
#     return answer