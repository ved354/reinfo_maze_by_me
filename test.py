from envirolment import envirolment
from network import Network
import numpy as np
import torch
test=envirolment(15,15,14,14,-1,-10,100,24,20)
maze=test.maze_gen()
maze=test.adding_walls_and_target_and_checker()
network_1=Network(15*15,4,20,4)
maze=maze.flatten()
maze_tensor=torch.tensor(maze,dtype=torch.float32)
output=network_1.forward(maze_tensor)
print(output)
envirolmentes_in_list=[ envirolment(15,15,14,14,-1,-10,100,25,20) for _ in range(5)]
print(envirolmentes_in_list)
print(test.maze)
