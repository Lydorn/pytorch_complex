PyTorch Complex is a PyTorch extension library for working with complex tensors.

It implements basic operations such as multiplication, square root, etc.

Note: this was a very quick implementation to solve the problem of PyTorch not handling the complex type in computation and automated differentiation. 
Thus all functions have regular scalar tensors as input, and the default complex dimension is the last one. 
The complex dimension should be of size 2, representing the real and imaginary part.
The complex dimension can be specified as an optional argument for all functions.
A more proper way would be to define a ComplexTensor class inheriting from torch.Tensor and adapting its operation methods.