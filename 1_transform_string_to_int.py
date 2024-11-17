import logging
from logging import StreamHandler, FileHandler

file_handler = FileHandler('file.log', encoding='utf-8')
stream_handler = StreamHandler()

logging.basicConfig(
    handlers=[file_handler, stream_handler],
    encoding='utf-8',
)


def convert_to_int(string: str) -> int:
    print(f'*** Преобразование значения "{string}" в число')
    integer: int = 0
    transform_success = False
    try:
        integer = int(string)
        transform_success = True
    except ValueError as e:
        logging.error(f'Ошибка значения: {e}')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
    finally:
        print(
            'Преобразование строки прошло успешно' if transform_success else 'Во время преобразования произошла ошибка'
        )

    return integer


print(convert_to_int('123'))
print(convert_to_int('abc'))
print(convert_to_int([1, 2, 3]))
