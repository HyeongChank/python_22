sum = 0
while True:
    num = int(input("숫자"))
    sum += num
    if sum >30:
        print("30넘음")
        break

print(f"총 {sum}")
print("총", sum)
# for customer in ["아이","토르","그루트"]:
#     print("{}, 커피 완료".format(customer))

# for i in range(1,-20,-3):
#     print(i, end="  ")
