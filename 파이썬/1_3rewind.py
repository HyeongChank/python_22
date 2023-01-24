# num = int(input("현재의 월 입력 : "))

# if num == 3 or num == 4 or num == 5:
#     print("봄")
# elif num == 6 or num == 7 or num == 8:
#     print("여름")
# elif num == 9 or num == 10 or num == 11:
#     print("가을")
# else:
#     print("겨울")

#구구단 옆으로 나열
for num in range(1,10):
    print("\n")
    for i in range(1, 10, 1):
        print(i,"*",num,"=",num * i, end="\t")
        
    

