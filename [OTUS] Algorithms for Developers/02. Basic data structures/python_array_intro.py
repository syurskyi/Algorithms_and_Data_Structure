import array

"""
built-in list() - встроенный тимп данных, написан на C (для cpython). Реализован 
как _динамический массив_, позволяет хранить ссылки на объекты разного типа и размера.
Код находится здесь https://github.com/python/cpython/blob/master/Objects/listobject.c

Важная часть кода на C - объявление list() - https://hg.python.org/cpython/file/tip/Include/listobject.h#l22

Использование списка - 
"""
my_list = [1, 2, "3"]
print("my_list: {}".format(my_list))

another_list = list("123")
print("another_list: {}".format(another_list))


"""
array - написан тоже на C. Находится в стандартной бибилиотеке, но является модулем.
Отличается тем, что оптимизирован под хранение массивов элементов одного типа - более производителен и экономен.
Ссылка: https://github.com/python/cpython/blob/master/Modules/arraymodule.c

Используется примерно так:
>>> my_arr = array.array('l', [1, 2, 3, 4, 5])

Поскольку массив - низкоуровневая структура данных, а python - высокоуровневый язык, на нем самом
реализовывать массив бессмысленно.
"""


my_arr = array.array('l', [1, 2, 3, 4, 5])
print("my_arr: {}".format(my_arr))

"""
Есть еще numpy.array() из библиотеки numpy, но это тема для отдельного разговора - он используется
в основном для "научных" вычислений.
"""
