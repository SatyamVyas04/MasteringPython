import openpyxl as xl

# loading Workbook
wb = xl.load_workbook('transactions2.xlsx')
# loading a singular sheet
sheet = wb["Sheet1"]
# assigning a variable the cell value
cell = sheet["a1"]  # or "cell = sheet.cell(1, 1)"

# adding a graph to the data
