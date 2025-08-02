# 카운트다운
def solution(n, k):

    answer = []
    # for i in range(1, n+1)로 하면 더 좋았을듯
    for i in range(n+1):
        if i % k == 0 and i != 0:
            answer.append(i)

    return answer

# 모범답안(꼭 1부터 시작할 필요없이, k의 배수이므로 k부터 시작하자.)
# def solution(n, k):
#     return [i for i in range(k,n+1,k)]
# def solution(n, k):
#     return list(range(k, n + 1, k))