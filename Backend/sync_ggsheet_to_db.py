from google_service import get_ggsheet_data
import mysql.connector
from config import DB_CONFIG

def sync_products():
    data = get_ggsheet_data()
    
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    for row in data:
        product_id = row["Mã (id) sản phẩm"]
        name = row["Tên sản phẩm"]
        desc = row["Mô tả ngắn gọn"]
        price = int(row["Giá"])
        img = row["Hình ảnh sản phẩm (tối đa 10 hình)"]
        category = 1 if row["Danh mục"] == "Rèm vải" else 2


        # Check nếu đã có rồi thì skip để khỏi bị lỗi trùng khoá chính
        cursor.execute("SELECT COUNT(*) FROM products WHERE product_id = %s", (product_id,))
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO products (product_id, product_name, product_description, category_id, product_img)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (product_id, name, desc, price, category, img))

        width_values = row["Chiều ngang sản phẩm"].split("\n")
        height_values = row["Chiều cao sản phẩm"].split("\n")

        for w in width_values:
            w = w.strip()
            if w.isdigit():
                cursor.execute("INSERT INTO product_sizes (product_id, width, height) VALUES (%s, %s, NULL)", (product_id, int(w)))

        for h in height_values:
            h = h.strip()
            if h.isdigit():
                cursor.execute("INSERT INTO product_sizes (product_id, width, height) VALUES (%s, NULL, %s)", (product_id, int(h)))

    conn.commit()
    conn.close()

    
if __name__ == "__main__":
    sync_products()
    print("✅ Đã đồng bộ sản phẩm từ Google Sheets vào database.")
