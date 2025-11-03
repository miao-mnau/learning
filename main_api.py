from fastapi import FastAPI, status
from pydantic import BaseModel
import mysql.connector
import json

app = FastAPI()

class CandidatesModel(BaseModel):
    name: str 
    skills: list

DB_CONFIG = {
    'host': "mainline.proxy.rlwy.net",
    'user': "root",
    'password': "jnFKylViDQKwLjALLBIaIdCfxxAHkszD",
    'database': "railway", # <--- 我们刚刚创建的那个数据库
    'port': 24162
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

@app.post("/candidates", status_code=status.HTTP_201_CREATED)
def create_candidate(candidate: CandidatesModel):
    print(f"--- 正在处理 POST / candidates 请求，数据为：{candidate}---")

    conn = get_db_connection()
    if conn is None:
        return{"error": "数据库连接失败"}
    
    cursor = conn.cursor()

    sql_query = "INSERT INTO candidates (name, skills) VALUES (%s, %s)"
    skills_json_string = json.dumps(candidate.skills)
    try:
        cursor.execute(sql_query, (candidate.name, skills_json_string))
        
        # 【极其重要！】
        # INSERT / UPDATE / DELETE 必须“提交”(Commit)！
        conn.commit() 
        
        # 获取刚创建的 "id"
        new_id = cursor.lastrowid
        
        print(f"--- 成功创建新候选人, ID: {new_id} ---")

    except mysql.connector.Error as err:
        print(f"!!! 插入数据时出错: {err} !!!")
        conn.rollback() # 如果出错了，就“回滚”（撤销操作）
        return {"error": str(err)}
    
    finally:
        cursor.close()
        conn.close()

    # “上菜”：把新创建的候选人（连同新ID）返回给顾客
    return {
        "id": new_id,
        "name": candidate.name,
        "skills": candidate.skills
    }

@app.put("/candidates/{candidate_id}")
def update_candidate(candidate_id: int, candidate: CandidatesModel):
    print(f"--- 正在处理 PUT /candidates/{candidate_id} 请求... ---")
    conn = get_db_connection()
    if conn is None:
        return {"error": "数据库连接失败"}
    cursor = conn.cursor()

    sql_query = """
        UPDATE candidates
        SET name = %s, skills = %s
        WHERE id = %s
    """
    skills_json_string = json.dumps(candidate.skills)

    try:

        cursor.execute(sql_query,(candidate.name, skills_json_string, candidate_id))

        conn.commit()

        if cursor.rowcount == 0:
            print(f"--- 警告：未找到 ID: {candidate_id}，更新失败 ---")
            return {"error": "Candidate not found"}
        
        print(f"--- 成功更新了 ID: {candidate_id} ---")

    except mysql.connector.Error as err:
        print(f"!!! 更新数据时出错: {err} !!!")
        conn.rollback()
        return {"error": str(err)}
    
    return {
        "id": candidate_id,
        "name": candidate.name,
        "skills": candidate.skills
    }

@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int):
    print(f"--- 正在处理 DELETE /candidates/{candidate_id} 请求... ---")

    conn = get_db_connection()
    if conn is None:
        return {"error": "数据库连接失败"}
    
    cursor = conn.cursor()

    sql_query = "DELETE FROM candidates WHERE id = %s"

    try:
        cursor.execute(sql_query, (candidate_id,))

        conn.commit()

        if cursor.rowcount == 0:
            print(f"--- 警告：未找到 ID: {candidate_id}，删除失败 ---")
            return {"error": "Candidate not found"}
        
        print(f"--- 成功删除了 ID: {candidate_id} ---")

    except mysql.connector.Error as err:
        print(f"!!! 删除数据时出错: {err} !!!")
        conn.rollback()
        return {"error": str(err)}
    
    finally:
        cursor.close()
        conn.close()

    return {"message": f"Candidate with id {candidate_id} was successfully deleted"}