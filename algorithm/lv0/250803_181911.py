# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        answer = answer + my_strings[i][parts[i][0] : parts[i][1]+1]
    return answer

# 모범답안(join 함수로 문자열을 합치고, zip 함수로 문자끼리 짝지어줌)
# 참고. unzip 함수로 짝지어진 문자열들을 다시 해제할수있음. 즉, 다시 문자로 만듦
# join 함수를 사용하니 이중 배열을 사용 안해도 됨.
# def solution(my_strings, parts):
#   return ''.join([x[y[0]:y[1]+1] for x,y in zip(my_strings, parts)])