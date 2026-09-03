import torch.nn as nn
import torch.nn.functional as F

class Network(nn.Module):
	def __init__(self,input_size,hidden_layers,hidden_layer_neu,output_size):
		super(Network,self).__init__()
		self.list_of_layers=nn.ModuleList()
		self.first_layer=nn.Linear(input_size,hidden_layer_neu)
		self.list_of_layers.append(self.first_layer)
		for _ in range(hidden_layers):
			self.hidden_layer=nn.Linear(hidden_layer_neu,hidden_layer_neu)
			self.list_of_layers.append(self.hidden_layer)
		self.output_layer=nn.Linear(hidden_layer_neu,output_size)
	def  forward(self,data):
		look_up_data=data
		for  layers in self.list_of_layers:
			look_up_data=F.relu(layers(look_up_data))
		look_up_data=self.output_layer(look_up_data)
		predicted_output=F.softmax(look_up_data,dim=-1)
		return predicted_output



