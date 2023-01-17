import re 

inputs = input('출력 예시 : ')

def find_string(inputs) :
    #TODO
    bin_list = []
    str = re.sub("[0-9]+"," ", inputs)
    bin_list =str.split()
    
    return " ".join(bin_list).split()
    
print(find_string(inputs))