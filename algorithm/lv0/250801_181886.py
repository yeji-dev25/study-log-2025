def solution(names):
    answer = []
    n = len(names)//5+1

    for i in range(n):
        if len(names) % 5 == 0 and i==n-1: break
        answer.append(names[i*5])

    return answer

# 모범 답안...
# def solution(names):
#     return names[::5]
