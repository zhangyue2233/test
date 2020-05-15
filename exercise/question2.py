# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
# 成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
# 40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
# 100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

def count_profit(profit):
    amount_list = []
    result_num = 0
    if profit-1000000>0: # 100万以上
        amount_list.append((profit-1000000)*0.01)
        profit = 1000000
    if profit -600000>0: # 60-100万
        amount_list.append((profit-600000)*0.015)
        profit = 600000
    if profit - 400000 >0: #40 - 60 万
        amount_list.append((profit-400000)*0.03)
        profit = 400000
    if profit - 200000 >0: #20 - 40 万
        amount_list.append((profit-200000)*0.05)
        profit = 200000
    if profit - 100000 >0: #10 - 20 万
        amount_list.append((profit-100000)*0.075)
        profit = 100000
    if profit <= 100000: #小于10万
        amount_list.append(profit*0.1)
    for n in amount_list:
        result_num = result_num + n      
    return result_num


