dict_first = {'사과':30, '배':15, '감':10, '포도':10}
dict_second = {'사과':5, '감':25, '배':15, '귤':25}

def merge_dict(dict_first, dict_second):
    for key in dict_second:
        if key in dict_first:
            dict_first[key] += dict_second[key]
        else:
            dict_first[key] = dict_second[key]

    dict_second.update(dict_first)
    
    dict_second = dict(sorted(dict_second.items()))
    print(dict_second)

    

print(merge_dict(dict_first, dict_second))
