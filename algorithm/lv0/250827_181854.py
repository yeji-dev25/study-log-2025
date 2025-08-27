# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    if len(arr) % 2 != 0:
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] += n
    else:
        for i in range(len(arr)):
            if i % 2 != 0:
                arr[i] += n
    return arr

# 모범답안(if문으로 구별하지말고 처음 증가값을 조정해주자.)
# def solution(arr, n):
#     N=len(arr)
#     if N%2:
#         for i in range(0,N,2): arr[i]+=n
#     else:
#         for i in range(1,N,2): arr[i]+=n
#     return arr
