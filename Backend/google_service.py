import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEET_ID

def get_ggsheet_data():
    scope = ["https://spreadsheets.google.com/feeds", 
             "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)  # file này do Google tạo
    client = gspread.authorize(creds)
    sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1
    data = sheet.get_all_records()
    return data


# scope: Phạm vi truy cập mà app cần từ Google
# creds: Dùng client_secret.json để xác thực (do Google cấp)
# authorize(creds): Đăng nhập và tạo client
# sheet: Truy cập vào Sheet cụ thể bằng ID
# sheet.get_all_records(): Lấy toàn bộ data từ sheet dưới dạng list of dict