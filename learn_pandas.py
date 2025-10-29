import pandas as pd
data = {
    'name':['Alex', 'Bob', 'Charlie', 'David'],
    'skills':[
        ['Java', 'SQL', 'Git'],
        ['HTML', 'python', 'Docker'],
        ['Python', 'Pandas', 'AWS'],
        ['Go', 'MySQL']
    ]
}
df = pd.DataFrame(data)

print("---这是您的Pandas智能表格（DataFrame）---")
print(df)
print("\n---访问'skills'这一列(Series)")
skills_column = df['skills']
print(skills_column)

print("\n---正在用 Pandas 的方式检查Python技能---")
df['has_python'] = df['skills'].apply(
    lambda skill_list: any(skill.lower() == 'python' for skill in skill_list)
)

print("\n---这是检查后的新表格---")
print(df)

print("\n--- 最终合格的候选人名单 ---")
qualified_candidates = df[ df['has_python'] == True]

print(qualified_candidates)

print("\n--- 最终合格的候选人姓名 ---")
print(qualified_candidates['name'])