import torch
import torchmetrics
import numpy
import pandas
import torchvision
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torch import nn


train_data= datasets.FashionMNIST(
    root="PYTORCH",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=None
)

test_data=datasets.FashionMNIST(
    root="PYTORCH",
    train=False,
    download=True,
    transform=ToTensor(),
    target_transform=None
)


class cnn_model(nn.Module):

    def __int__(self, input_layers, hidden_layers, output_layers):
        self.super()
        self.conv_1=nn.Sequential(
            nn.Conv2d(
                in_channels=input_layers,
                out_channels=hidden_layers,
                padding=1,
                kernel_size=3,
                stride=1
            ),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=hidden_layers,
                out_channels=hidden_layers,
                padding=1,
                kernel_size=3,
                stride=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3,stride=1,padding=1)
        )


        self.conv_2= self.conv_1=nn.Sequential(
            nn.Conv2d(
                in_channels=input_layers,
                out_channels=hidden_layers,
                padding=1,
                kernel_size=3,
                stride=1
            ),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=hidden_layers,
                out_channels=hidden_layers,
                padding=1,
                kernel_size=3,
                stride=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3,stride=1,padding=1)
        )
        self.classifier=nn.Sequential(
            nn.Linear(in_features=input_layers, out_features=hidden_layers),
            nn.ReLU(),
            nn.Linear(in_features=hidden_layers, out_features=hidden_layers),
            nn.ReLU()
        )
    
    def forward(self,x):
        x=self.conv_1(x)
        x=self.conv_2(x)
        x=self.classifier(x)
        return x
