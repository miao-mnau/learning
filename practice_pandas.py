import pandas as pd

# --- 您的初始数据 ---
# (一个字典，键是'列名'，值是'数据列表')
sales_data = {
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006],
    'salesperson': ['Alice', 'Bob', 'Alice', 'Bob', 'Alice', 'Charlie'],
    'amount': [250, 150, 300, 500, 100, 50],
    'status': ['Completed', 'Pending', 'Completed', 'Completed', 'Pending', 'Completed']
}

# --- 您的任务从这里开始 ---

# 任务1：创建 DataFrame
# (提示：使用 pd.DataFrame(...) )

print("--- 1. 原始销售数据 (DataFrame) ---")
df = pd.DataFrame(sales_data)  # [ 在这里替换 None，创建您的 DataFrame ]
print(df)


# 任务2：筛选数据
# (提示：使用您刚学会的“布尔筛选” df[... == ...] )
print("\n--- 2. 筛选出‘已完成’(Completed)的销售 ---")
completed_sales_df = df[df['status'] == 'Completed']  # [ 在这里替换 None，筛选出 'status' == 'Completed' 的行 ]
print(completed_sales_df)


# 任务3：分组与聚合 (Group By & Aggregate)
# 这是新知识，也是AI实习的核心技能！
# (提示：您需要先 .groupby('列名')，然后再选择要计算的列，最后调用 .mean() )
print("\n--- 3. 计算每个销售员的‘平均’销售额 ---")
# (我们只在“已完成”的销售里计算)
avg_sales_per_person = completed_sales_df.groupby('salesperson')['amount'].mean()  # [ 在这里替换 None，完成您的 .groupby(...) 和 .mean() ]
print(avg_sales_per_person)


# 期望的输出 (Expected Output) 应该是:
# salesperson
# Alice      200.0  (因为 Alice 已完成的是 250 和 100, (250+100)/2 = 200 )
# Bob        500.0  (因为 Bob 已完成的只有 500)
# Charlie     50.0  (因为 Charlie 已完成的只有 50)
# Name: amount, dtype: float64