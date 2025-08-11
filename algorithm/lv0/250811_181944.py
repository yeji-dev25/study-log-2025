# 홀짝 구분하기
a = int(input())
if a % 2 == 0:
    print(a, "is even")
else:
    print(a, "is odd")

# 모범답안(f 스트링을 이용한 삼항연산)
# n = int(input())
# print(f"{n} is odd" if n % 2 else f"{n} is even")