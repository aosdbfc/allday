# RFM 상대적 지방 질량

gender = int(input("여성이면 1 남성이면 0을 입력하시오:   "))
height = float(input("당신의 키는 얼마 입니까? :     "))
weight = float(input(" 당신의 허리 둘레는 얼마 입니까?:    "))
RFM = 64 - ( 20 * ( height  /  weight ) ) + 12 * gender
print(" 당신의 RFM은" , RFM , "입니다.") 
