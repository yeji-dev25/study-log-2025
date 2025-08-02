# 카운트다운
def solution(start_num, end_num):
    answer = []
    for i in range(start_num - end_num+1):
        answer.append(start_num)
        start_num-=1
    return answer

# 모범답안(range 함수 주의.)
# def solution(start, end):
#   return list(range(start,end-1,-1))
