# --- 您的初始数据 ---
# (注意：这次是一个 "列表List"，列表的 "每一项" 是一个 "字典Dict")
candidate_database = [
    {
        "id": 101,
        "name": "Alex",
        "skills": ["Java", "SQL", "Git"]
    },
    {
        "id": 102,
        "name": "Bob",
        "skills": ["HTML", "python", "Docker"] # Bob会小写的 "python"
    },
    {
        "id": 103,
        "name": "Charlie",
        "skills": ["Python", "Pandas", "AWS"] # Charlie会大写的 "Python"
    },
    {
        "id": 104,
        "name": "David",
        "skills": ["Go", "MySQL"]
    }
]

# --- 您的任务从这里开始 ---

# 任务1：创建“助手函数” (Helper Function)
# 您的第一个任务是：把您在 learn_func.py 里写的“检查逻辑”
# 变成一个完美的、可重复使用的“助手函数”。
#
# * 它应该叫:    check_python_skill
# * 它应该接收:  一个 "profile" 字典作为参数
# * 它应该返回:  True (如果技能中包含'python', 忽略大小写)
# * False (如果技能中不包含'python')
#
def check_python_skill(profile):
    found_python = False
    for skill in profile["skills"]:
        if skill.lower() == "python":
            found_python = True
            break

    if found_python == True:
        return True
    else:
        return False
    # [ 在这里写下您的“任务4”代码 (for, if, .lower(), return) ]
    # (提示：您几乎可以把 learn_func.py 里的函数体整个复制过来)
    # 您可以删掉这行 'pass'，然后开始写代码


# 任务2：创建“主函数” (Main Function)
# 这是您这个练习的核心。
#
# * 它应该叫:    find_qualified_candidates
# * 它应该接收:  一个 "candidate_list" (就像上面的 candidate_database)
# * 它应该返回:  一个 "新的列表"，里面只包含“合格”候选人的“名字(name)”
#
def find_qualified_candidates(candidate_list):
    print("--- 过滤器开始工作... ---")
    
    # 1. 创建一个空列表，用来存放“合格者”的名字
    qualified_names = []

    # 2. [ 在这里写一个 For 循环，遍历 "candidate_list" 中的每一个 "candidate" ]
    for candidate in candidate_list:
        if check_python_skill(candidate) == True:
            qualified_names.append(candidate["name"])
    return qualified_names
        # 3. [ 在循环内部，调用您的“助手函数” (任务1) 来检查“当前这个” candidate ]
        #    (提示: if check_python_skill(candidate) == True: )
        
            # 4. [ 如果“助手函数”返回True，就把“当前这个” candidate 的 "name" 添加到 qualified_names 列表中 ]
            #    (提示: qualified_names.append( ... ) )
    
    # 5. [ 在循环结束后，"返回" (return) 那个 "qualified_names" 列表 ]
    #pass # 您可以删掉这行 'pass'


# --- 您的主程序 (不要修改这里) ---
# (代码会从这里开始真正“运行”)
print("--- 启动候选人筛选程序 ---")

# 1. 调用您的“主函数”，并把“数据库”传给它
approved_list = find_qualified_candidates(candidate_database)

# 2. 打印最终结果
print("--- 筛选完毕! ---")
print(f"最终合格的候选人名单是: {approved_list}")

# 期望的输出 (Expected Output) 应该是:
# 最终合格的候选人名单是: ['Bob', 'Charlie']