# 题目：求100之内的素数

def find_num():
    alist = []
    for i in range(2,100):
        flag = False
        for j in range(2,i-1):
            if i%j == 0:
                flag = True
                continue
        if not flag:
            alist.append(i)        
    print(alist)        
find_num()