# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
#result3 = [elem for elem in range(20, 241) if elem % 20 == 0 or elem % 21 == 0]
#print(result3)
print([elem for elem in range(20, 241) if elem % 20 == 0 or elem % 21 == 0])