#coding=utf-8
import requests
import json
import xlrd
import unittest

workbook = xlrd.open_workbook(r'/Users/leiyali/Desktop/mywork_2020/data/apitest_data1.xls')

sheet_name = workbook.sheet_names()[0]
sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
print(sheet.cell_value(2,5))

print(json.dumps(sheet.cell_value(2,5)))
print(json.dumps(sheet.cell_value(2,5),indent=2,sort_keys=True))
rows = sheet.row_values(1)  # 获取第2行内容
cols = sheet.col_values(2)  # 获取第3列内容

print(sheet.name, sheet.nrows, sheet.ncols)

print('-------------------------->>>\n')
<<<<<<< HEAD
<<<<<<< HEAD

=======
print('--------------bugfix_dev branch for test------------>>>\n')
print('--------------bugfix_dev branch for test------------>>>\n')
print('--------------bugfix_dev branch for test------------>>>\n')
print('--------------bugfix_dev branch for test------------>>>\n')
print('--------------bugfix_dev branch for test------------>>>\n')
>>>>>>> bugfix_dev
=======
print('--------------test bugfix_dev branch 002------------>>>\n')
print('--------------test bugfix_dev branch 003------------>>>\n')
print('--------------test bugfix_dev branch 004------------>>>\n')


>>>>>>> dev


class RunMain:

    def __init__(self,url,method,data=None):
        res = self.run_main(url,method,data)

    def send_post(self,url,data):
        res = self.requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_get(self,url, data):
        res = self.requests.get(url=url, data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            send_get(url,data)
        else:
            send_post(url,data)
        return res

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    data = {
        'cart': '11'
    }
    run = RunMain(url,'GET',data)

    print(run)







