# 题目：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？

import math

# 假设该数为 x
# 1.则有 x + 100 = a * a      x + 268 = b * b
# 2.a = math.sqrt(x+100)   b= math.sqrt(x + 268)
# 3.因为要取证数  所以对a 和 b 进行取整操作
# 4.再对整数a和整数b进行平方   若 int(a) * int(a) = a+100 且 int(b) * int(b) = a+268
# 5.若判断成立则可以将 数字x 取出

# 解1
# def find_num():
#     for x in range(-100,10000):
#         sqrt_a = int(math.sqrt(x+100))
#         sqrt_b = int(math.sqrt(x+268))
#         if sqrt_a**2 == x+100 and sqrt_b**2 == x+268:
#             print(x)
# find_num()

# 解2
# x = 0
# while True:
#     sqrt_a = int(math.sqrt(x+100))
#     sqrt_b = int(math.sqrt(x+268))
#     if sqrt_a**2 == x+100 and sqrt_b**2 == x+268:
#         print(x)
#         break
#     x += 1
        

