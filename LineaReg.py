import torch
from torch import nn
class LinearregressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights=nn.Parameter(torch.randn(1,requires_grad=True,dtype=torch.float))
        self.bias=nn.Parameter(torch.randn(1,requires_grad=True,dtype=torch.float))

    def forward(self,x:torch.tensor)->torch.tensor:
        return x*self.weights+self.bias
model =LinearregressionModel()
loss_fn=nn.L1Loss()
torch.manual_seed(42)
start=0
end=1
step=0.02

x = torch.arange(start, end, step).unsqueeze(dim=1)
y=0.7*x+0.3

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_train)
optimizer=torch.optim.SGD(params=model.parameters(),lr=0.01)
epochs=200
for epochs in range(epochs):
    model.train()
    y_pred=model(x_train)
    loss=loss_fn(y_pred, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

model.eval()
with torch.inference_mode():
    test_pred=model(x_test)
    test_loss=loss_fn(test_pred,y_test)





start=0
end=1
step=0.02
weight=0.7
bias=0.3
xl=torch.arange(start, end, step).unsqueeze(dim=1)
yl=weight*xl+bias


from sklearn.model_selection import train_test_split
xl_train,xl_test,yl_train,yl_test=train_test_split(xl,yl,test_size=0.2, random_state=42)
print(len(xl_train))
print(len(xl_test))
class linearModelV2(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer=nn.Linear(in_features=1,out_features=1)
    def forward(self,x:torch.tensor)->torch.tensor:
        return self.linear_layer(x)

torch.manual_seed(42)
modelv2=linearModelV2()


loss_funV2=nn.L1Loss()
optimizer_v2=torch.optim.SGD(params=modelv2.parameters(),lr=0.01)
print(modelv2.state_dict())
epochs=100
for epochs in range(epochs):
    modelv2.train()
    y_pred=modelv2(xl_train)
    loss=loss_funV2(y_pred,yl_train)
    optimizer_v2.zero_grad()
    loss.backward()
    optimizer_v2.step()

    modelv2.eval()
    with torch.inference_mode():
        test_pred=modelv2(xl_test)
        test_loss=loss_funV2(test_pred,yl_test)

    print(test_loss, loss)
print(modelv2.state_dict())