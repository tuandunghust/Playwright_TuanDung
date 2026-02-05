import openpyxl
import os

class ExcelReader:
    @staticmethod
    def get_data(file_path, sheet_name="Sheet1"):
        if not os.path.exists(file_path):
             raise FileNotFoundError(f"File not found: {file_path}")
             
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        
        data = []
        headers = []
        
        # Read header row
        for cell in list(sheet.rows)[0]:
            headers.append(cell.value)
            
        # Read data rows
        for row in list(sheet.rows)[1:]:
            row_data = {}
            for index, cell in enumerate(row):
                row_data[headers[index]] = cell.value
            data.append(row_data)
            
        return data
