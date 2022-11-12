"""
請輸入要印出的箭頭大小
​
hint:
可利用字串乘法
val="*" * 3
print(val)
***
​
EX:
請輸入要印出的箭頭大小:3
  *  
 *** 
*****
  *  
  *  
  * 
"""
put = int(input('請輸入:'))
for z in range(put):
    print(" " * (put - 1 - z) + "*" * (z * 2 + 1))
for z in range(put):
    print(" " * (put - 1) + "*")