import numpy as np
class envirolment:
    def __init__(self,rows,columes,target_row,target_col,general_punisher,wall_hitter_punisher,target_reward,no_of_walls,step_count_max):
        self.rows=rows
        self.columes=columes
        self.target_col=target_col
        self.target_row=target_row
        self.general_punisher=general_punisher
        self.wall_hitter_punisher=wall_hitter_punisher
        self.target_reward=target_reward
        self.normal_punisher_rep=0
        self.wall_punisher_rep=-1
        self.target_value_rep=1
        self.maze=0
        self.agent_row=0
        self.agent_col=0
        self.no_of_walls=no_of_walls
        self.step_count_target=step_count_max
        self.reach_target=0
    def maze_gen(self):
        self.maze=np.full((self.rows,self.columes),self.normal_punisher_rep)
        return self.maze
    def adding_walls_and_target_and_checker(self):
        for _ in range(self.no_of_walls):
#work on the max_size and the min_size to make them auto algo to fix the max and min sizes
            min_size_for_row=1
            max_size_for_row=4
            min_size_for_col=1
            max_size_for_col=4
            target_height_row=np.random.randint(min_size_for_row,max_size_for_row)
            target_height_col=np.random.randint(min_size_for_col,max_size_for_col)
            start_col=np.random.randint(0,self.columes-target_height_col)
            start_row=np.random.randint(0,self.rows-target_height_row)
            end_row=start_row+target_height_row
            end_col=start_col+target_height_col
            column_number=np.random.randint(0,self.columes)
            row_number=np.random.randint(0,self.rows)
            self.maze[start_row:end_row,column_number]=self.wall_punisher_rep
            self.maze[start_col:end_col,row_number]=self.wall_punisher_rep
        if self.maze[0:1,0:1]==-1:
            self.maze[0,0]=0
        if self.maze[self.target_row:self.target_row+1,self.target_col:self.target_col+1]==-1 or  self.maze[self.target_row:self.target_row+1,self.target_col:self.target_col+1]==0 :
            self.maze[self.target_row:self.target_row+1,self.target_col:self.target_col+1]=self.target_value_rep
        self.maze[0:2,0:2]=0
        return self.maze
    def checker(self,row_to_check,col_to_check):
        if row_to_check<=self.rows-1 and row_to_check>=0 and col_to_check<=self.columes-1 and col_to_check>=0:
            return True
        else:
            return False
    def action(self,action):
        #[rules 0 means up,1 means down ,2 means right ,3 means left]
        if action ==0:
            if self.checker(self.agent_row+1,self.agent_col)==True:
                self.agent_row+=1
                return (self.agent_row,self.agent_col)
            else:
                return "no action taken"
        if action==1:
            if self.checker(self.agent_row-1,self.agent_col)==True:
                self.agent_row-=1
                return (self.agent_row,self.agent_col)
            else:
                return "no action taken"
        if action==2:
            if self.checker(self.agent_row,self.agent_col-1)==True:
                self.agent_col-=1
                return (self.agent_row,self.agent_col)
            else:
                return "no action taken"
        if action==3:
            if self.checker(self.agent_row,self.agent_col+1)==True:
                self.agent_col+=1
                return (self.agent_row,self.agent_col)
            else:
                return "no action taken"
            return reward,status_of_agent
    def backtrack_due_to_wall(self,action_took):
        if action_took==0:
            self.agent_row-=1
        if action_took==1:
            self.agent_row+=1
        if action_took==2:
            self.agent_col+=1
        if action_took==3:
            self.agent_col-=1
    def done(self,step_count):
#       map={self.noraml_punisher_rep:self.general_punisher,self.wall_punisher_rep:self.wall_hitter_punisher,self.target_value_rep:self.target_reward}
        checker=self.maze[self.agent_row:self.agent_row+1,self.agent_col:self.agent_col+1]
        if checker==-1:
            return False
        if self.agent_row==self.target_row and self.agent_col==self.target_col:
            self.reach_target+=1
            return True
        if self.step_count_target==step_count:
            return True
        else:
            return False
    def step(self,pred_action,step_count):
        print("--------------")
        print(f"previosu_x {self.agent_row} previous_y {self.agent_col}")
        status=self.action(pred_action)
        #print(status)
        if status=="no action taken":
            reward=self.general_punisher-4000
            print(f"position {self.agent_row,self.agent_col}")
            print(f"no action on {pred_action}")
            return reward,False
        else:
            maps={self.normal_punisher_rep:self.general_punisher,self.wall_punisher_rep:self.wall_hitter_punisher,self.target_value_rep:self.target_reward}
            print(f"maps {maps}")
            print(f"action_took {pred_action}")
            print(f"position {self.agent_row,self.agent_col}")
            print(f"position_value {self.maze[self.agent_row:self.agent_row+1,self.agent_col:self.agent_col+1].flatten()[0]}")
            reward=maps[self.maze[self.agent_row:self.agent_row+1,self.agent_col:self.agent_col+1].flatten()[0]]
            status_of_agent=self.done(step_count)
            print(status_of_agent)
            if self.maze[self.agent_row:self.agent_row+1,self.agent_col:self.agent_col+1].flatten()[0]==-1:
                self.backtrack_due_to_wall(pred_action)
            return reward,status_of_agent
    def checker_for_maze(self):
        self.maze[0:2,0]=0
        self.maze[0:2,1]=0
    def reset(self):
        self.agent_row=0
        self.agent_col=0
        new_maze=self.maze_gen()
        self.maze=new_maze
        self.maze=self.adding_walls_and_target_and_checker()

##make more randomnes in the maze
#ok also add more row wise maze in the network
