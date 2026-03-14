from sklearn.datasets import make_blobs
from matplotlib import pyplot
import torch
from torch import nn
x,y=make_blobs(n_samples=1000,n_features=2,cluster_std=1, centers=4)

x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)
print(y.shape)
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test=train_test_split(x,y, test_size=0.2,random_state=42)

# Calculate accuracy (a classification metric)
def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item() # torch.eq() calculates where two tensors are equal
    acc = (correct / len(y_pred)) * 100 
    return acc

class multiClassModel(nn.Module):
    def __init__(self, input_features, output_features, hidden_features=8):
        super().__init__()
        self.layer=nn.Sequential(
            nn.Linear(in_features=input_features, out_features=hidden_features),
            nn.ReLU(),
            nn.Linear(in_features=hidden_features, out_features=hidden_features),
            nn.ReLU(),
            nn.Linear(in_features=hidden_features, out_features=output_features)
        )

    def forward(self,x):
        return self.layer(x)
    

model=multiClassModel(2,4)
loss_fn=nn.CrossEntropyLoss()
optimizer=torch.optim.SGD(params=model.parameters(), lr=0.1)

print(y[:5])

epochs=100
for epoch in range(epochs):
    model.train()
    y_logits = model(x_train) # model outputs raw logits 
    y_pred = torch.softmax(y_logits, dim=1).argmax(dim=1)
    loss=loss_fn(y_logits, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch %10==0:
        print(f"loss {loss}, acccuracy {accuracy_fn(y_pred=y_pred,y_true=y_train)}")
