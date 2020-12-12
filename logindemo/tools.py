# *** coding: utf-8 ***
#@Time   : 2020/12/2 17:12
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : tools.py

import csv

def write_csv(name, pwd):
    with open('result.csv', 'a+', newline='') as f:
        csv_write = csv.writer(f)
        data_row = [name, pwd]
        csv_write.writerow(data_row)

def read_csv(name, pwd):
    with open('result.csv', 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        for row in data:
            if name in row and pwd in row:
                return True

if __name__ == '__main__':
    # write_csv('lala', '33445')
    print(read_csv('lala', '33445'))