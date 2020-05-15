# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续
def choose_day(s):
    day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    res_list = []
    for i in day_list:
        if i.find(s)>-1 and i.find(s)<len(s):
            res_list.append(i)
    print(res_list)
choose_day('s')