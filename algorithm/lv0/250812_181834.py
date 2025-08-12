# l로 만들기
def solution(myString):
    
    for i in myString:
        if i < 'l': myString = myString.replace(i, 'l')
    
    return myString

# 모범답안(파이썬 형식대로 생각하는 능력을 기르자)
# def solution(myString):
#     answer = [x if x > 'l' else 'l' for x in myString]
#     return ''.join(answer)