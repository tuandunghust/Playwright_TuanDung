import json
import os

def read_json(file_path):
    """Đọc dữ liệu từ file JSON."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_json_value(file_path, key, value):
    """Cập nhật một giá trị trong file JSON."""
    data = read_json(file_path)
    data[key] = value
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
