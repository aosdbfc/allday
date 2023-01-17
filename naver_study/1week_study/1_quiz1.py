# 주어진 리스트
num_list = [1,5,7,15,16,22,28,29]

def get_odd_num(num_list):
    #TODO
    a = []
    for i in num_list :
        if i % 2 == 0 :
            pass 
        else :
            a.append(i)
    return a
    
print(get_odd_num(num_list))