import mysql.connector
import json

DB_USER = "root"
DB_PASSWORD = "123456"
DB_HOST = "127.0.0.1"
DB_PROT = 3306

try:
    print(f"---正在连接到MySQL服务器({DB_HOST}:{DB_PROT})...---")
    mydb = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        port = DB_PROT
    )
    mycursor = mydb.cursor()

    DB_NAME = "ai_intern_db"
    print(f"---正在创建数据库'{DB_NAME}'(如果不存在)...---")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    mycursor.execute(f"USE {DB_NAME}")

    print("--- 正在创建 'candidates' 表 (如果不存在)... ---")

    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS candidates (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            skills JSON
        )
        """
    )

    mycursor.execute("SELECT COUNT(*) FROM candidates")
    if mycursor.fetchone()[0] == 0:
        print("---表示空的，正在插入初始数据...---")

        sql_query = "INSERT INTO candidates (name, skills) VALUES (%s, %s)"

        candidates_list = [
            ("Alex", json.dumps(["Java", "SQL", "Git"])),
            ("Bob", json.dumps(["HTML", "python", "Docker"])),
            ("Charlie", json.dumps(["Python", "Pandas", "AWS"])),
            ("David", json.dumps(["Go", "MySQL"]))
        ]

        mycursor.executemany(sql_query, candidates_list)
        mydb.commit()

        print(f"成功插入了 {mycursor.rowcount}条数据。")
    else:
        print("---数据已存在,无需插入。 ---")
    
    print(f"\n***数据库 '{DB_NAME}'已准备就绪！ ***")

except mysql.connector.Error as err:
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"!!! 发生错误: {err}")
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n【帮助】：")
    print("1. 请确保您的 MySQL 服务器 (比如 XAMPP, WAMP, 或您截图里的 'lol') 正在运行。")
    print(f"2. 请确保您的用户名 '{DB_USER}' 和密码 '{DB_PASSWORD}' 是正确的。")
    print(f"3. 请确保您的主机 '{DB_HOST}' 和端口 '{DB_PROT}' 是正确的。")

finally:
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("--- MySQL 连接已关闭。 ---")