number = int(input('fizzbuzz를 출력할 범위를 입력하세요: '))

for i in range(1, number + 1):
    if i%3==0 and i%5==0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)


