from time import sleep
import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            line = f'Какое-то слово № {i}\n'
            f.write(line)
            sleep(0.1)
        print(f'Завершилась запись в {file_name}')


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time() - start_time
print(f'Работа потоков: {end_time:.6f} сек.')

thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = Thread(target=write_words, args=(100, 'example8.txt'))

start_time = time.time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time = time.time() - start_time
print(f'Работа потоков: {end_time:.6f} сек.')
