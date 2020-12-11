# coding=utf-8
import xlrd
import os

curPath = os.path.abspath(os.path.dirname(__file__))


class ExcelUtil:
    def __init__(self, excelpath, sheetname):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # Get the first row as the key value
        self.keys = self.table.row_values(0)
        # Get the total number of rows
        self.rowNum = self.table.nrows
        # Get the total number of columns
        self.colNum = self.table.ncols

    # 打印excel所有信息，每行信息保存在字典中。
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于2")
        else:
            data = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行开始取对应的values值
                values = self.table.row_values(j)
                for k in range(self.colNum):
                    s[self.keys[k]] = values[k]
                    data.append(s)
                j += 1
        return data

    # 将第二行的数据进行拼接并声明为全局变量供外部直接调用。
    def link_col1(self):
        values = self.table.row_values(1)
        global link_col
        link_col = values[1] + str(values[2])
        return link_col


if __name__ == '__main__':
    filepath = r"E:\Pythonworkspace\pythonExercise\utialmodel\data\sample.xlsx"
    sheetname = "Sheet1"
    data = ExcelUtil(filepath, sheetname)
    print(data.dict_data())
    print(data.link_col1())
    print(link_col)
