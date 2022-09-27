import openpyxl as xl

# loading Workbook
wb = xl.load_workbook('transactions2.xlsx')
# loading a singular sheet
sheet = wb["Sheet1"]

# adding a graph to the data
