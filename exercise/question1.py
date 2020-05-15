# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
my_nums = [1,2,3,4]

def create_num():
    results = []
    for i in my_nums:
        for j in my_nums:
            if i == j:
                continue
            for k in my_nums:
                if j==k or k==i:
                    continue
                results.append(i*100+j*10+k)
                pass
            pass
        pass
    return results
r = create_num()
print(r,len(r))