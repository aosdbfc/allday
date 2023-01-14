num = int(input(" 정수를 입력하시오:   "))
if num < 0 :
    print("음수 입니다")
else :
    print("양수입니다.")
    if num & 2 == 0 :
        print(" 짝수 입니다.")
    else :
        print("홀수 입니다.")
