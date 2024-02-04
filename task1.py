from pathlib import Path

def total_salary(path_str: str) -> [float, float]:

    total = 0
    average = 0

    path = Path(path_str)
    if path.exists():
        if path.is_file():
            with open(path, encoding = 'utf-8') as file_salary:
                lines = [el.strip() for el in file_salary.readlines()]
            if len(lines) > 0:
                for line in lines:
                    total += float(line.split(',')[1])
                average = total / len(lines)
        else:
            print('Вказаний путь не є файлом')
    else:
        print('Вказаний путь не існує')

    return [total, average]
