my_internship_data = {
    "company":"DTSE (T-Mobile)",
    "position": "AI Intern",
    "required_sql":True,
    "my_sql_level":0
}

print("这是我的实习目标:")
print(my_internship_data)

position = my_internship_data["position"]
print(f"我申请的职位是：{position}")

my_internship_data["my_sql_level"] = 1
print(f"我现在的SQL的等级是：{my_internship_data['my_sql_level']}")

my_internship_data["my_python_level"] = 1
print(f"我现在的python的等级是: {my_internship_data['my_python_level']}")

print("----实习要求总结----")
for key, value in my_internship_data.items():
    print(f"Key:{key} ---> Value:{value}")