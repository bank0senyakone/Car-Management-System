import os
import mysql.connector
from mysql.connector import pooling

# Configuration for MySQL (Docker Container: mysql_exam)
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("DB_PORT", "3307"))  # Docker Map 3307:3306
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")   # <-- ໃສ່ລະຫັດຜ່ານຂອງ Docker MySQL ຢູ່ນີ້
DB_NAME = os.environ.get("DB_NAME", "jp_auto_db")

# Create connection pool to reuse connections and bypass DNS resolution delays
db_pool = pooling.MySQLConnectionPool(
    pool_name="jp_auto_pool",
    pool_size=10,
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

def get_db():
    return db_pool.get_connection()
