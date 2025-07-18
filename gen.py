# Machine learning framework used to generate open Neural Network Exchange models on ONNX Runtime (ORT) which is a production grade AI engine running on an Apple Silicon accelerated machine learning inference AI processor, a type of NPU (Neural processing unit).

import torch
import torch.nn as nn

class AddModel(nn.Module):
    def __init__(self):
        super(AddModel, self).__init__()

    def forward(self, x, y):
        return x + y

model = AddModel()
input_one = torch.randn(1)
input_two = torch.randn(1)

torch.onnx.export(model, (input_one, input_two), "add_model.onnx")
