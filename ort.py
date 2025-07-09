import onnxruntime as ort
import numpy as np

# Load the ONNX model
ort_session = ort.InferenceSession("add_model.onnx", providers=["CoreMLExecutionProvider"])

# Prepare inputs
input_name1 = ort_session.get_inputs()[0].name
input_name2 = ort_session.get_inputs()[1].name
input_data1 = np.array([2/3.0], dtype=np.float32)
input_data2 = np.array([2/3.0], dtype=np.float32)
inputs = {input_name1: input_data1, input_name2: input_data2}

# Run the model
outputs = ort_session.run(None, inputs)

# Output result
output_name = ort_session.get_outputs()[0].name
output_value = outputs[0]
print(f"Output Value: {output_value}")
