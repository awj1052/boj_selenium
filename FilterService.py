def filtering_problem_number(solved_data, target):
    filtered_data = []
    for solvedData in solved_data:
        if int(solvedData.problem_number) == target and solvedData.is_correct():
            filtered_data.append(solvedData)
    return filtered_data

def get_usernames(solvedData_list):
    usernames = set()
    for solvedData in solvedData_list:
        usernames.add(solvedData.user_name)
    return list(usernames)