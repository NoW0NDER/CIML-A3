import sys, grader, parse
from copy import deepcopy

def value_iteration(problem):
    return_value = ''
    return return_value

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -4
    problem_id = 3
    grader.grade(problem_id, test_case_id, value_iteration, parse.read_grid_mdp_problem_p3)