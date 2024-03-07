class SolvedData:

    def __init__(self, solution_number, user_name, problem_number, result):
        self.solution_number = solution_number
        self.user_name = user_name
        self.problem_number = problem_number
        self.result = result

    def is_correct(self):
        return True if self.result == "맞았습니다!!" else False