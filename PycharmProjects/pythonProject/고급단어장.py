import random #random함수 import

with open("vocabulary.txt", 'r') as f:
    voca_dict = {}
    for line in f:
        voca_list = line.strip().split(": ")
        voca_dict[voca_list[0]] = voca_list[1]
#    q = False
#    while True:


    q = True
    while q != False:
        #목록가져오기

        correct_answer_eng, question_kor = random.choice(list(voca_dict.items()))  # key를 list로 반환하면 할 수 있음
        answer_enq = input("{}: ".format(question_kor))

        if answer_enq == correct_answer_eng:
            print("맞았습니다!")
        elif answer_enq == "q":
            q = False
        else:
            print("틀렸습니다. 정답은 {}입니다.".format(correct_answer_eng))
