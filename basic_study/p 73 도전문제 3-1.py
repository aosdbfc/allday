second = int(input("초를 입력하세요 ;    "))
hours = second // 3600
minutes = (second % 3600 ) // 60
seconds = minutes % 60 

print("입력한 시간은" , hours , " 시간", minutes, "분" , seconds, "초") 
