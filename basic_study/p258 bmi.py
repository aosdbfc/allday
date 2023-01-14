import numpy as np

heights = [ 1.83 , 1.76 , 1.69 , 1.86 , 1.77 , 1.73]
weights = [ 86 , 74 , 59 , 95 , 80 ,68 ]

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi = np_heights/(np_weights**2)
print('대상자들의 키:', np_heights)
print('대상자들의 몸무게:', np_weights)
print('대상자들의 bmi')
print(bmi)

print()
print(bmi[bmi >25 ]) # bmi가 25가 넘는 사람들 추출 
