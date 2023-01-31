# 5
# 라이브러리 불러오기
import csv
import pprint

file_path = "./data-01-test-score.csv" #데이터 경로 file_path 변수에 할당 

class ReadCSV(object):  # 클래스 
    def __init__(self, file_path) :   #초기화
         self.file_path = file_path  # file_path 불러오기 
        
    def read_file(self): # 파일을 읽기위한 정규문자 r 사용
        f = open("./data-01-test-score.csv")  
        data = list(csv.reader(f))
        for j in range(0, len(data)):   #각 row 을 읽기 위한 반복문 
            data[j] = [int(i) for i in data[j]]
            self.data = data
        return self.data # return이 어디에 indent 되냐에 따라 str 변수가 될수도 있고 int가 될수도?? (질문사항)
            
    def merge_list(self): # 4번에서 merge_list 수정 
        sum_list = [sum(i) / len(i)for i in self.data] # 각 평균을 sum_list에 할당 
        return sorted(sum_list) # 오름차순으로 정리 

read_csv =ReadCSV(file_path)
pprint.pprint(read_csv.read_file())
print(read_csv.merge_list())