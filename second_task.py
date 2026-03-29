from pprint import pprint

def get_cats_info(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cats = []
    for line in lines:
        content = line.strip().split(",")
        cats.append({
                "id": content[0],
                "name": content[1],
                "age": content[2]
                })

    return cats

cats_info = get_cats_info("C:/Users/iskor/OneDrive/Educations/goit-algo-hw-04/cats_info.txt")
pprint(cats_info)