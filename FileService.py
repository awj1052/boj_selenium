# test last solution number 74505618

import csv

file_path = 'last_solution.txt'
csv_path = 'user.csv'

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

def get_user_dict():
    dic = {}
    f = open(csv_path, mode='r')
    reader = csv.reader(f)

    for line in reader:
        dic[line[0]] = line[1]

    return dic

def get_name(usernames):
    dic = get_user_dict()
    names = []
    for user in usernames:
        if user in dic.keys():
            names.append(dic[user])
    return names
            