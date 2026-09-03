import numpy as np
import torch
import torch.optim as optimiser
from liveshower import liveplotter

liver=liveplotter(window=2000)
class agent:
    def __init__(self,network,gamma,learning_rate):
        self.global_network=network
        self.gamma=gamma
        self.learning_rate=learning_rate
        self.optimiser=optimiser.Adam(params=network.parameters(),lr=learning_rate,weight_decay=0.8,betas=(0.9,0.99))
    def picker(self,probes_given):
        action=np.random.choice(a=len(probes_given),p=probes_given.detach().numpy())
        return action
    def thinker(self,envirolment):
        envirolment_data=torch.tensor(envirolment.maze.flatten(),dtype=torch.float32)
        probs=self.global_network(envirolment_data)
        action_taking=self.picker(probs)
        log_prob=torch.log(probs[action_taking])
        return action_taking,log_prob
    def real_G_generater(self,rewardes):
        rewardes_gen_in_termes_of_time=[]
        R=0
        for r in  reversed(rewardes):
            R=r+self.gamma*R
            rewardes_gen_in_termes_of_time.insert(0,R)
        return rewardes_gen_in_termes_of_time
    def learner(self,log_probes,rewardes_from_agent):
        real_rewardes_acc_to_timestep=self.real_G_generater(rewardes_from_agent)
        loss=-sum(prob*G for prob,G in zip(log_probes,real_rewardes_acc_to_timestep))
        liver.plot_ubdater(loss)
        return loss
    def ubdater(self,loss):
        self.optimiser.zero_grad()
        loss.backward()
        self.optimiser.step()
        return "----done ubdating-----"

