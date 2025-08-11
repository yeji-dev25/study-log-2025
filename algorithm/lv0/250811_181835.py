# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    if k % 2 == 1:
        for i in range(len(arr)):
            arr[i] *= k
    else:
        for i in range(len(arr)):
            arr[i] += k
    return arr
