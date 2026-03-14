import sklearn
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt
import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from torch import nn


x,y=make_circles(1000, random_state=42, noise=0.05)
dataset= pd.DataFrame({"x1":x[:,0],"x2":x[:,1],"label":y})
print(dataset)
plt.scatter(x[:,0],x[:,1],c=y)
#plt.show()
x=torch.from_numpy(x).float()
y=torch.from_numpy(y).float().unsqueeze(1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

class classificationModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer1=nn.Linear(in_features=2,out_features=5)
        self.linear_layer2=nn.Linear(in_features=5,out_features=1)

    def forward(self,x:torch.tensor)->torch.tensor:
        return self.linear_layer2(self.linear_layer1(x))

model=classificationModel()
loss_fn=nn.BCEWithLogitsLoss()
optimizer=torch.optim.SGD(lr=0.01,params=model.parameters())

for epochs in range(1000):
    model.train()
    y_pred=model(x_train)
    #y_pred=torch.round(torch.sigmoid(y_pred)) to be used with bceloss
    #print(y_pred)
    loss=loss_fn(y_pred,y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    model.eval()
    with torch.inference_mode():
        test_pred=model(x_test)
        test_loss=loss_fn(test_pred,y_test)
    
    if epochs %10==0:
        print(f"loss {loss}, testloss:{test_loss}" )


print(model.state_dict())

