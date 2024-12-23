from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, knight, power):
        super().__init__()
        self.knight = knight
        self.power = power
        self.enemies = 100
        self.day = 0

    def run(self):
        print(f"{self.knight} на нас напали!")
        while self.enemies > 0:
            print(f"{self.knight} сражается {self.day} день(дня)..., осталось {self.enemies} воинов.")
            self.enemies -= self.power
            self.day += 1
            sleep(1)
        print(f'{self.knight} одержал победу спустя {self.day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")