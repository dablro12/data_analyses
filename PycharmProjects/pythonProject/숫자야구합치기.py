from random import randint


def generate_numbers():
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers: #같은 숫자가 안나오게
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    # 지난 실습의 코드를 여기에 붙여 넣으세요
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

#점수 계싼
def get_score(guesses, solution):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
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


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
# 여기에 코드를 작성하세요
while True:
    strike_cnt, ball_cnt = get_score(take_guess(), ANSWER)
    if strike_cnt == 3:
        print("{}S {}B\n".format(strike_cnt, ball_cnt))
        break
    else:
        print("{}S {}B\n".format(strike_cnt, ball_cnt))


    tries += 1

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
