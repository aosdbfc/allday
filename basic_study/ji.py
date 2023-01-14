class Student(object): #클래스 객체를 선언한다.
    def __init__(self, name, major, age, gender): #__init__으로 4가지 인자를 계속 초기화하는 함수를 실행한다.
        self.name = name #name 인자 선언
        self.major = major #major 인자 선언
        self.age = age   # age 인자 선언
        self.gender = gender # genger 인자 선언 


class StudentManagerSystem(object): # 객체를 받아오기 위한 클래스를 선언한다. 
    def __init__(self): #초기화하는 함수 선언
        self.students = {} #학생 object 인자 선언 

    def addStudent(self, name, major, age, gender): #학생 정보에 필요한 4가지 인자를 입력하는 함수를 선언한다. (추가부분)
        student = Student(name, major, age, gender) #student 변수에 4가지 인자를 저장
        self.students.update({name: student}) # 학생정보 새 수정은 이름 인자를 이용하도록 한다. 

    def removeStudent(self, name): #객체 삭제도 필요하기 때문에 name 인자로 삭제하는 함수를 선언한다. 
        try:
            del self.students[name]  # 존재하는 이름이면 본 class에서 삭제
        except:
            print("존재하지 않는 이름입니다.") #존재하지 않는 이름이면 "존재하지 않는 이름입니다"를 출력한다. 
    
    def printStudentInfo(self, name):   # 이름인자로 학생 정보를 출력하는 함수를 선언한다. 
        print("이름 :\t",  self.students[name].name) # 이름 정보를 출력하는 print 문에 class에 저장된 이름 정보 출력 
        print("전공 :\t",  self.students[name].major) # 전공 정보를 출력하는 print문에 class에 저장된 전공 정보 출력 
        print("나이 :\t",  self.students[name].age) # 나이 정보를 출력하는 print 문에 class에 저장된 나이 정보 출력 
        print("성별 :\t",  self.students[name].gender) # 성별 정보를 출력하는 print 문제 class에 저장된 성별 정보 출력 
 
    def printStudentsInfo(self): # class에 저장된 전체 학생 정보를 출력하는 함수를 선언한다. 
        for student_stat in self.students.values(): # for ~ in 문으로 학생의 정보를 배열화한다. 
            print(20 * "-") # -를 20번 출력 
            print("이름 :\t",  student_stat.name) # 배열화 된 student_stat에 저장된 이름 정보 출력 
            print("전공 :\t",  student_stat.major) # 배열화 된 student_stat에 저장된 전공 정보 출력 
            print("나이 :\t",  student_stat.age)  # 배열화 된 student_stat에 저장된 나이 정보 출력 
            print("성별 :\t",  student_stat.gender) # 배열화 된 student_stat에 저장된 성별 정보 출력 
            print(20 * "-") # - 20번 출력 


def main(): #처음 학생의 정보를 받아오거나 출력하는 main() 함수 선언 
    system = StudentManagerSystem() # system이라는 변수로 설정한다. 
    while True:  # 무한 반복문으로 main() 이라는 함수 시스템에서 어떤 기능을 할지 선언하도록 한다. 
        print("1. 학생 등록") # 1. 학생 등록이라는 문자 출력
        print("2. 학생 삭제") # 2. 학생 삭제라는 문자 출력 
        print("3. 학생 정보 출력") # 3. 학생 정보 출력이라는 문자 출력
        print("4. 전체 학생 정보 출력") # 4. 전체 학생 정보라는 문자 출력 
        print("0. 종료\n") # 0를 선택하면, 종료라는 문자 출력 
        select_number = int(input("원하는 기능을 선택하세요 : ")) # 사용자에게 원하는 기능을 선택하도록 input 함수 선언 
        if select_number == 0 : # 1~4 외에 0를 입력하면 , 
            print("시스템을 종료합니다") # 시스템을 종료합니다라는 문자 출력 
            break    # break로 무한 반복문를 벗어난다. 

        if select_number == 1: # 1 입력할 때, 
            print("----- 학생 등록 ----") # -----학생등록-----이라는 문자 출력 
            name = input("이름 :\t") # 사용자에게 이름을  입력받도록 한다  
            major = input("전공 :\t") # 사용자에게 전공을 입력 받도록 한다 
            age = input("나이 :\t")  # 사용자에게 나이를 입력 받도록 한다 
            gender = input("성별 :\t") # 사용자에게 성별을 입력 받도록 한다 
            system.addStudent(name, major, age, gender) # 사용자에게 받은 정보를 addStudent class에 객체화 한다. 
            print(20 * "-"+"\n")  # - 를 20번 출력 

        elif select_number == 2: # 2를 입력할 때, 
            print("----- 학생 삭제 ----") # ----- 학생 삭제 ---- 라는 문자 출력 
            name = input("이름 :\t") # 사용자에게 이름을 입력받도록 한다. 
            system.removeStudent(name) # 사용자에게 받은 이름 정보를 removeStudent class로 삭제하도록 한다. 
            print(20 * "-"+"\n") # -를 20번 출력 

        elif select_number == 3: # 3 입력할 때, 
            name = input("이름 :\t") # 사용자에게 이름을 입력받도록 한다. 
            print("----- 학생 정보 출력 ----") # -----학생 정보 출력 ---- 이라는 문자 출력 
            system.printStudentInfo(name) # printStudentinfo에서 이름이라는 인자를 받아 그 이름에 대한 학생 정보 출력 
            print(25 * "-"+"\n") # -를 25번 출력 

        elif select_number == 4: # 4 입력할 때, 
            print("= 전체 학생 정보 출력 =") # =전체 학생 정보=라는 문자 출력 
            system.printStudentsInfo() # printStudentsinfo에 저장되어 있는 전체 학생 정보를 출력하도록 한다. 
            print(20 * "-"+"\n") # -를 20번 출력 
        else:
            print("지원하지 않는 기능을 선택했습니다. \n") # 0~4 숫자 외에 다른 숫자 입력 시 지원하지 않는 기능을 선택했습니다 출력 (예외처리)

main() # main 이라는 메소드에서 실행됨을 알려준다. 
