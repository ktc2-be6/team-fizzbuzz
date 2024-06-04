print('it works')

def fizz_numbers(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("fizz")
        else:
            print(i)

# 예시 사용
number = int(input("숫자를 입력하세요: "))
fizz_numbers(number)

