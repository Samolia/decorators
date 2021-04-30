from application import my_fibonacci, area_of_a_rectangle, create_cook_book_from_file


def main():
    my_fibonacci(77, file_name='my_logger.txt', text='Число последовательности Фибоначчи стоящее на позиции')

    area_of_a_rectangle(5, 3, file_name='my_logger.txt', text='Площадь прямоугольника со сторонами')

    create_cook_book_from_file('data/recipes.txt', file_name='my_logger.txt',
                               text='Принимает имя файла')


if __name__ == '__main__':
    main()
