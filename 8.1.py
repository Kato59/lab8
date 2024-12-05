def iterate(obj, callback):
    for key, value in obj.items():
        callback(key, value, obj)


# Пример использования:
obj = {"a": 1, "b": 2, "c": 3}
iterate(obj, lambda key, value, obj: print({"key": key, "value": value}))
# Вывод:
# {'key': 'a', 'value': 1}
# {'key': 'b', 'value': 2}
# {'key': 'c', 'value': 3}
