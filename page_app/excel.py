import xlrd as xl
from data_goog.settings import MEDIA_ROOT


class ExcelImport:

    def __init__(self, file_name, version):
        # self.file_name = unicode(file_name, "utf-8")
        # 文件路径修改
        self.file_name = (MEDIA_ROOT + str(file_name)).replace("/", "\\").decode("utf-8")
        # print self.file_name
        self.workbook = xl.open_workbook(self.file_name)
        self.table = self.workbook.sheets()[0]
        # 获取总行数
        self.nrows = self.table.nrows

        # 版本号
        self.version = version

        self.cases = []

    def get_cases(self):
        # 从第二行开始
        for x in range(1, self.nrows):
            row = self.table.row_values(x)
            self.cases.append(
                {
                    "case_class": row[3],
                    "name": row[4],
                    "code": row[0],
                    "level": row[5],
                    "condition": row[6],
                    "step": row[7],
                    "expected_result": row[9],
                    "version": self.version
                })


