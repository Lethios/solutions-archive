# https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet:

    def __init__(self, rows: int):
        self.cell_dict = dict()

    def setCell(self, cell: str, value: int) -> None:
        self.cell_dict[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cell_dict[cell] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+")

        if x[0].isalpha():
            x = self.cell_dict.get(x, 0)
        else:
            x = int(x)
        if y[0].isalpha():
            y = self.cell_dict.get(y, 0)
        else:
            y = int(y)
        
        return x + y

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
