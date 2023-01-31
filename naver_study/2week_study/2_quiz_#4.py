# 4 
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
        for j in range(len(data)):   #각 row 을 읽기 위한 반복문 
            data[j] = [int(i) for i in data[j]] # int 와 str 합 오류 방지
            self.data = data
        return self.data
             
    def merge_list(self):
        return [sum(i) for i in self.data]

# 출력 예시
read_csv = ReadCSV(file_path)
pprint.pprint(read_csv.read_file())
print(read_csv.merge_list())