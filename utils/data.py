import os
from utils.json_helper import read_json

# Đường dẫn tuyệt đối tới file JSON
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "user_data.json")

user_data = read_json(DATA_PATH)

EMAIL = user_data.get("email")
PASSWORD = user_data.get("password")
