# 题目：输出9*9口诀。
for i in range(1,10):
    # print(i)
    line_list = []
    for j in range(i,10):
        line_list.append(str(i)+'*'+str(j)+'='+str(i*j))
    print(" ".join(line_list))
    print('-----------')