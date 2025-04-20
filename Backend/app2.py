from flask import Flask, render_template, request, url_for, abort
from sync_ggsheet_to_db import sync_products

from google_service import get_ggsheet_data
from config import DB_CONFIG

import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        database="AZUCHI_SQL",
        user="root",
        password="!Cc8X8iMsVyjktj",
        host="localhost",
        port="3306"
    )
    return connection

@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/intro")
def intro():
    return render_template("intro.html")

@app.route("/contactInfo")
def contactInfo():
    return render_template("contactInfo.html")

#@app.route("/login")
#def login():
 #   return render_template("login.html")

@app.route("/remVai")
def remVai():
    return render_template("remVai.html")

@app.route("/remVoan")
def remVoan():
    return render_template("remVoan.html")

@app.route("/catalog")
def catalog():
    return render_template("catalog.html")

@app.route("/news")
def news():
    return render_template("news.html")

#@app.route("/bag")
#def bag():
 #   return render_template("bag.html")


@app.route("/products")
def product():
    conn = get_db_connection()
    cursor = conn.cursor()

    selected_categories = request.args.getlist('category')
    sort_order = request.args.get("sort", "default")
    min_price = int(request.args.get("min_price", 0))
    max_price = int(request.args.get("max_price", 5000000))

    query = """
        SELECT product_id, product_name, product_description, product_price, product_img, category_id 
        FROM products
    """
    conditions = []
    params = []

    search_query = request.args.get("search", "").lower()

    # Lọc theo từ khóa nếu có
    if search_query:
        conditions.append("(LOWER(product_name) LIKE %s OR LOWER(product_id) LIKE %s)")
        params.extend([f"%{search_query}%", f"%{search_query}%"])

    # Lọc theo giá luôn luôn có
    conditions.append("product_price BETWEEN %s AND %s")
    params.extend([min_price, max_price])

    # Filter theo danh mục
    if selected_categories:
        placeholders = ','.join(['%s'] * len(selected_categories))
        conditions.append(f"category_id IN ({placeholders})")
        params.extend(selected_categories)


    # Gộp tất cả conditions lại bằng AND
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Sort theo giá
    if sort_order == "price-asc":
        query += " ORDER BY product_price ASC"
    elif sort_order == "price-desc":
        query += " ORDER BY product_price DESC"

    cursor.execute(query, params)
    rawProducts = cursor.fetchall()
    conn.close()
    

    # Convert category id to product type:
    products = []
    for product in rawProducts:
        categoryName = "Rèm vải" if product[5] == 1 else "Rèm voan"
        products.append((product[0], product[1], product[2], product[3], product[4], categoryName))
    return render_template("product.html", 
                           products=products, 
                           selected_categories=selected_categories, 
                           sort_order=sort_order,
                           min_price=min_price,
                           max_price=max_price,
                           search_query=search_query)


@app.route("/product/<product_id>")
def productDetail(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    #Get the products
    cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
    product = cursor.fetchone()
    
    if product is None:
        conn.close()
        return "Không tìm thấy sản phẩm", 404
    
    
    # Convert tuple to dictionary
    product_dict = {
        "product_id": product[0],
        "product_name": product[1],
        "product_description": product[2],
        "product_price": product[3],
        "category_id": product[4],
        "product_img": product[5],
        "created_at": product[6],
        "category_name": "Rèm vải" if product[4] == 1 else "Rèm voan"
    }

    # Lấy tất cả kích thước width và height từ bảng product_sizes
    cursor.execute("SELECT DISTINCT width FROM product_size_prices WHERE product_id = %s", (product_id,))
    widths = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT height FROM product_size_prices WHERE product_id = %s", (product_id,))
    heights = [row[0] for row in cursor.fetchall()]


    cursor.execute("""
        SELECT width, height, price 
        FROM product_size_prices 
        WHERE product_id = %s
    """, (product_id,))
    price_dict = {f"{row[0]}x{row[1]}": row[2] for row in cursor.fetchall()}

    conn.close()
    
    return render_template("productDetail.html", 
                           product=product_dict, 
                           widths=widths, 
                           heights=heights, 
                           price_dict=price_dict)

@app.route("/sync-now", methods=["POST"])
def sync_now():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if token != "YOUR_SECRET_TOKEN":
        abort(403)  # Forbidden
    
    data = request.get_json()
    if not data:
        abort(400, "Dữ liệu không hợp lệ")

    product_id = data["product_id"]
    name = data["product_name"]
    desc = data["description"]
    price_by_size = data["price_by_size"]
    category = data["category"]
    image = data["image"]

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Insert sản phẩm chính nếu chưa có
    cursor.execute("SELECT COUNT(*) FROM products WHERE product_id = %s", (product_id,))
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO products (product_id, product_name, product_description, category_id, product_img)
            VALUES (%s, %s, %s, %s, %s)
        """, (product_id, name, desc, category, image))

    # 2. Parse các dòng kích thước + giá
    for line in price_by_size.strip().split("\n"):
        if not line.strip():
            continue
        try:
            size_part, price_str = line.split(":")
            width_str, height_str = size_part.lower().split("x")
            width = int(width_str.strip())
            height = int(height_str.strip())
            price = float(price_str.strip().replace(",", ""))
        except Exception as e:
            print("❌ Lỗi khi parse dòng:", line, e)
            continue

    # 3. Insert vào bảng product_size_prices nếu chưa có
        cursor.execute("""
            SELECT COUNT(*) FROM product_size_prices
            WHERE product_id = %s AND width = %s AND height = %s
        """, (product_id, width, height))
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO product_size_prices (product_id, width, height, price)
                VALUES (%s, %s, %s, %s)
            """, (product_id, width, height, price))


    conn.commit()
    conn.close()
    return "✅ Đã sync xong!", 200


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # lấy port render cung cấp
    app.run(host="0.0.0.0", port=port)
