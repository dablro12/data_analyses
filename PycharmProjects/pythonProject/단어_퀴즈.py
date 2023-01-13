with open("vocabulary.txt", 'r') as f:
    for line in f:
        voca_list = line.strip().split(": ")
        answer = input("{}: ".format(voca_list[1]))
        if answer == voca_list[0]:
            print("맞았습니다.")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(voca_list[0]))

