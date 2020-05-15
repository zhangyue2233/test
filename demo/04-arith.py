# sum1 = 1+2*3/4
# print(sum1)

# sum2 = 2**3
# print(sum2)
# sum3 = 11 % 7
# print(sum3)

# sumStr1 = 'hello' *3
# print(sumStr1)
# sumStr2 = 'hello' + ' ' + 'world'
# print(sumStr2)

# sumList1 = [1,2,3] + ['a',True,4.0]
# print(sumList1)

# sumList2 = [5,6,7] * 4
# print(sumList2)

# The target of this exercise is 
# to create two lists called x_list and y_list, 
# which contain 10 instances of the variables x and y, 
# respectively. 
# You are also required to create a list called big_list, 
# which contains the variables x and y, 10 times each, 
# by concatenating the two lists you have created.
x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

x_list = x_list * 10
y_list = y_list * 10
big_list = x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")