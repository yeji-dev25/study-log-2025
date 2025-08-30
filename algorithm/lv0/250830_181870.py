# ad 제거하기
def solution(strArr):
    answer = []
    
    for i in strArr:
        if "ad" not in i:
            answer.append(i)
    
    return answer

# 다른 풀이
# 같은 식인데 한줄 코딩함
def solution(strArr):
    return [word for word in strArr if 'ad' not in word]
