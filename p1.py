import sys, random, grader, parse
from copy import deepcopy

def play_episode(problem):
    experience = ''
    return experience

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -8
    problem_id = 1
    grader.grade(problem_id, test_case_id, play_episode, parse.read_grid_mdp_problem_p1)