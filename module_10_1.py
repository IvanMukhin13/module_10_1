import time
from time import sleep
from threading import Thread

time_start = time.time()


def write_word(word_count: int, file_name):
    """
    Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
    с прерыванием после записи каждого на 0.1 секунду.
    :param word_count: количество записываемых слов
    :param file_name: название файла, куда будут записываться слова
    :return: "Какое-то слово № <номер слова по порядку>"
    """
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(1, word_count + 1):
        file.write(f'Какое-то слово № {i}')
        file.write('\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


write_word(10, 'example1')
write_word(30, 'example2')
write_word(200, 'example3')
write_word(100, 'example4')

time_end = time.time()
res_time = time_end - time_start
print(f'Работа потоков: {res_time}')

thr_fifth = Thread(target=write_word, args=(10, 'example5'))
thr_sixth = Thread(target=write_word, args=(30, 'example6'))
thr_seventh = Thread(target=write_word, args=(200, 'example7'))
thr_eighth = Thread(target=write_word, args=(100, 'example8'))

thr_fifth.start()
thr_sixth.start()
thr_seventh.start()
thr_eighth.start()

thr_eighth.join()
thr_seventh.join()
thr_sixth.join()
thr_fifth.join()

time_end_2 = time.time()
res_time = time_end_2 - time_end
print(f'Работа потоков: {res_time}')
