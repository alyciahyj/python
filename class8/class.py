# ['蘋果', '香蕉', '葡萄']

# ['蘋果']
# ['a', 'b']
# [1, 2, 3]

# [1, 2] + ['b', 'c']

# [1, 2] * 2

# l = ['a', 'b', 'c']
# l[0]
# l[1]
# l[2]

# l = [0, 1, 2, 3, 4]
# l[0:3]
# l[3:5]

# len([])
# len(['蘋果'])
# len(['a', 'b'])
# len([1, 2, 3])

# l = ['a', 'b', 'c']
# for index in range(len(l)):
#     print(l[index])

# l = ['a', 'b', 'c']
# for element in l:
#     print(element)

# max([])
# max(['蘋果', '香蕉', '橘子'])
# max(['a', 'b'])
# max([1, 2, 3])

# min([])
# min(['蘋果', '香蕉', '橘子'])
# min(['a', 'b'])
# min([1, 2, 3])

# list('abc')
# list([4, 5, 6])
# list(range(3))
# '1,2,3'.split(',')
# '2020/1/1'.split('/')

# img = ['1', '2', '3']
# '-'.join(img)

# l = ['a', 'b', 'c']
# a = l.copy()
# a[0] = 1
# print(a, l)
# l = ['a', 'b', 'c']
# l
# l[0] = 'A'
# l
# l = ['a', 'b', 'c']
# a = l.com()
# a[0] = 1
# print(a, l)
juices = ['蘋果汁', '柳橙汁', '葡萄汁', '可樂', '系統關閉']
while True:
    for i in range(len(juices)):
        print(f'{i+1}).{juices[i]}')
    ans = int(input("請輸入編號:"))
    if ans == len(juices):
        print("~~系統關閉~~")
        break
    elif ans > len(juices) or ans <= 0:
        print("輸入錯誤查無此果汁，請重新輸入")

    else:
        print(f"您店的商品是{juices[ans-1]}")

l = [1, 2, 3]
l.append(4)
print(1)
