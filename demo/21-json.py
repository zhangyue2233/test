# import json # Json 模块提供了四个方法： dumps、dump、loads、load

# lds = json.loads('1')
# print(lds,type(lds))

# lt = [1,2,3]
# dumps可以格式化大部分的基本数据类型为字符串    str , list , int , float , bool , dict , none
# dmp = json.dumps(lt)
# print(dmp,type(dmp))
# loads可以大部分基本数据类型字符串反序列化为对应类型
# lds = json.loads(dmp)
# print(lds,type(lds))

#dump将内容序列化，并写入打开的文件中
# v = {'k1':'yh','k2':'小马过河'}
# f = open('xiaoma.txt',mode='w',encoding='utf-8') #文件不存在就会生成
# res = json.dump(v,f)
# print(res)
# f.close()
#load将文件中的内容反序列化
# f = open('xiaoma.txt',mode='r',encoding='utf-8')
# data = json.load(f)
# f.close()
# print(data,type(data))

import pickle # pickle 模块也提供了四个功能：dumps、dump、loads、load

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))