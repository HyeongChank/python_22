# 짝수(even number), 홀수(odd number)
number = input("정수: ")
last_character = number[-1]  # 정수의 일의 자리

if last_character in "02468":
    print("짝수")
if last_character in "13579":
    print("홀수")

number = input("정수: ")
number = int(number)

if number % 2 == 0:
    print("짝수")
if number % 2 == 1:
    print("홀수")

