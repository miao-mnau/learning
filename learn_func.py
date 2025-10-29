def check_python_skill(profile):
    print(f"---正在为{profile['name']}检查技能 ---")

    found_python = False
    for skill in profile["skills"]:
        if skill.lower() == "python":
            found_python = True
            break

    if found_python == True:
        return True
    else:
        return False

alex_profile = {
    "name":"Alex",
    "skills":["Java", "SQL", "Git"]
}

bob_profile = {
    "name":"Bob",
    "skills":["HTML", "python", "Docker"]
}

alex_has_python = check_python_skill(alex_profile)

bob_has_python = check_python_skill(bob_profile)

print("\n--- 最终招聘决定 ---")

if alex_has_python == True:
    print("Alex 符合要求！")
else:
    print("Alex 不符合要求。")

if bob_has_python == True:
    print("bob 符合要求！")
else:
    print("bob 不符合要求。")