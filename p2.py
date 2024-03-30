import sys, grader, parse, copy
from copy import deepcopy

def to_string(table ,map_):
    ret = ""

    for i in range(len(table)):
        for j in range(len(table[i])):
            if map_[i][j] == "#":
                ret += "| ##### |"
            else:
                ret += "|{:7.2f}|".format(table[i][j])
        ret += "\n"
    return ret


def policy_evaluation(problem):
    return_value = ''
    d = {'N':['N', 'E', 'W'], 'E':['E', 'S', 'N'], 'S':['S', 'W', 'E'], 'W':['W', 'N', 'S']}
    table = [[0 for _ in range(problem.len_x)] for _ in range(problem.len_y)]
    return_value += f"V^pi_k=0\n{to_string(table, problem.grid)}"
    for _ in range(problem.iterations-1):
        return_value += f"V^pi_k={_+1}\n"
        new_table = copy.deepcopy(table)
        for y in range(problem.len_y):
            for x in range(problem.len_x):
                if problem.grid[y][x] == "#":
                    continue
                if problem.policy[y][x] == "exit":
                    new_table[y][x] = float(problem.grid[y][x])
                    continue
                sum_ = 0
                intended_action = problem.policy[y][x]
                for action in d[intended_action]:  
                    if action == intended_action:
                        T = 1-problem.noise*2
                    else:
                        T = problem.noise
                    if action == "N":
                        if y-1>=0 and problem.grid[y-1][x] != "#":
                            sum_ += T*(problem.livingReward+problem.discount*table[y-1][x])
                        else:
                            sum_ += T*(problem.livingReward+problem.discount*table[y][x])
                    elif action == "S":
                        if y+1 < problem.len_y and problem.grid[y+1][x] != "#":
                            sum_ += T*(problem.livingReward+problem.discount*table[y+1][x])
                        else:
                            sum_ += T*(problem.livingReward+problem.discount*table[y][x])
                    elif action == "E":
                        if x+1 < problem.len_x and problem.grid[y][x+1] != "#":
                            sum_ += T*(problem.livingReward+problem.discount*table[y][x+1])
                        else:
                            sum_ += T*(problem.livingReward+problem.discount*table[y][x])
                    elif action == "W":
                        if x-1 >= 0 and problem.grid[y][x-1] != "#":
                            sum_ += T*(problem.livingReward+problem.discount*table[y][x-1])
                        else:
                            sum_ += T*(problem.livingReward+problem.discount*table[y][x])
                            
                new_table[y][x] = sum_
        table = new_table
        return_value += to_string(table, problem.grid)
                        
                
                
    
    
    
    return return_value.rstrip()

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -7
    problem_id = 2
    grader.grade(problem_id, test_case_id, policy_evaluation, parse.read_grid_mdp_problem_p2)