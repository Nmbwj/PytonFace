import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rand_tens = torch.rand(3,4,4)

print(rand_tens)

zeros = torch.zeros(3,4,4)

print(zeros, zeros * rand_tens)

ones = torch.ones(3,4,4)

print(ones, ones *rand_tens, ones.dtype, rand_tens.dtype)
