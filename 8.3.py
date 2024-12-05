def contract(fn, *types):
    def wrapper(*args):
        # Проверяем типы аргументов
        for i, (arg, expected_type) in enumerate(zip(args, types[:-1])):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Argument {i} expected type {expected_type.__name__}, but got {type(arg).__name__}")
        
        # Выполняем функцию
        result = fn(*args)

        # Проверяем тип результата
        if not isinstance(result, types[-1]):
            raise TypeError(f"Result expected type {types[-1].__name__}, but got {type(result).__name__}")
        
        return result
    return wrapper


# Пример 1: сложение чисел
def add(a, b):
    return a + b

add_numbers = contract(add, int, int, int)
res = add_numbers(2, 3)
print(res)  # Вывод: 5

# Пример 2: конкатенация строк
def concat(s1, s2):
    return s1 + s2

concat_strings = contract(concat, str, str, str)
res = concat_strings("Hello ", "world!")
print(res)  # Вывод: Hello world!
