import sys, random, grader, parse
from copy import deepcopy

def format_float(num):
    
    if abs(num - round(num)) < 1e-9:
        return f"{int(num)}.0"
    else:
        return f"{num:.3g}"

def play_episode(problem):
    experience = ''
    experience+="Start state:\n"
    experience+=problem.to_string()
    experience+=f"Cumulative reward sum: {problem.reward}\n"
    experience+="-------------------------------------------- \n"
    
    random.seed(problem.seed, version=1)
    # print(problem.policy)
    # print(problem.grid)
    d = {'N':['N', 'E', 'W'], 'E':['E', 'S', 'N'], 'S':['S', 'W', 'E'], 'W':['W', 'N', 'S']}
    while not problem.is_terminal:
        intended_action = problem.policy[problem.y][problem.x]
        if problem.policy[problem.y][problem.x] != "exit":
            action = random.choices(population=d[intended_action], weights=[1-problem.noise*2, problem.noise, problem.noise])[0]
            problem.move(action)
            experience += f"Taking action: {action} (intended: {intended_action})\n"
            experience += f"Reward received: {problem.livingReward}\n"
            problem.reward += problem.livingReward
            experience += f"New state:\n"
            experience += problem.to_string()
            experience += f"Cumulative reward sum: {format_float(problem.reward)}\n"
            experience += "-------------------------------------------- \n"
        else:
            experience += f"Taking action: exit (intended: exit)\n"
            problem.is_terminal = True
            reward = float(problem.grid[problem.y][problem.x])
            experience += f"Reward received: {reward}\n"
            problem.reward += reward
            experience += f"New state:\n"
            experience += problem.to_string()
            experience += f"Cumulative reward sum: {format_float(problem.reward)}"
            


    
    return experience

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -8
    problem_id = 1
    grader.grade(problem_id, test_case_id, play_episode, parse.read_grid_mdp_problem_p1)