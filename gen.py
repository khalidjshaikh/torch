# SEO hello world onnx example onnx runtime
# conda activate test

import torch
import torch.nn as nn

class AddModel(nn.Module):
    def __init__(self):
        super(AddModel, self).__init__()

    def forward(self, x, y):
        return x + y

model = AddModel()
dummy_input1 = torch.randn(1)
dummy_input2 = torch.randn(1)

torch.onnx.export(model, (dummy_input1, dummy_input2), "add_model.onnx")
