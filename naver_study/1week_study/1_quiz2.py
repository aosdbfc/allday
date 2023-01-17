sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
    #TODO
    str1 = sentence[31 : ]
    str2 = sentence[25:30]
    str3 = sentence[22:24]
    str4 = sentence[20]
    str5 = sentence[15:19]
    str6 = sentence[9:14]
    str7 = sentence[6:8]
    str8 = sentence[4]
    str9 = sentence[0:3]
    sentence = str1 +" "+ str2 + " " + str3+ " " + str4 + " " + str5 + " " + str6 + " " + str7 + " " + str8 + " " + str9
    return sentence
    # print(str1 +" "+ str2 + " " + str3+ " " + str4 + " " + str5 + " " + str6 + " " + str7 + " " + str8 + " " + str9)
    
print(reverse_sentence(sentence))