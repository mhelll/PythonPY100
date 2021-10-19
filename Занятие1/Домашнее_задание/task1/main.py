# Напишите ваше решение
speed_ = int(input('Скорость передачи данных: ')) / 1024 / 1024 / 1024
time_ = int(input('Время скачивания игры: ')) * 60

game_size = int(speed_ * time_)

print(game_size, 'Gb')

coast = int(input('Цена за Gb: '))

print('Цена за скачивание:', coast * (game_size - 1), 'рублей')