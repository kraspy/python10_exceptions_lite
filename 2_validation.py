def validate_user_input(data):
    print(f'{data=}')
    if not type(data) is dict:
        raise TypeError('Значение должно иметь тип: dict')
    if 'name' not in data:
        raise ValueError('Словарь должен иметь ключ "name".')
    if 'age' not in data and data['age'] < 0:
        raise ValueError('Словарь должен иметь ключ "age" и его значение должно быть положительным числом.')
    print('OK')
    return True


try:
    validate_user_input({'name': 'Alice', 'age': 30})
except (ValueError, TypeError) as e:
    print(f'Error {e}')

try:
    validate_user_input({'age': 30})
except (ValueError, TypeError) as e:
    print(f'Error {e}')

try:
    validate_user_input({'name': 'Alex', 'age': -30})
except (ValueError, TypeError) as e:
    print(f'Error {e}')

try:
    validate_user_input('abc')
except (ValueError, TypeError) as e:
    print(f'Error {e}')
