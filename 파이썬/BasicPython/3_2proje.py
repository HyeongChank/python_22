# sum = 0
# a = int(input("최종 숫자 : "))
# for i in range(1,a+1):
#     sum += i
# print(sum)

# num = int(input("최종 숫자: "))
# i=1
# hap = 0

# while i<= num:
#     hap += i
#     i = i+1
# print(num, hap)

# num = int(input("최종숫자"))
# sum = 0
# i = 0
# while i <= num:
#     sum += i
#     i = i + 1
# print(sum)





# a = int(input("출력 단"))
# for i in range(1,10):
#     print(a,"x", i,"=",a*i)


# num = int(input("출력 단 : "))
# i = 1
# while i <= 9:
#     print(num,"x", i,"=", num*i)
#     i = i+1

# print(100%3)


# i = 1
# num = int(input("배수 숫자 입력 : "))
# a = i * num
# while 100//num > 0:
#     print(a)
#     i = i+1
#     if a > 100:
#         break
#     else:
#         continue

# while i<= 100:
#     if(i%2==0) and (i%3!=0):
#         print(i,end=",")
#     i=i+1
    
num = int(input("배수"))
i = 0
sum = 0
while i < 10 :
    i = i + 1
    if(i%num) != 0:
        print(i,f"은 {num}의 배수아님")
        continue
    print(i,f"은 {num}의 배수임")             
    sum = sum + i

print(sum)



# sum = 0
# i = 0
# while i <= 10:
#     i= i+1
#     if(i%2==0) and (i%3!=0):
#         sum += i
#         print(i,end=" ")
        
# print("\n")
# print(sum)


