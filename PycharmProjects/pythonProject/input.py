#입력 함수 input
input_str = input("이름을 입력하세요 : ") #중요! str로 넣음

print("{}".format(input_str))
print(type(input_str)) # -> <class 'str'>

input_str = input("숫자를 입력하세요 : ")
print(input_str+5) #에러뜸! -> 해결방법 정수/실수형으로 만들어주기
input_int = int(input("숫자를 입력하세요 : "))
print(input_int+5) #출력됨