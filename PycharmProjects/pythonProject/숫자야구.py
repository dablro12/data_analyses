from random import randint

#자동생성 함수
def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers: #같은 숫자가 안나오게
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

#숫자 3개 입력 함수
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 여기에 코드를 작성하세요
    i =1
    while len(new_guess) < 3:
        number = int(input("{}번째 숫자를 입력하세요: ".format(i)))
        if number < 0 or number > 10:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(number)
        i += 1

    return new_guess

#점수 계산 함수
#스트라이크 수와 볼 수 를 알려줌
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    guesses_li = guesses
    solution_li = solution
    # 여기에 코드를 작성하세요
    for i in range(len(guesses_li)):
        if guesses_li[i] == solution_li[i]:
            strike_count += 1
        elif guesses_li[i] in solution_li:
#            if guesses_li[i] != solution_li[i]: #굳이 안해도된다 if문에서 먼저 걸리지 않으면 나머지 index에 대해 비교하므로
                ball_count += 1


    return strike_count, ball_count

# 테스트 코드
#print(generate_numbers())
#print(take_guess())
#s_1, b_1 = get_score([2, 7, 4], [2, 6, 3])
#print(s_1, b_1)
#s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
#print(s_2, b_2)
#s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
#print(s_3, b_3)
#s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
#print(s_4, b_4)

