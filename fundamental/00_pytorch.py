import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(torch.__version__)


scalar = torch.tensor(7)

print(scalar, scalar.ndim, scalar.item())

vector = torch.tensor([8,3,3,5])

print(vector, vector.ndim, vector.shape)

MATRIX = torch.tensor([[23,56,45],[35,256,11],[3,36,116],[21,67,38]])

print(MATRIX, MATRIX.ndim, MATRIX.shape)

print(MATRIX[2])

TENSOR = torch.tensor([[[1,2,3],[3,4,5],[6,7,8]],[[10,20,30],[40,50,60],[70,80,90]],[[9,8,7],[6,5,4],[3,2,1]]])
print(TENSOR, TENSOR.ndim, TENSOR.shape)

print(TENSOR[1])

