# 题目：用*号输出字母C的图案


# 000cccccc000
# 0cccccccccc0
# cccc0000cccc
# ccc000000000
# ccc000000000
# cccc0000cccc
# 0cccccccccc0
# 000cccccc000

for i in range(8):
    if i == 0:
        print('   ******   ')
    if i == 1:
        print(' ********** ')
    if i == 2:
        print('****    ****')
    if i == 3:
        print('***         ')
    if i == 4:
        print('***         ')
    if i == 5:
        print('****    ****')
    if i == 6:
        print(' ********** ') 
    if i == 7:
        print('   ******   ')                       
    