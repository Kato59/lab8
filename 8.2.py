def store(value):
    def read():
        return value
    return read


# Пример использования:
read = store(5)
value = read()
print(value)  # Вывод: 5
