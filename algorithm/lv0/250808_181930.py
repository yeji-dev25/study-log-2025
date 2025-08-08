# 주사위 게임 2
def solution(a, b, c):
    answer = 0
    num_list = [a,b,c]
    num_list.sort()
    a = num_list[0]
    b = num_list[1]
    c = num_list[2]
    
    if a != b != c: answer = a+b+c
    elif a != b or b != c: answer = (a+b+c) * (a**2+b**2+c**2)
    else: answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    
    
    return answer

# 모범답안(set 함수로 동일값 추출함)
#  def solution(a, b, c):
#     check=len(set([a,b,c]))
#     if check==1:
#         return 3*a*3*(a**2)*3*(a**3)
#     elif check==2:
#         return (a+b+c)*(a**2+b**2+c**2)
#     else:
#         return (a+b+c)
# 처음에 answer을 모두 다른 수일경우로 초기화 해주고,
# 하나라도 같으면 if문에 걸리며 다 같을경우 또 다른 if문에 걸려서 값이 바뀐다.
# if를 두개만 쓰며, 리스트 정렬을 안써주므로 효율적인 관리가 가능해진다.
# def solution(a, b, c):
#     answer = a+b+c
#     if a == b or a == c or b == c: answer = (a+b+c) * (a**2+b**2+c**2)
#     if a == b == c: answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
#     return answer