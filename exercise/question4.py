# 题目：输入某年某月某日，判断这一天是这一年的第几天
import datetime
def find_day(YYYY,mm,dd):
    date_info = datetime.date(YYYY, mm, dd).isocalendar()
    print(date_info[1]*7 + date_info[2])

find_day(2020,5,11)       