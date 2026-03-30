from pathlib import Path

def total_salary(path):
    file_path = Path(path)
    try:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                print(lines)

                salaries = []
                for line in lines:
                    name, salary_str = line.strip().split(",")
                    salary = int(salary_str)
                    salaries.append(salary)

                total = sum(salaries)
                average = float(total / len(salaries))
                return total, average
        else:
            print(f"Файл '{path}' не існує.")
            return None
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None

total, average = total_salary("C:/Users/iskor/OneDrive/Educations/goit-algo-hw-04/total_salary.txt")
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")