import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_circles
from torch import nn

x,y=make_circles(1000,noise=0.03,random_state=42)
x=torch.from_numpy(x).float()
y=torch.from_numpy(y).float().unsqueeze(1)
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2)
print(len(x_train))
print(x_train)
plt.scatter(x[:,0],x[:,1],c=y)
#plt.show()


class nonLinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1=nn.Linear(2,10)
        self.layer2=nn.Linear(10,10)
        self.layer3=nn.Linear(10,1)
        self.relu=nn.ReLU()
    def forward(self,x):
        return self.layer3(self.relu(self.layer2(self.relu(self.layer1(x)))))
    
    
    
model=nonLinearModel()
print(model)


epoch=2000
loss_fin=nn.BCEWithLogitsLoss()
optimizer=torch.optim.SGD(lr=0.1,params=model.parameters())


for epoch in range(0,epoch):
    model.train()
    y_pred=model(x_train)
    loss=loss_fin(y_pred,y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    model.eval()
    with torch.inference_mode():
        y_test_pred=model(x_test)
        test_loss=loss_fin(y_test_pred,y_test)

    if epoch %10==0:
        print(f"loss {loss}, testloss:{test_loss}" )

def plot_decision_boundary(model, x, y):
        model.eval()

        # Create grid
        x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
        y_min, y_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5

        xx, yy = np.meshgrid(
            np.linspace(x_min, x_max, 200),
            np.linspace(y_min, y_max, 200)
        )

        # Convert grid to tensor
        grid = torch.from_numpy(
            np.c_[xx.ravel(), yy.ravel()]
        ).float()

        # Predict
        with torch.no_grad():
            logits = model(grid)
            probs = torch.sigmoid(logits)
            preds = probs.reshape(xx.shape)

        # Plot
        plt.contourf(xx, yy, preds, levels=50, cmap="RdBu", alpha=0.6)
        plt.scatter(x[:, 0], x[:, 1], c=y.squeeze(), edgecolors="k")
        plt.show()    

plot_decision_boundary(model=model,x=x.numpy(),y=y.numpy())