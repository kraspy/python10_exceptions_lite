class NegativeNumberError(Exception):
    def __init__(self, value, message):
        super().__init__(message)
        self.value = value

    def __str__(self):
        return f'Error ({self.value}): {self.message}'


def check_positive_number(number: int | float):
    if number < 0:
        raise NegativeNumberError(number, 'Число должно быть положительным!')
    return True


print(check_positive_number(1))
print(check_positive_number(-1))
