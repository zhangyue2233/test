# 题目：计算字符串中子串出现的次数
def count_str(sup,sub):
    return sup.count(sub,0,len(sup))


x =     count_str('asdcccasdvccsasdscdasdacdaasd','asd')
print(x)