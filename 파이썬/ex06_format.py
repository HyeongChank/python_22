print("{} {} {} {}".format(1,2,3,4))            # 중괄호 안에 뒤 숫자, 문자 들어감


print("{} {} {} {}".format(2022, 4, 20, "월"))

print("HELLO".upper())           
print("HELLo".lower())

print("        문자      ".strip())             # 공백 없애기
print("        문자      ".rstrip())            # 오른쪽 공백 없애기
print("        문자      ".lstrip())            # 왼쪽 공백 없애기
print("가나다라마바사".find("라"))               # 0부터 세서 값 나옴

print("가나다라마바사".find("하"))               # 없으면 -1
print("가나다라마바사다나가".rfind("나"))         # 오른쪽부터 가장 먼저 있는거
print("가" in "가나다라마")                      # 있으면 true, 없으면 false
print("10 20 30 40 50".split(" "))              # " " 로 구분하여 앞에 수 구분

a = input("첫번째 수: ")
b = input("두번째 수: ")

print("{} + {} = {}".format(a, b, int(a)+int(b)))
print(a, " + ", b, " = ", int(a)+int(b))
