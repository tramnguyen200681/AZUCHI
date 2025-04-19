CREATE DATABASE AZUCHI_SQL;
USE AZUCHI_SQL;

CREATE TABLE categories(
category_id INT AUTO_INCREMENT PRIMARY KEY,
category_name VARCHAR(255) NOT NULL UNIQUE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE PRODUCTS (
	product_id VARCHAR(30) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_description TEXT,
	product_price DECIMAL(11,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    category_id INT,
	product_img VARCHAR(500),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

CREATE TABLE product_images(
	image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(30),
    image_url VARCHAR(500),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

SHOW TABLES;
SELECT * FROM products;
INSERT INTO categories(category_name)
VALUES('Rèm vải'), ('Rèm voan');

INSERT INTO PRODUCTS (product_id, product_name, product_description, product_price, stock_quantity, category_id, product_img)
VALUES (
	'FJ2216',
    'RÈM VẢI FUJI FJ2216 – VINTAGE & CAO CẤP',
    '1. Xuất xứ: Nhật Bản\n2. Chất liệu: ...\n3. Công nghệ chống cháy...',
    100000,
    100,
    1,
    '/static/images/FJ2216_1.png'
    );
    SET SQL_SAFE_UPDATES = 1;
    UPDATE PRODUCTS
    SET product_img = REPLACE(product_img, '/static/images/', '/static/images/products/');
    
    INSERT INTO PRODUCTS (product_id, product_name, product_description, product_price, stock_quantity, category_id, product_img)
    VALUES (
    'FJ2309',
    'RÈM VOAN FUJI FJ2309 – CAO CẤP JACQUARD',
    'Mã voan FJ2309 được dệt trên máy kim Jacquard là dòng voan cao cấp được sản xuất bằng công nghệ hiện đại, hướng đến thị trường Nhật Bản với các tiêu chuẩn chất lượng nghiêm ngặt. Chất liệu polyester cấu trúc kim cương mang lại độ bền vượt trội và khả năng phản sáng tối ưu.\nThiết kế họa tiết Jacquard tinh xảo, sắc nét, kết hợp sự mềm mại của voan giúp sản phẩm trở thành lựa chọn lý tưởng cho những không gian yêu cầu sự sang trọng và nhẹ nhàng.\n\nƯu điểm vượt trội:\n1. Vải nhập khẩu: Đáp ứng tiêu chuẩn Nhật Bản, sản phẩm có độ bền cao, dễ dàng giặt máy mà không lo mất dáng hoặc hư hỏng.\n2. Phản sáng và chống tia UV: Nhờ cấu trúc sợi poly kim cương, rèm có khả năng cản tia UV đến 52% và cản nhiệt 27%, giúp bảo vệ sức khỏe và đồ nội thất trong nhà (có chứng nhận).\n3. Tính thẩm mỹ cao: Họa tiết Jacquard dệt kim nổi bật nhưng vẫn giữ được vẻ nhẹ nhàng, thoáng đãng, thích hợp với nhiều phong cách thiết kế nội thất.\n4. Tiện dụng và bền bỉ: Vải voan không chỉ mềm mại mà còn chịu được giặt máy nhiều lần, đảm bảo độ bền lâu dài mà vẫn giữ được nét đẹp ban đầu.\n5. Chống cháy: Theo tiêu chuẩn Mỹ (có chứng nhận).\n6. Không Fomaldehyde, không dư lượng chất tẩy nhuộm độc hại (có chứng nhận).\n\nỨng dụng:\n• Không gian phòng khách: Tạo cảm giác thoáng đãng, sáng sủa nhưng vẫn đảm bảo cản nắng và bảo vệ không gian.\n• Phòng ngủ: Giúp tạo không gian nhẹ nhàng, thư giãn với ánh sáng dịu nhẹ.\n• Nhà hàng, quán café: Phù hợp với không gian mở, vừa tạo điểm nhấn vừa giữ được sự riêng tư nhất định.\n\nLý do chọn sản phẩm này:\nVoan dệt kim Jacquard không chỉ là một tấm rèm, mà còn là giải pháp toàn diện về thẩm mỹ và công năng. Khả năng chống UV, cản nhiệt cùng độ bền cao làm cho sản phẩm này trở thành lựa chọn lý tưởng cho những khách hàng muốn kết hợp giữa sự tinh tế và thực tiễn.\nVới sản phẩm này, chúng ta không chỉ được sở hữu một mẫu rèm đẹp mà còn mang đến giá trị về sức khỏe và sự tiện nghi cho khách hàng. Đây chắc chắn là sự lựa chọn hoàn hảo cho mọi không gian sống và làm việc hiện đại.',
    950000,
    100,
    2,
    '/static/images/products/fj2309.png'
);

ALTER TABLE products DROP COLUMN stock_quantity;

ALTER TABLE products DROP COLUMN product_height;
SHOW COLUMNS FROM products;
 
