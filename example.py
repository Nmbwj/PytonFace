import torch

print("Torch Version: {}".format(torch.__version__))

print("GPU Avialable: {}".format(torch.cuda.is_available()))

print("Number of GPU device: {}".format(torch.cuda.device_count()))

print("Index of current GPU device: {}".format(torch.cuda.current_device()))

print("GPU Name: {}".format(torch.cuda.get_device_name(torch.cuda.current_device())))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device named in torch: {}".format(device))

print(torch.rand(3, 3).to(device))
