from pathlib import Path
from pprint import pprint

def get_cats_info(path):
    file_path = Path(path)
    try:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
        else:
            print(f"Файл '{path}' не існує.")
            return None
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except IOError:
        print(f"Файл '{path}' пошкоджений або недоступний для читання.")
        return None
    except Exception as e:
        print(f"Непередбачена помилка: {e}")
        return None

    cats = []
    for line in lines:
        content = line.strip().split(",")
        if len(content) == 3:
            cats.append({
                "id": content[0],
                "name": content[1],
                "age": content[2]
            })
    return cats

cats_info = get_cats_info("C:/Users/iskor/OneDrive/Educations/goit-algo-hw-04/cats_info.txt")
pprint(cats_info)