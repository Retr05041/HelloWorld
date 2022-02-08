# IMPORTS
import torch # Duh
import numpy as np # Matrtices

"""
DIFFERENT WAYS TO MAKE TENSORS

Straight from data ::

data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)

From a NumPy array ::

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

From another Tensor ::

x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"Ones Tensor: \\n {x_ones} \\n")

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \\n {x_rand} \\n")

GETTING INFO FROM A TENSOR

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

MOVING A CPU TENSOR TO GPU (For speed)

# We move our tensor to the GPU if available
if torch.cuda.is_available():
  tensor = tensor.to('cuda')

"""

data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)
print(x_data)

if torch.cuda.is_available(): # checks if cuda is avaliable
    print("GPU enabled")
    print("Setting x_data to GPU")
    x_data = x_data.to("cuda")

print(f"Shape of tensor: {x_data.shape}")
print(f"Datatype of tensor: {x_data.dtype}")
print(f"Device tensor is stored on: {x_data.device}")