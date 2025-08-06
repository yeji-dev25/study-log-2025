# 부분 문자열 이어 붙여 문자열 만들기
def solution(numLog):
    answer = ""
    for i in range(len(numLog)-1):
        number = numLog[i+1] - numLog[i]
        if number == 1: answer += "w"
        elif number == -1: answer += "s"
        elif number == 10: answer += "d"
        elif number == -10: answer += "a"
    
    return answer

# 모범답안(사전으로 zip 함수를 사용해 하나씩 짝지어준 다음 비교해서 문자열을 더해준다.)
# 범위를 1부터 시작해서 현재 인덱스와 이전 인덱스를 비교해준다.(나는 0부터 시자한대신 다음 인덱스와 현재 인덱스를 비교해줌)
# def solution(log):
    # res=''
    # joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    # for i in range(1,len(log)):
    #     res+=joystick[log[i]-log[i-1]]
    # return res