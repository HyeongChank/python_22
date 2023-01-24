# num = [[11,12,13],[21,22,23],[31,32,33,34],[41,42]]

# for j in range(len(num)):
#     sum = 0
#     for i in range(len(num[j])):
#         sum = sum +num[j][i]
#     print(j+1, "번째 줄의 합:",sum)


# from random import *

# lotto = []
# for j in range(1,6):
#     for i in range(1,7):
#         a=randint(1,45)
#         lotto.append(a)
#     print(lotto)
#     lotto.clear()


# num = [[11,33,22,7],[77,2,90],[3,66,44,9,8]]

# for j in range(len(num)):
#     sum = 0
#     for i in range(len(num[j])):
#         sum = sum + num[j][i]
#     print(j+1,sum, "최소값 : ",min(num[j]))
    

from random import *

lotto = []
for i in range(1,3):
    a=randint(1,10)
    lotto.append(a)
print(lotto)
lotto.clear()


