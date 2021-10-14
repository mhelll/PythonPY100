# Напишите ваше решение
NALOG = 13

oklad = int(input("Размер оклада: "))

razmernaloga = oklad // 100 * NALOG
print("Подоходный налог: ", razmernaloga)

naruki = oklad - razmernaloga
print("Зарплата на руки: ",naruki)

