# 题目：输入三个整数x,y,z，请把这三个数由小到大输出
def sort_xyz(x,y,z):
    my_list = []
    my_list.append(x)
    my_list.append(y)
    my_list.append(z)
    my_list.sort( key=None, reverse=False)
    print(my_list)

sort_xyz(222,1,99)    
