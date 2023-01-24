a = input("s")
b = input("ss")
print(a+b)        # sss 출력

a = int(input("5를 적어주세요>>>"))
b = int(input("6을 적어라>>>"))
print(a+b)         # input은 문자열로 값이 나와서 5적고 6적으면 56 이렇게 나옴 11이 나오려면 숫자로 바꿔야 함

c = float(input("5를 적어주세요>>>"))
d = float(input("6을 적어라>>>"))
print(c+d)

str_input = input("숫자 입력>")
num_input = float(str_input)       
print(num_input, "inch")    # 5.0 inch

a = input("첫 글자")
b = input("2번째 글자")
print(a,b)

c = b                    # a, b 순서 바꾸기 위해 c를 가져와 이동
b = a
a = c
print(a,b)

c = input("첫 글자")
d = input("2번째 글자")

c, d = d, c                # c, d 순서변경
print(c,d)






