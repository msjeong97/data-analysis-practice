# Tensorflow

## 1. What is Tensorflow
- 딥러닝 프로그램을 쉽게 구현 할 수 있도록 기능을 제공하는 구글에서 만든 라이브러리다.
- 구현은 c++로 되어 있으나, python, java등 다양한 언어를 지원한다. 
- 텐서들의 흐름이라는 의미를 갖고 있으며, 자세한 내용은 뒤에서 설명한다.

## 2. What is tensor
- 텐서는 하나의 배열을 의미한다.
- 텐서는 Rank, Shape, Type 세가지의 특징을 갖는다. 
```python
tensor = [
[1, 2],
[2, 3],
[3, 4]
]
```
- Rank는 배영의 차원이다. 위 예제에서 Rank는 2다.
- Shape는 배열의 모양이다. 위 예제에서 Shape는 3 * 2다.
- Type는 텐거 값의 타입이다. 주로 float.32를 사용하며 위 예제는 int다. 

## 3. 
