# def my_function():
#     print('hello')

# my_function()    
# def my_function(name,age):
#     print('my name is %s my age is %d' % (name,age))

# my_function('jo',10)    

# def my_function(a,b):
#     return a+b

# c = my_function(1,2)
# print(c)    

# in this exercise you'll use an existing function, and while adding your own to create a fully functional program.
# Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
# Run and see all the functions work together!
# Modify this function to return a list of strings as defined above
def list_benefits():
    lst = []
    lst.append("More organized code")
    lst.append("More readable code")
    lst.append("Easier code reuse")
    lst.append("Allowing programmers to share and connect code together")
    return lst
    

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + 'is a benefit of functions!'
    

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()