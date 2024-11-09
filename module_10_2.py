import threading
import time


class Knight(threading.Thread):

    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.days_of_battle = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        number_of_enemies = 100

        while number_of_enemies > 0:
            if number_of_enemies >= self.power:
                number_of_enemies -= self.power
            else:
                number_of_enemies = 0

            time.sleep(1)
            self.days_of_battle += 1
            print(f"{self.name} сражается {self.days_of_battle} день(дня)..., осталось {number_of_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days_of_battle} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
