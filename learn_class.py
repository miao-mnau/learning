class Candidate:
    def __init__(self, name_from_outside, skills_from_outside):
        print(f"---正在创建新候选人：{name_from_outside}---")
        self.name = name_from_outside
        self.skills = skills_from_outside


    def checck_python_skill(self):
        print(f"---正在为{self.name}检查技能---")
        found_python = False
        for skill in self.skills:
            if skill.lower() == "Python":
                found_python = True
                break

        if found_python == True:
            return True
        else:
            return False
        
    def print_summary(self):
        print(f"候选人总结：Name = {self.name}, Skills = {self.skills}")

alex_candidate = Candidate("Alex", ["Java", "SQL", "Git"])
bob_candidate = Candidate("Bob", ["HTML", "python", "Docker"])

print("\n---开始检查技能---")
alex_has_python = alex_candidate.checck_python_skill()
bob_has_python = bob_candidate.checck_python_skill()
print("\n---打印最终结果---")
print(f"Alex是否会Python？{alex_has_python}")
print(f"Bob是否会Python？{bob_has_python}")

print("\n---打印对象总结---")
alex_candidate.print_summary()
bob_candidate.print_summary()

