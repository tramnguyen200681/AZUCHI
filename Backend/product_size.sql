CREATE TABLE product_sizes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(50),
    width INT,
    height INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
USE AZUCHI_SQL;

DROP TABLE IF EXISTS product_sizes;
CREATE TABLE product_size_prices (
	id INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(50),
    width INT,
    height INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
SHOW TABLES;