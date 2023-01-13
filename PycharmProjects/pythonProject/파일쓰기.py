#쓰기 기능을 사용하고 싶으면 w , 추가하고 싶으면 a
with open('new_file.txt', 'a') as f:
    f.write("Hello World!\n")
    f.write("My name is daehyeon\n")
#new_file이 project 디렉토리 내에 생긴 것을 알 수 있다.
#줄바꿈이 안됨 \n을 이용
