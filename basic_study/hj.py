class Student:
    def __init__(self, n, m, a, g):
        self.name = n
        self.major = m
        self.age = a
        self.gender = g

class StudenManageSystem:
    def __init__(self):
        self.students = {}

    def addStudent(self, s):
        self.students[s.name] = s

    def removeStudent(self, n):
        del self.students[n]

    def printStudentInfo(self, n):
        student = self.students[n]
        print('----- 학생 정보 출력-----')
        print('이름 :\t', student.name)
        print('전공 :\t', student.major)
        print('나이 :\t', student.age)
        print('성별 :\t', student.gender)
        print('----------')

    def printStudentsInfo(self):
        print('\n= 전체 학생 정보 출력 =')
        for student in self.students.values():
            print('-----------------------')
            print('이름 :\t', student.name)
            print('전공 :\t', student.major)
            print('나이 :\t', student.age)
            print('성별 :\t', student.gender)
            print('-----------------------')

sms = StudenManageSystem()
sms.addStudent(Student('박찬호', '야구', 49, 'M'))  # 학생 등록
sms.addStudent(Student('박지성', '축구', 36, 'M'))  # 학생 등록
sms.addStudent(Student('김연경', '배구', 25, 'W'))  # 학생 등록
sms.addStudent(Student('박세리', '골프', 48, 'M'))  # 학생 등록
sms.addStudent(Student('손흥민', '축구', 31, 'M'))  # 학생 등록

sms.printStudentInfo('박찬호')    # 학생 검색 및 출력
sms.printStudentInfo('박세리')    # 학생 검색 및 풀력

sms.printStudentsInfo()  # 전체 학생 출력
sms.removeStudent('박찬호') # 학생 삭제
sms.removeStudent('김연경') # 학생 삭제
sms.removeStudent('박세리') # 학생 삭제
sms.printStudentsInfo()  # 전체 학생 출력
