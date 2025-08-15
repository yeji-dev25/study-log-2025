# 특별한 이차원 배열 2
def solution(arr):
    answer = 1
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]: answer = 0
    
    return answer

# 모범답안
# 결국엔 대칭행렬 판별 문제임. 먼저 *arr로 이중배열 리스트를 언패킹하고,
# zip으로 행과 열을 바꿔 전치 시켜줌 그리고 map으로 list 형태로 묶어줌 그리고 list로 이차배열 형식을 맞춰주고
# 그렇게 만들어진 행렬이 처음 arr와 같은지 비교한 후 true, false를 int로 묶어
# 0과 1로 나오게 함
# def solution(arr):
#   return int(arr == list(map(list, zip(*arr))))