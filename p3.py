import sys, grader, parse, copy
from copy import deepcopy
from p2 import to_string

def a_to_string(a_table, grid):
    ret = ""
    for i in range(len(a_table)):
        for j in range(len(a_table[i])):
            ret += f"| {a_table[i][j]} |"
        ret += "\n"
    return ret
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def value_iteration(problem):
    return_value = ''
    d = {'N':['N', 'E', 'W'], 'E':['E', 'S', 'N'], 'S':['S', 'W', 'E'], 'W':['W', 'N', 'S']}
    v_table = [[0 for _ in range(problem.len_x)] for _ in range(problem.len_y)]
    a_table = [[0 for _ in range(problem.len_x)] for _ in range(problem.len_y)]
    return_value += f"V_k=0\n{to_string(v_table, problem.grid)}"
    for _ in range(problem.iterations-1):
        new_v_table = copy.deepcopy(v_table)
        for y in range(problem.len_y):
            for x in range(problem.len_x):
                if problem.grid[y][x] == "#":
                    a_table[y][x] = "#"
                    continue
                if is_number(problem.grid[y][x]):
                    a_table[y][x] = "x"
                    new_v_table[y][x] = float(problem.grid[y][x])
                    continue
                max_val = -float('inf')
                for action in d.keys():
                    sum_ = 0
                    for intended_action in d[action]:
                        if intended_action == action:
                            T = 1-problem.noise*2
                        else:
                            T = problem.noise
                        if intended_action == "N":
                            if y-1>=0 and problem.grid[y-1][x] != "#":
                                sum_ += T*(problem.livingReward+problem.discount*v_table[y-1][x])
                            else:
                                sum_ += T*(problem.livingReward+problem.discount*v_table[y][x])
                        elif intended_action == "S":
                            if y+1 < problem.len_y and problem.grid[y+1][x] != "#":
                                sum_ += T*(problem.livingReward+problem.discount*v_table[y+1][x])
                            else:
                                sum_ += T*(problem.livingReward+problem.discount*v_table[y][x])
                        elif intended_action == "E":
                            if x+1 < problem.len_x and problem.grid[y][x+1] != "#":
                                sum_ += T*(problem.livingReward+problem.discount*v_table[y][x+1])
                            else:
                                sum_ += T*(problem.livingReward+problem.discount*v_table[y][x])
                        elif intended_action == "W":
                            if x-1 >= 0 and problem.grid[y][x-1] != "#":
                                sum_ += T*(problem.livingReward+problem.discount*v_table[y][x-1])
                            else:
                                sum_ += T*(problem.livingReward+problem.discount*v_table[y][x])
                    if sum_ > max_val:
                        max_val = sum_
                        a_table[y][x] = action
                        new_v_table[y][x] = sum_
        v_table = new_v_table
        return_value += f"V_k={_+1}\n"
        return_value += f"{to_string(v_table, problem.grid)}"
        return_value += f"pi_k={_+1}\n"
        return_value += f"{a_to_string(a_table, problem.grid)}"
    
    return return_value.rstrip()

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -4
    problem_id = 3
    grader.grade(problem_id, test_case_id, value_iteration, parse.read_grid_mdp_problem_p3)