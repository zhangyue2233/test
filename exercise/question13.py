# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def if_reverse(num):
    return str(num) == str(num)[::-1]

x = if_reverse(123322)    
print(x)