from task1 import total_salary
from task2 import get_cats_info

if __name__ == '__main__':

    # task 1
    total, average = total_salary('salary.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    
    # task 2
    cats_info = get_cats_info("cats_info.txt")
    print(cats_info)
