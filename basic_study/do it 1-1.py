# 세 정수를 입력받아 최댓값 구하기
print()
print('세 정수의 최대값을 구합니다')

a = int(input(' 정수 a의 값을 입력하세요: '))
b = int(input(' 정수 b의 값을 입력하세요: '))
c = int(input(' 정수 c의 값을 입력하세요: '))

max = a
if b > max : max = b
if c > max : max = c
print()
print(f'최댓값은 {max}입니다')
