# 3
# 라이브러리 불러오기
import csv 
import pprint

file_path = "./data-01-test-score.csv"

# f 라는 변수에 데이터셋 open
f = open("./data-01-test-score.csv")
data = csv.reader(f) # data 변수에 csv.reader 할당 

for row in data: # data 각 row을 하나씩 print 
    print(row)

f.close()
file_path = "./data-01-test-score.csv"