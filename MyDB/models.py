from datetime import datetime
from .mysql_connector import db

class User:
    @staticmethod
    def create_table():
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL,
            username VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        db.execute_query(query)

    @staticmethod
    def create_user(telegram_id, username):
        query = """
        INSERT INTO users (telegram_id, username)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
        username = VALUES(username)
        """
        db.execute_query(query, (telegram_id, username))

class Order:
    @staticmethod
    def create_table():
        query = """
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            items JSON NOT NULL,
            total DECIMAL(10, 2) NOT NULL,
            status ENUM('new', 'preparing', 'ready', 'delivered', 'canceled') DEFAULT 'new',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) on DELETE CASCADE
        )
        """
        db.execute_query(query)

    @staticmethod
    def create_order(user_id, items, total):
        query = """
        INSERT INTO orders (user_id, items, total)
        VALUES (%s, %s, %s)
        """
        db.execute_query(query, (user_id, items, total))
        return db.fetch_one("SELECT LAST_INSERT_ID()")[0]

    @staticmethod
    def get_all_orders():
        query = """
        SELECT o.*, u.username
        FROM orders o
        JOIN users u ON o.user_id = u.id
        ORDER BY o.created_at DESC
        """
        return db.fetch_all(query)

    @staticmethod
    def update_order(order_id, status):
        query = "UPDATE orders SET status = %s WHERE id = %s"
        db.execute_query(query, (status, order_id))

class Product:
    @staticmethod
    def create_table():
        query = """
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price DECIMAL(10, 2) NOT NULL,
            category VARCHAR(100),
            image_url VARCHAR(500),
            is_available BOOLEAN DEFAULT TRUE
        )
        """
        db.execute_query(query)

    @staticmethod
    def get_all_available_products():
        query = "SELECT * FROM products WHERE is_available = TRUE"
        return db.fetch_all(query)

def init_database():
    User.create_table()
    Order.create_table()
    Product.create_table()
    print("Database tables initialized")