Machine learning framework used to generate open Neural Network Exchange models on ONNX Runtime (ORT) which is a production grade AI engine running on an Apple Silicon accelerated machine learning inference AI processor, a type of NPU (Neural processing unit).

# PyTorch is an open-source machine learning framework primarily used for building and training deep learning models

# ONNX Runtime (ORT) is a production-grade AI engine that serves as a cross-platform accelerator for machine learning inference and training

python3 gen.py # ONNX AI model generated
# add_model.onnx
![](images/Screenshot 2025-07-09 at 10.22.12 AM.png)

# ONNX Runtime (ORT) is a production-grade AI engine that serves as a cross-platform accelerator for machine learning inference and training

python3 ort.py # Executed on the CoreML Inference AI processor, a type of NPU (Neural Processing Unit).
Output Value: [1.3333334]

---

macOS 15.5 M1

# macOS system
which python3
/usr/bin/python3

python3 --version
Python 3.9.6

brew install python3 pyenv

pip3 install torch onnx onnxruntime

python3 gen.py 
python3 ort.py 
Output Value: [1.3330078]

---

# homebrew
which python3
/opt/homebrew/bin/python3

python3 --version
Python 3.13.5

pyenv install 3.14-dev
pyenv global 3.14-dev

pip3 install torch onnx onnx runtime --break-system-packages

python3 gen.py 
python3 ort.py 
Output Value: [1.3330078]

---

# pyenv 3.14
pyenv global 3.14-dev

python3 --version
Python 3.14.0b3+

which python3
/Users/$USER/.pyenv/shims/python3

pip3 intall torch
## ERROR: No matching distribution found for torch

---

# pyenv 3.13
pyenv global 3.13

python3 --version
Python 3.13.5

which python3
/Users/$USER/.pyenv/shims/python3

pip3 install torch onnx onnxruntime

python3 gen.py 
python3 ort.py 
Output Value: [1.3330078]

---

pip3 install torch
Collecting torch
  Using cached torch-2.7.1-cp313-none-macosx_11_0_arm64.whl.metadata (29 kB)
Collecting filelock (from torch)
  Using cached filelock-3.18.0-py3-none-any.whl.metadata (2.9 kB)
Collecting typing-extensions>=4.10.0 (from torch)
  Downloading typing_extensions-4.14.1-py3-none-any.whl.metadata (3.0 kB)
Collecting setuptools (from torch)
  Using cached setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting sympy>=1.13.3 (from torch)
  Using cached sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
Collecting networkx (from torch)
  Using cached networkx-3.5-py3-none-any.whl.metadata (6.3 kB)
Collecting jinja2 (from torch)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting fsspec (from torch)
  Using cached fsspec-2025.5.1-py3-none-any.whl.metadata (11 kB)
Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch)
  Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting MarkupSafe>=2.0 (from jinja2->torch)
  Using cached MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (4.0 kB)
Using cached torch-2.7.1-cp313-none-macosx_11_0_arm64.whl (68.6 MB)
Using cached sympy-1.14.0-py3-none-any.whl (6.3 MB)
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
Downloading typing_extensions-4.14.1-py3-none-any.whl (43 kB)
Using cached filelock-3.18.0-py3-none-any.whl (16 kB)
Using cached fsspec-2025.5.1-py3-none-any.whl (199 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl (12 kB)
Using cached networkx-3.5-py3-none-any.whl (2.0 MB)
Using cached setuptools-80.9.0-py3-none-any.whl (1.2 MB)
Installing collected packages: mpmath, typing-extensions, sympy, setuptools, networkx, MarkupSafe, fsspec, filelock, jinja2, torch
Successfully installed MarkupSafe-3.0.2 filelock-3.18.0 fsspec-2025.5.1 jinja2-3.1.6 mpmath-1.3.0 networkx-3.5 setuptools-80.9.0 sympy-1.14.0 torch-2.7.1 typing-extensions-4.14.1

---

pip3 install onnx
Collecting onnx
  Using cached onnx-1.18.0-cp313-cp313-macosx_12_0_universal2.whl.metadata (6.9 kB)
Collecting numpy>=1.22 (from onnx)
  Downloading numpy-2.3.1-cp313-cp313-macosx_14_0_arm64.whl.metadata (62 kB)
Collecting protobuf>=4.25.1 (from onnx)
  Using cached protobuf-6.31.1-cp39-abi3-macosx_10_9_universal2.whl.metadata (593 bytes)
Requirement already satisfied: typing_extensions>=4.7.1 in /Users/khalid/.pyenv/versions/3.13.5/lib/python3.13/site-packages (from onnx) (4.14.1)
Using cached onnx-1.18.0-cp313-cp313-macosx_12_0_universal2.whl (18.3 MB)
Downloading numpy-2.3.1-cp313-cp313-macosx_14_0_arm64.whl (5.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 3.1 MB/s eta 0:00:00
Using cached protobuf-6.31.1-cp39-abi3-macosx_10_9_universal2.whl (425 kB)
Installing collected packages: protobuf, numpy, onnx
Successfully installed numpy-2.3.1 onnx-1.18.0 protobuf-6.31.1

---

pip3 install onnxruntime
Collecting onnxruntime
  Using cached onnxruntime-1.22.0-cp313-cp313-macosx_13_0_universal2.whl.metadata (4.5 kB)
Collecting coloredlogs (from onnxruntime)
  Using cached coloredlogs-15.0.1-py2.py3-none-any.whl.metadata (12 kB)
Collecting flatbuffers (from onnxruntime)
  Using cached flatbuffers-25.2.10-py2.py3-none-any.whl.metadata (875 bytes)
Requirement already satisfied: numpy>=1.21.6 in /Users/khalid/.pyenv/versions/3.13.5/lib/python3.13/site-packages (from onnxruntime) (2.3.1)
Collecting packaging (from onnxruntime)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: protobuf in /Users/khalid/.pyenv/versions/3.13.5/lib/python3.13/site-packages (from onnxruntime) (6.31.1)
Requirement already satisfied: sympy in /Users/khalid/.pyenv/versions/3.13.5/lib/python3.13/site-packages (from onnxruntime) (1.14.0)
Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime)
  Using cached humanfriendly-10.0-py2.py3-none-any.whl.metadata (9.2 kB)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /Users/khalid/.pyenv/versions/3.13.5/lib/python3.13/site-packages (from sympy->onnxruntime) (1.3.0)
Using cached onnxruntime-1.22.0-cp313-cp313-macosx_13_0_universal2.whl (34.3 MB)
Using cached coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
Using cached humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
Using cached flatbuffers-25.2.10-py2.py3-none-any.whl (30 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Installing collected packages: flatbuffers, packaging, humanfriendly, coloredlogs, onnxruntime
Successfully installed coloredlogs-15.0.1 flatbuffers-25.2.10 humanfriendly-10.0 onnxruntime-1.22.0 packaging-25.0

---

# AI
python3 gen.py 
python3 ort.py 
Output Value: [1.3333334]

---

# PyTorch is an open-source machine learning framework primarily used for building and training deep learning models

# ONNX Runtime (ORT) is a production-grade AI engine that serves as a cross-platform accelerator for machine learning inference and training

python3 gen.py # ONNX AI model generated
# add_model.onnx
![](images/Screenshot 2025-07-09 at 10.22.12 AM.png)

# ONNX Runtime (ORT) is a production-grade AI engine that serves as a cross-platform accelerator for machine learning inference and training

python3 ort.py # Executed on the CoreML Inference AI processor, a type of NPU (Neural Processing Unit).
Output Value: [1.3333334]
