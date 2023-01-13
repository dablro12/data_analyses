import random

chance_count = 4
correct_answer = random.randint(1,20)
i = 0
while i < 4:
    select_int = int(input("기회가 {}번 남았습니다. 1~20 사이의 숫자를 맞혀보세요: ".format(chance_count)))
    if select_int == correct_answer:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(i))
        break
    elif select_int > correct_answer:
        print("Down")
    else:
        print("Up")
    i += 1
    chance_count -= 1
print("아쉽습니다. 정답은 {}였습니다.".format(correct_answer))