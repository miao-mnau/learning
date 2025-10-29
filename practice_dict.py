# --- 这是您的初始数据 ---
# (一个嵌套字典，模拟从API或数据库来的JSON数据)

candidate_profile = {
    "candidate_id": 101,
    "name": "Alex",
    "contact_info": {
        "email": "alex.doe@example.com",
        "phone": "123-456-789"
    },
    "status": "Pending Review",
    "skills": ["Java", "SQL", "Git"]
}

print(f"--- 正在处理候选人: {candidate_profile['name']} ---")
print(f"原始数据: {candidate_profile}")

# --- 您的任务从这里开始 ---

# 任务1：访问并打印 (Accessing)
# 您的第一个任务是获取并打印出这位候选人的“电子邮件(email)”。
# (提示: 这是一个“嵌套”字典，您需要访问两层)
print("\n--- 任务1：打印Email ---")
# [ 在这里写您的代码来打印 'alex.doe@example.com' ]
print(f"Email:{candidate_profile['contact_info']['email']}")


# 任务2：修改数据 (Modifying)
# 我们发现候选人的状态(status)更新了。请将 "status" 的值从 "Pending Review" 修改为 "Technical Interview"。
print("\n--- 任务2：更新状态 ---")
# [ 在这里写您的代码来修改 status ]
# [ 在这里写一行代码来打印新的 'status' 值, 确认修改成功 ]
candidate_profile["status"] = "Technical Interview"
print(f"state:{candidate_profile['status']}")


# 任务3：添加数据 (Adding)
# 我们需要记录这位候选人是由谁推荐的。请在 'candidate_profile' 字典的顶层添加一个新的键值对：
# 键(key) 应该是 "referred_by"
# 值(value) 应该是 "Kateřina Malcová" (就是您在招聘广告上看到的那个联系人)
print("\n--- 任务3：添加推荐人 ---")
# [ 在这里写您的代码来添加新的键值对 ]
# [ 在这里写一行代码, 打印整个 candidate_profile 字典, 看看新数据是否加进去了 ]
candidate_profile["referred_by"] = "Kateřina Malcová"
print(candidate_profile)


# 任务4：【挑战】遍历并检查技能 (Looping & Logic)
# 这位候选人要申请 "AI Intern" 岗位, 我们知道 "Python" 是必须的。
# 请您写一个循环来检查 "skills" 列表：
#   - 如果在列表中找到了 "Python"，就打印 "候选人会Python，符合要求！"
#   - 如果循环结束了都没找到 "Python"，就打印 "警告：候选人缺少Python技能！"
print("\n--- 任务4：检查Python技能 ---")
# [ 在这里写您的循环和 if/else 逻辑代码 ]
found_python = False
for skill in candidate_profile["skills"]:
    if skill =="Python":
        print("候选人会Python,符合要求！")
        found_python = True
        break
if found_python == False:
    print("警告：候选人缺少Python技能！")
