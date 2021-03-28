# Tensorflow-practice

## 0. Install Python
```bash
$ pyenv install 3.8.5
$ pyenv virtualenv 3.8.5 <virtual_env_name>
```

## 1. Install Tensorflow
[Tensorflow Install](https://www.tensorflow.org/install/pip?hl=ko#macos)
```bash

$ pip3 install --upgrade pip
$ pip3 install --upgrade tensorflow

# check version
$ python -c "import tensorflow as tf; print(tf.version.GIT_VERSION, tf.version.VERSION)"
v2.4.0-49-g85c8b2a817f 2.4.1`
```

## 2. Install Jupyter Notebook
```bash
$ pip3 install jupyter 
$ jupyter notebook
```

## 3. Warning Message
```bash
$ python matrix_practice/matrix_gen.py
2021-03-26 21:37:54.607573: I tensorflow/compiler/jit/xla_cpu_device.cc:41] Not creating XLA devices, tf_xla_enable_xla_devices not set
2021-03-26 21:37:54.607858: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
``` 
- 일단 오류는 아니다. 경고 메세지다. 최신 CPU들은 AVX2, SSE4 등과 같은 instruction들을 지원한다. 이러한 명령어들은 스칼라 연산 및 벡터 연산의 성능을 높인다. 이러한 성능 개선은 학습 속도의 상승으로 이어진다.
- 공식 배포되는 텐서플로우 라이브러리는 위에서 설명한 특정 CPU, GPU특화 instruction이 사용되지않도록 되어 있다. 
- Sol1
	- ~~경고니까 무시한다. 아래와 같이 코드를 작성하면 무시 가능하다.~~
	```python
	import os
	os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
	import tensorflow as tf
	```
- Sol2
	- 소스코드 클론후 직접 빌드하여 바이너리를 생성
	[Tensorflow Install from Source](https://www.tensorflow.org/install/source?hl=ko#macos_1)
	```bash
	$ pip3 install -U pip numpy wheel
	$ pip3 install -U keras_preprocessing --no-deps
	$ git clone https://github.com/tensorflow/tensorflow.git
	
	#install bazel 3.7.2
	$ export BAZEL_VERSION=3.7.2
	$ curl -fLO "https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-darwin-x86_64.sh"
	$ chmod +x "bazel-${BAZEL_VERSION}-installer-darwin-x86_64.sh"
	$ ./bazel-${BAZEL_VERSION}-installer-darwin-x86_64.sh --user
	$ bazel --version

	# 사용 가능한 instruction 확인
	$ sysctl -a | grep "machdep.cpu.*features:"

	$ cd tensorflow
	$ ./configure
	
	# AVX2, FMA instruction을 지원하도록 빌드
	$ bazel build -c opt --copt=-mavx2 --copt=-mfma //tensorflow/tools/pip_package:build_pip_package

	$ pip install /tmp/tensorflow_pkg/tensorflow-<version>-<tags>.whl
	




	```	 

## 4. 
