import random

while True :
    x = random.randint( 1, 100)
    y = random.randint( 1, 100)
    print( x , '+', y ,    '=',   end =   '    ')
    answer = int(input())
    if answer == x + y :
        print( ' 정답입니다.')
    else :
        print(' 다시 시도하세요.') 
