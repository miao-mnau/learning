from fastapi import FastAPI
import mysql.connector
import json

app = FastAPI()

DB_CONFIG = {
    'host': "127.0.0.1",
    'user': "root",
    'password': "123456",
    'database': "ai_intern_db", # <--- 我们刚刚创建的那个数据库
    'port': 3306
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"!!! 数据库连接失败: {err} !!!")
        return None
    
@app.get("/")
def read_root():
    return{"message":"欢迎来到我的‘迷你数据后端API’！"}

@app.get("/candidates")
def get_all_candidates():
    print("---正在处理 /candidates 请求...---")
    candidates_list = []

    conn = get_db_connection()

    if conn is None:
        return {"error": "数据库连接失败，请检查您的MySQL服务器是否正在运行"}

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, skills FROM candidates")
    all_rows = cursor.fetchall()

    for row in all_rows:
        try:
            row['skills']  = json.loads(row['skills'])
        except Exception as e:
            print(f"JSON 解冻失败：{e} - 原始数据：{row['skills']}")
            row['skills'] = []

        candidates_list.append(row)
    
    cursor.close()
    conn.close()

    return candidates_list