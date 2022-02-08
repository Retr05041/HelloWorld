# Pytorch Basics

# Jan. 31, 2021

# MAKE SURE TO HAVE THE CORRECT VERSION OF CUDA INSTALLED IF WANTED WHEN RUNNING THE PIP COMMAND

# Cuda Version for this venv : https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal

# Where to get Pytorch : https://pytorch.org/ | Useing 11.0 Cuda, Pip, 1.7.1

# Pip command : pip install torch===1.7.1+cu110 torchvision===0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html 

import torch

print(torch.cuda.is_available()) # Prints True if cuda works

# if you use `.cuda()` it will run something on GPU | CANT MULTIPLY 2 TENSORS TOGETHER IF ONES ON GPU AND ONES OFF | `my_tensor.cuda()` | `.cpu()` to Switch back

# https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html