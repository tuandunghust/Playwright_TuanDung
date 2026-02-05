from openpyxl import Workbook
import os

def generate_test_data():
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    # Headers
    ws.append(["username", "password"])
    
    # Data
    ws.append(["user1@example.com", "password123"])
    ws.append(["user2@example.com", "password456"])
    
    output_path = 'data/users.xlsx'
    wb.save(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_test_data()
