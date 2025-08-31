# x 사이의 개수
def solution(myString):
    answer = []
    count = 0
    for i in myString:
        if i == "x":
            answer.append(count)
            count = 0
        else: count+=1
    
    answer.append(count)
    
    return answer

# 다른 풀이(파이썬 형식으로 split 함수 사용하여 만든 코드)
def solution(myString):
    return [len(w) for w in myString.split('x')]