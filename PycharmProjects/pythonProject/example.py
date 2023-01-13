# standard library (표준 라이브러리)
import math #표준 라이브러리에 기본적인 것
import random
import os

#math 라이브러리
print(math.log10(100))  #가져다쓰면됨
print(math.cos(0))
print(math.pi) #파이를 가져 올수도 있음

#random 라이브러리
print(random.random()) #random라이브러리의 random() 함수는 0~1사이의 값을 알려줌

#os 라이브러리
print(os.getlogin()) # -> root 알려줌
print(os.getcwd()) # -> 현재 위치알려줌