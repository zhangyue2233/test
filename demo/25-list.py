# map
# mylist = [1,2,3]
# def multiple(x):
#     return x*2
# count_list = list(map(multiple,mylist))
# count_list = list(map(lambda x: x ** 2, mylist) )
# count_list = list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# print(count_list)

# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [1,2,3,4,5]

# results = list(zip(my_strings, my_numbers))

# print(results)

# filter
# mylist = [1,2,3,4,5,6]
# def morethan3(x):
#     return x>3
# results = list(filter(morethan3,mylist))
# print(results)

# reduce
# from functools import reduce
# numbers = [1,2,3,4,5]
# def count_num(x,y):
    # return x+y
# results = reduce(count_num,numbers)
# results = reduce(count_num,numbers,10)
# print(results)

# In this exercise, you'll use each of map, filter, and reduce to fix broken code

from functools import reduce 

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
def square_float(x):
    return x*x
map_result = list(map(square_float,my_floats))   

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
def count_str(s):
    return s.count(s)<7
filter_result = list(filter(count_str,my_names))

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
def count_num(x,y):
    return x*y
reduce_result = reduce(count_num,my_numbers)

# Fix all three respectively.
# map_result = list(map(lambda x: x, my_floats))
# filter_result = list(filter(lambda name: name, my_names, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0)

print(map_result)
print(filter_result)
print(reduce_result)