""" QUEENBEE: github.com/entr0pie/QUEENBEE """
# Date: 2022-10-20
# Source: https://www.beecrowd.com.br/judge/pt/problems/view/1129
# Author: entr0pie
# Contact: <github.com/entr0pie>
# Name: BEE 1129

while True:
    questions = int(input(""))
    if questions == 0:
        break

    alternatives = ('A', 'B', 'C', 'D', 'E')

    for qst in range(questions):
        answer = input("").split(' ')

        marked_question = []
        
        for asw in answer:
            if int(asw) <= 127:
                marked_question.append(answer.index(asw))

        
        if len(marked_question) == 0 or len(marked_question) > 1:
            print("*")
        
        else:
            print(alternatives[marked_question[0]])