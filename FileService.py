# test last solution number 74505618

file_path = 'last_solution.txt'

def get_last_solution():
    last_solution = 0

    f = open(file_path, mode="r", encoding="utf-8")
    last_solution = int(f.readline())
    f.close()

    return last_solution

def update_last_solution(first_solution_number):
    f = open(file_path, mode="w", encoding="utf-8")
    f.write(str(first_solution_number))
    f.close()