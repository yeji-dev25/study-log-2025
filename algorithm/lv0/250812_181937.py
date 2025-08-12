# n의 배수
def solution(num, n):
    answer = 0
    if num % n == 0: answer = 1
    
    return answer

# 모범답안(참과 거짓으로 나오는걸 int로 감싸면서 1과 0으로 나오게 함)
#  def solution(num, n):
#     return int(num % n == 0)