# name = 'john'
# print('hello %s' % name)
# age = 20
# print('his name is %s his age is %d' % (name,age))
# mylist = [1,2,3]
# print('list %s' % mylist)

# You will need to write a format string which prints out the data using the following syntax:
#  Hello John Doe. Your current balance is $53.44.

# data = ("John", "Doe", 53.44)
# format_string = "Hello %s %s . Your current balance is $%d"

# print(format_string % data)

astring = "Hello world!"
# print(len(astring)) #字符串长度
# print(astring.index("o")) # 首次出现的位置
# print(astring.count("l")) # 计算出现次数
# print(astring[3:7])  #[3,7) 截取
# print(astring[3:7:3]) #截取字符间 间隔多少个字符
# print(astring[::-1]) # 字符倒序
# print(astring.upper())
# print(astring.lower())
# print(astring.startswith("Hello")) #Bool 以xxx开头
# print(astring.endswith("asdfasdfasdf")) #Bool 以xxx结尾
# afewwords = astring.split(" ") # 将字符串分割为数组
# print(afewwords)

# Try to fix the code to print out the correct information by changing the string.
# First occurrence of "a" should be at index 8
s = 'length=9a'
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
s = 'aba'
print("a occurs %d times" % s.count("a"))

s='abcdefghijlmnop'
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The characters with even index are '%s'" %s[0::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

s = 'hello'
# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

s= 'HELLO'
# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
s = 'String'
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

s='isome'
# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
s = 'what a stupid exercise'
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))