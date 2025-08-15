# 특별한 이차원 배열 1
def solution(n):
    answer = [[0] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:answer[i][j] = 1    
    
    return answer

# 모범답안(어차피 i와 j가 같은 수인데 굳이 이중 for문을 돌 필요가 전혀 없었음)
# def solution(n):
#   answer=[[0]*n for i in range(n)]
#   for i in range(n): answer[i][i]=1
#   return answer