# 题目：要求输出国际象棋棋盘
for i in range(1,9):
    mylist = []
    for j in range(1,9):
        if i%2 == j%2 :
            mylist.append('*')
        else:
            mylist.append('0') 
    print(''.join(mylist))          
