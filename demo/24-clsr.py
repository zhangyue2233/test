# def outer(msg):
#     'this is outer'
#     def inner():
#         "this is inner"
#         print(msg)
#     inner()

# outer('this is msg')

# def print_num(num):
#     def change_num():
#         num = 1
#         print(num)
#         pass
#     change_num()
#     print(num)
# print_num(2)    

# def print_msg(msg):
#     def trans_msg():
#         print('tanslate %s' % msg)
#     return trans_msg

# m = print_msg('emmmm')
# m()        

