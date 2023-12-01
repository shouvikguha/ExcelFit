import openpyxl as xl

def create_workbook(filename):
    wb = xl.Workbook()
    wb.remove(wb.active)  # Remove the default sheet
    wb.save(filename)

def add_data(filename, sheet_name, data):
    wb = xl.load_workbook(filename)
    if sheet_name not in wb.sheetnames:
        wb.create_sheet(sheet_name)
    sheet = wb[sheet_name]
    sheet.append(data) # Add data to the sheet
    wb.save(filename)


