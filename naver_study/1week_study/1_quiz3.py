score = [(100,100),(95,90),(55,60),(75,80),(70,70)]

def get_avg(score):
    # TODO
    for i , j in enumerate(score):
        print("{} 번, 평균 : {}".format(i+1,sum(j)/2))

get_avg(score)