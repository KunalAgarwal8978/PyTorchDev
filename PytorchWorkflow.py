import torch
from torch import nn
import matplotlib.pyplot as plt
#Datapreprocessing

x=torch.arange(0,1,0.02).unsqueeze(dim=1)
print(x.shape)
y=0.3+0.7*x
print(y.shape)

