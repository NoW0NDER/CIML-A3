import copy
class ProblemP1:
    def __init__(self, seed, noise, livingReward, grid, policy,x,y):
        self.seed = seed
        self.noise = noise
        self.livingReward = livingReward
        self.grid = grid
        self.policy = policy
        self.x = x
        self.y = y
        self.reward = 0.0
        self.is_terminal = False
        self.len_y = len(grid)
        self.len_x = len(grid[0])
    def move(self, direction):
        if direction == "N":
            if self.y-1>=0 and self.grid[self.y-1][self.x] != "#":
                self.y -= 1
        elif direction == "S":
            if self.y+1 < self.len_y and self.grid[self.y+1][self.x] != "#":
                self.y += 1
        elif direction == "E":
            if self.x+1 < self.len_x and self.grid[self.y][self.x+1] != "#":
                self.x += 1
        elif direction == "W":
            if  self.x-1 >= 0 and self.grid[self.y][self.x-1] != "#":
                self.x -= 1
                

        
    def to_string(self):
        temp_map = copy.deepcopy(self.grid)
        if not self.is_terminal:
            temp_map[self.y][self.x] = "P"
        
        res_str = ""
        for row in temp_map:
            for ele in row:
                res_str += "{:>5}".format(ele)
            res_str += "\n"
        del temp_map
        return res_str

class ProblemP2(ProblemP1):
    def __init__(self, discount, noise, livingReward, grid, policy,x,y,iterations):
        super().__init__(-1, noise, livingReward, grid, policy,x,y)
        self.discount = discount
        self.reward = 0.0
        self.is_terminal = False
        self.len_y = len(grid)
        self.len_x = len(grid[0])
        self.iterations = iterations


class ProblemP3(ProblemP1):
    def __init__(self, seed, noise, livingReward, grid, policy, x, y, discount, iterations):
        super().__init__(seed, noise, livingReward, grid, policy, x, y)
        self.discount = discount
        self.reward = 0.0
        self.is_terminal = False
        self.len_y = len(grid)
        self.len_x = len(grid[0])
        self.iterations = iterations
        
class ProblemP4(ProblemP1):
    def __init__(self, seed, noise, livingReward, grid, policy, x, y, discount):
        super().__init__(seed, noise, livingReward, grid, policy, x, y)
        self.discount = discount
        self.reward = 0.0
        self.is_terminal = False
        self.len_y = len(grid)
        self.len_x = len(grid[0])
        

def read_grid_mdp_problem_p1(file_path):
    #Your p1 code here
    problem = ''
    with open(file_path, 'r') as file:
        seed = int(file.readline().strip().split()[1])
        noise = float(file.readline().strip().split()[1])
        livingReward = float(file.readline().strip().split()[1])
        grid = []
        file.readline()
        start_pos = (-1,-1)
        y = 0
        while line:=file.readline().strip():
            if line == "policy:":
                break
            else:
                line_elements = line.strip().split()
                if "S" in line_elements:
                    x = line_elements.index("S")
                    start_pos = (y,x)
                grid.append(line.strip().split())
                y+=1
        policy = []
        while line:=file.readline().strip():
            policy.append(line.strip().split())
    problem = ProblemP1(seed, noise, livingReward, grid, policy, start_pos[1], start_pos[0])
    return problem

def read_grid_mdp_problem_p2(file_path):
    #Your p2 code here
    problem = ''
    with open(file_path, 'r') as file:
        discount = float(file.readline().strip().split()[1])
        noise = float(file.readline().strip().split()[1])
        livingReward = float(file.readline().strip().split()[1])
        iterations = int(file.readline().strip().split()[1])
        grid = []
        file.readline()
        start_pos = (-1,-1)
        y = 0
        while line:=file.readline().strip():
            if line == "policy:":
                break
            else:
                line_elements = line.strip().split()
                if "S" in line_elements:
                    x = line_elements.index("S")
                    start_pos = (y,x)
                grid.append(line.strip().split())
                y+=1
        policy = []
        while line:=file.readline().strip():
            policy.append(line.strip().split())
    problem = ProblemP2(discount, noise, livingReward, grid, policy, start_pos[1], start_pos[0], iterations)
    return problem

def read_grid_mdp_problem_p3(file_path):
    #Your p3 code here
    with open(file_path, 'r') as file:
        discount = float(file.readline().strip().split()[1])
        noise = float(file.readline().strip().split()[1])
        livingReward = float(file.readline().strip().split()[1])
        iterations = int(file.readline().strip().split()[1])
        grid = []
        file.readline()
        start_pos = (-1,-1)
        y = 0
        while line:=file.readline().strip():
            line_elements = line.strip().split()
            if "S" in line_elements:
                x = line_elements.index("S")
                start_pos = (y,x)
            grid.append(line.strip().split())
            y+=1
    problem = ProblemP3(-1, noise, livingReward, grid, [], start_pos[1], start_pos[0], discount, iterations)
    return problem

def read_grid_mdp_problem_p4(file_path):
    #Your p4 code here
    with open(file_path, 'r') as file:
        discount = float(file.readline().strip().split()[1])
        noise = float(file.readline().strip().split()[1])
        livingReward = float(file.readline().strip().split()[1])

        grid = []
        file.readline()
        start_pos = (-1,-1)
        y = 0
        while line:=file.readline().strip():
            line_elements = line.strip().split()
            if "S" in line_elements:
                x = line_elements.index("S")
                start_pos = (y,x)
            grid.append(line.strip().split())
            y+=1
    problem = ProblemP4(-1, noise, livingReward, grid, [], start_pos[1], start_pos[0], discount)
    return problem