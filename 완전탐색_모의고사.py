def solution(answers):
    answer = []
    student_1 = [x for x in range(1,6)]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]

    s1 = len(student_1)
    s2 = len(student_2)
    s3 = len(student_3)
    for i, x in enumerate(answers):
        if x == student_1[i%s1]:
            score[0] += 1
        if x == student_2[i%s2]:
            score[1] += 1
        if x == student_3[i%s3]:
            score[2] += 1
    
    m = max(score)
    for i, x in enumerate(score):
        if x == m:
            answer.append(i+1)

    return answer