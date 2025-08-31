# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    
    for i in arr:
        for j in range(i):
            answer.append(i)
    
    return answer

# 다른 풀이(내가 푼 방법을 한줄로 정리한 풀이)
def solution(arr):
    return [i for i in arr for j in range(i)]
# 다른 풀이2(이중 for문 하지않고 리스트를 곱해서 더하는 방법)
def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer