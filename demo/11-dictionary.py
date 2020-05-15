# phoneBook = {}

# phoneBook['Jim'] = 987789123
# phoneBook['Adon'] = 999111234
# phoneBook['Kite'] = 989812345

# print(phoneBook)

# phoneBook = {
#     "Jim":987789123,
#     "Adon":999111234,
#     "Kite":989812345
# }
# # print(phoneBook)

# del phoneBook['Jim']
# phoneBook.pop('Adon')


# for name,number in phoneBook.items():
#     print('name: %s number: %d' % (name,number))

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook['Jake'] = 938273443

phonebook.pop('Jill')

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
