from pathlib import Path

def get_cats_info(path_str: str):

    cats_info = []

    path = Path(path_str)
    if path.exists():
        if path.is_file():
            with open(path, encoding="utf-8", errors="strict") as file_cats_info:
                lines = [el.strip() for el in file_cats_info.readlines()]
            if len(lines) > 0:
                for line in lines:
                    line_list = line.split(',')
                    cats_info.append({"id": line_list[0], "name": line_list[1], "age": line_list[2]})
        else:
            print('Вказаний путь не є файлом')
    else:
        print('Вказаний путь не існує')

    return cats_info
