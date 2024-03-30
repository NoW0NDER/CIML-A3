import sys, grader, parse
from copy import deepcopy
import random


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def is_terminal(Q1,Q2):
    for y in range(len(Q1)):
        for x in range(len(Q1[y])):
            if isinstance(Q1[y][x], dict):
                for action in Q1[y][x]:
                    if abs(Q1[y][x][action]-Q2[y][x][action])>0.001:
                        return False
    return True


def to_string(Q):
    ret = ""
    for y in range(len(Q)):
        for x in range(len(Q[y])):
            if Q[y][x] == "#":
                action = "#"
            elif isinstance(Q[y][x], float):
                action = "x"
            else:
                action = max(Q[y][x], key=Q[y][x].get)
                # print(Q[y][x],max(Q[y][x], key=Q[y][x].get))
            ret += f"| {action} |"
        ret += "\n"
    return ret
    

def td_learning(problem):
    random.seed(253)
    Q_table = []
    epsilon = problem.noise
    alpha = 0.6
    for y in range(problem.len_y):
        Q_table.append([])
        for x in range(problem.len_x):
            if problem.grid[y][x] == "#":
                Q_table[y].append("#")
            elif is_number(problem.grid[y][x]):
                Q_table[y].append(float(problem.grid[y][x]))
            else:
                # N, E, S, W
                to_append = {"N":0, "E":0, "S":0, "W":0}
                if y == 0:
                    to_append.pop("N")
                if y == problem.len_y-1:
                    to_append.pop("S")
                if x == 0:
                    to_append.pop("W")
                if x == problem.len_x-1:
                    to_append.pop("E")
                if y-1 >= 0 and problem.grid[y-1][x] == "#":
                    to_append.pop("N")
                if y+1 < problem.len_y and problem.grid[y+1][x] == "#":
                    to_append.pop("S")
                if x-1 >= 0 and problem.grid[y][x-1] == "#":
                    to_append.pop("W")
                if x+1 < problem.len_x and problem.grid[y][x+1] == "#":
                    to_append.pop("E")
                Q_table[y].append(to_append)
                    

    while True:
        Q_table_new = deepcopy(Q_table)
        for y in range(problem.len_y):
            for x in range(problem.len_x):
                if problem.grid[y][x] == "#":
                    continue
                if is_number(problem.grid[y][x]):
                    continue
                intended_action = max(Q_table[y][x], key=Q_table[y][x].get)
                if random.random() < epsilon:
                    action = random.choice(list(Q_table[y][x].keys()))
                else:
                    action = intended_action
                sample = problem.livingReward 
                if action == "N":
                    new_y = y-1
                    new_x = x
                elif action == "S":
                    new_y = y+1
                    new_x = x
                elif action == "E":
                    new_y = y
                    new_x = x+1
                elif action == "W":
                    new_y = y
                    new_x = x-1
                if isinstance(Q_table[new_y][new_x], float):
                    sample += problem.discount*Q_table[new_y][new_x]
                elif Q_table[new_y][new_x] == "#":
                    sample += problem.discount*Q_table[y][x][action]
                else:
                    sample += problem.discount*Q_table[new_y][new_x][max(Q_table[new_y][new_x], key=Q_table[new_y][new_x].get)]
                Q_table_new[y][x][action] = (1-alpha)*(Q_table[y][x][action]) + alpha*sample
        if is_terminal(Q_table, Q_table_new):
            break
        alpha *= 0.9999
        epsilon *= 0.99
        Q_table = deepcopy(Q_table_new)
    
    
    return_value = to_string(Q_table)
    return return_value.rstrip()

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -4
    problem_id = 4
    grader.grade(problem_id, test_case_id, td_learning, parse.read_grid_mdp_problem_p4)