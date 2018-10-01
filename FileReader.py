
class FileReader:
    def __init__(self):
        self.fileHandle = None
        self.numOfColumns = 0
        self.columns = dict()
        self.table = dict()

    def parse(self, path):
        self.fileHandle = open(path, "r")
        self.parse_all_rows()

    def parse_all_rows(self):
        header_row = self.fileHandle.readline()
        self.columns = header_row.split('|')
        self.numOfColumns = len(self.columns)

        for row in self.fileHandle:
            self.parse_row(row)

    def parse_row(self, row):
        columns = row.split('|')
        self.table[columns[0].strip()] = columns

    def get_row(self, key):
        if key in self.table:
            return self.table[key]
        return None
