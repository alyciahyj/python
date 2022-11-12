# for i in range(2, 6):
#     print(i)
# else:
#     print("迴圈正常結束")

# i = 2
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("迴圈正常結束")

# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

#
# import random

# random.randint(1, 100)
# random.randrange(1, 100)

#
#
import random as r

x = r.randrange(0, 101)
while True:
    a = int(input('請輸入1~100的整數:'))
    if a > x:
        print('在小一點')
    elif a < x:
        print('在大一點')
    else:
        print('~恭喜猜中了!!!~')
        break
