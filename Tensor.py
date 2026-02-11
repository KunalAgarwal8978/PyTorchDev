import torch
matrix=torch.tensor([1,2])


random_image_matrix= torch.rand(size=(224,224,3),
                                device="cpu")

tensor_a=torch.tensor([[2,4,5],[5,6,7]], dtype=float)
print(tensor_a.mean())
print(tensor_a.sum())
print(tensor_a.argmax())

x= torch.arange(1,10)
z= x.view(1,9)
x[0]=100
print(x.shape)
print(z.shape)
print(tensor_a[1][2])

y=torch.rand(size=[2,3,3,3]) # 2 matrix of size 3*3
print(y)
print(y[0])

print(torch.__version__)

