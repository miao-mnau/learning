import mysql.connector
import json

# --- 【“云”配置】---
# (这些是您从 Railway 拿到的，是正确的！)
DB_USER = "root"
DB_PASSWORD = "jnFky1V1DQKwLjALLBIaIdCfxxAHksZD"
DB_HOST = "mainline.proxy.rlwy.net"
DB_PORT = 24162  # <-- 我帮您把变量名从 DB_PROT 改成了 DB_PORT (Port/端口)
DB_NAME = "railway"
# ---------------------

try:
    # 1. 连接到“云”MySQL 服务器
    print(f"--- 正在连接到“云”MySQL服务器 ({DB_HOST}:{DB_PORT})... ---")
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        database=DB_NAME  # <-- 我们“直接”连接到“railway”数据库
    )
    mycursor = mydb.cursor()
    print(f"--- 成功连接到“云”数据库 '{DB_NAME}'！ ---")

    # 2. 【“修复”】我们“不”创建数据库了，我们“直接”创建“表”！
    print(f"--- 正在 '{DB_NAME}' 数据库中创建 'candidates' 表 (如果不存在)... ---")
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS candidates (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            skills JSON 
        )
        """
    )
    
    # 3. 检查“云”表格是否为空
    mycursor.execute("SELECT COUNT(*) FROM candidates")
    if mycursor.fetchone()[0] == 0:
        print(f"--- ‘{DB_NAME}’表是空的, 正在插入初始数据... ---")
        
        sql_query = "INSERT INTO candidates (name, skills) VALUES (%s, %s)"
        
        candidates_list = [
            ("Alex", json.dumps(["Java", "SQL", "Git"])),
            ("Bob", json.dumps(["HTML", "python", "Docker"])),
            ("Charlie", json.dumps(["Python", "Pandas", "AWS"])),
            ("David", json.dumps(["Go", "MySQL"]))
        ]
        
        mycursor.executemany(sql_query, candidates_list)
        mydb.commit() # “提交”到“云”
        
        print(f"成功插入了 {mycursor.rowcount} 条数据。")
    else:
        print("--- “云”数据已存在, 无需插入。 ---")
        
    print(f"\n*** “云”数据库 '{DB_NAME}' 已准备就绪！***")

except mysql.connector.Error as err:
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"!!! 发生错误: {err}")
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n【帮助】：请确保您的 Railway 数据库正在运行。")

finally:
    # 4. 关闭“云”连接
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("--- MySQL 连接已关闭。 ---")