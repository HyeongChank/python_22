# print("백문이불\n견이다")
# print("나는 \"수박\"이 좋다")
# print("C:\tdf")
# print("C:\\tdf")

# print("나는가리오리\r나라")  # 뒷글자가 앞글자 치환


a = input("영어 문장을 입력 : ")
print("입력된 문장의 길이는 : ",len(a))
print("각 단어의 첫 문자를 대문자로 변환 : ", a.title())  # 각 단어의 첫글자를 대문자로
print(a.upper())
print(a.count("a"))
print(a.isalpha())          # 문자로 구성되었는지 isalpha
print(a.isdigit())          # 숫자로 구성되었는지 isdigit
print(a.isupper())

b = "i like python i love python"
print(b.count(" "))