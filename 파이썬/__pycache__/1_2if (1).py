# score = int(input("enter your score : "))
# if score >= 4.2:
#     print("당신의 평점은: {}".format(score))
#     print("해외 연수 기회 부여")
# else :
#     print("다음 기회에")


# num1 = int(input("첫번째 숫자 입력 : "))
# num2 = int(input("두번째 숫자 입력 : "))

# print("두 수 중 큰 수는 ",max(num1,num2),\
#     "작은 수는 ",min(num1,num2),"입니다")


# num = int(input("현재 월: "))  ## 모르겠음 문제5
# if num >= 3 :
#     if num >= 6 :
#         if num >= 9 :
#             if num >= 12 :
#                 print("{}은 겨울임".format(num))
#             else :
#                 print("가을")
#         else:
#             print("여름")
#     else:
#         print("봄")
# else :
#     print("겨울")


month = int(input("현재 월 : "))
if month == 3 or month ==4 or month == 5:
    print("봄")
elif month >= 6 and month <=8:
    print("여름")
elif month >=9 and month <=11:
    print("가을")
else :
    print("겨울")