# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

def trans_int(num):
    print('位数是 %s 逆序 %s' % (len(str(num)),str(num)[::-1]))

trans_int(3452)    