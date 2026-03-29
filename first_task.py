def total_salary(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.readlines()
        print(content)

    salaries = []
    for content in content:
        name, salary_str = content.strip().split(",")
        salary = int(salary_str)
        salaries.append(salary)

    total = sum(salaries)
    average = int(total / len(salaries))
    return total, average

total, average = total_salary("C:/Users/iskor/OneDrive/Educations/goit-algo-hw-04/total_salary.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")