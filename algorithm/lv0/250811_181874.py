# A 강조하기(lower 함수는 그 문자 자체를 바꾸는것이 아닌 반환 해주는것이다.)
def solution(myString):
    answer = ''
    myString = myString.lower()
    for i in myString:
        if i == "a":
            answer += "A"
        else: answer += i
    return answer

# 모범 답안(소문자로 바꾼 문자에 replace() 함수로 'a'를 'A'로 일괄 바꿈)
# def solution(myString):
#     return myString.lower().replace('a', 'A')