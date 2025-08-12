# 문자열 바꿔서 찾기
def solution(myString, pat):
    answer = ''
    for i in myString:
        if i == 'A': answer += 'B'
        else: answer += 'A'
    return 0 if answer.find(pat) == -1 else 1

# 위에서 find로 안 찾아도 in 함수를 써도 됐겠다