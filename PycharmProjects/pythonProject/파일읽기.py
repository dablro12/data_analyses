#chicken.txt가 같은 폴더에 있기에 가능한 것
#with open('파일이 있는 경로', 'r') 읽기모드로 읽기
#with open('data/chicken.txt', 'r') as f:
#    for line in f:
#        print(line) # 한줄씩 출력

#1일: 453400\n 이 txt에 저장되어있어서 \n을 처리 해주어야 함
#strip() : 문자열에서 앞 뒤에 있는 화이트 스페이스(공백) 들을 제거해줌
print("       abc     def         ".strip()) #-> abc     def
print("    \t   \n  abc     def\n\n\n      ".strip()) #-> abc     def

#위 파일을 적용해보자
with open('data/chicken.txt', 'r') as f:
    for line in f:
        print(line.strip())  # 한줄씩 출력되어 화이트 스페이스가 없어짐을 알 수 있음