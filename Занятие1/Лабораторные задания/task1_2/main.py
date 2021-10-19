# Напишите ваше решение
NALOG = 13

oklad = int(input('Введите размер оклада: '))
pod_nal = oklad / 100 * NALOG
na_ruki = oklad - pod_nal

print('Размер подоходного налога:', pod_nal)
print('Размер зарплаты за вычетом подоходного налога:', na_ruki)