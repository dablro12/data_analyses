import random
from random import randint


def generate_numbers(n):
    # 여기에 코드를 작성하세요
    generate_numbers_li = []
    for i in range(n):
        generate_numbers_li.append(random.randint(1, 45))
    return generate_numbers_li


def draw_winning_numbers():
    # 여기에 코드를 작성하세요
    generate_numbers_li = generate_numbers(6)
    generate_numbers_li.sort()
    generate_numbers_li.append(random.randint(1,45))
    return generate_numbers_li

def count_matching_numbers(numbers, winning_numbers):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    count = 0
    for i in range(len(winning_numbers)):
        for j in range(len(numbers)):
            if numbers[j] == winning_numbers[i]:
                count += 1
    return count

def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    original_count = 0
    bonus_count = 0
    bonus_numbers = []
    bonus_numbers.append(winning_numbers[-1])

    if len(winning_numbers) == 7:
        original_count =count_matching_numbers(numbers, winning_numbers[:6])  # 보너스제외하고 확인
        bonus_count = count_matching_numbers(numbers, bonus_numbers)  # 보너스번호만 확인
    elif len(winning_numbers) == 6:
        original_count = count_matching_numbers(numbers, winning_numbers)

    if original_count == 6:
        return 1000000000
    elif original_count == 5 and bonus_count == 1:
        return 50000000
    elif original_count == 5:
        return 1000000
    elif original_count == 4:
        return 50000
    elif original_count == 3:
        return 5000
    else:
        return 0