# split
my_string = "1. 2. 3. 4. 5. 6"
#print(my_string.split(".")) #->['1', ' 2', ' 3', ' 4', ' 5', ' 6']
#split("구분자")는 문자열을 리스트로 만들어줌
#띄워쓰기가 남아있는 것을 알 수 있음 이를 바꿔주기
print(my_string.split(". "))

full_name = "Kim, Yuna"
name_data = full_name.split(", ") #->['Kim', 'Yuna']
first_name = name_data[0]
last_name = name_data[1]

print(first_name)
print(last_name)

print("     \n\n 2 \t \n        5       7 11 \n".split()) #->['2', '5', '7', '11']
#split으로 return 된 값은 '문자열'이므로 주의!
numbers = "     \n\n 2 \t \n        5       7 11 \n".split()
print(int(numbers[0])+int(numbers[1]))