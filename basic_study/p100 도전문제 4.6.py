age = int(input(" 나이를 입력하시오:     "))
if age >= 15 :
    print(" 본 영화를 보실 수 있습니다.")
    print(" 영화의 가격은 10000원 입니다.")
    print(" 할인 , 적립이 있으신가요? ")

else :
    print(" 영화를 보실 수 없습니다.")
    print(" 다른 영화를 보시겠어요?")


card = input("교통카드 종류는 무엇인가요?(청소년, 성인)")

if card == "청소년" :
    print("청소년 입니다.")
else : 
    print(" 승인되었습니다.")
    
