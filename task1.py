from pathlib import Path
from random import randint, choice

WOVES = 'аеёиоуыэюя'
CONSTANTS = 'бвгджзклмнпрстфхцчщ'


def get_name(extension: str, min_len_name: int = 6, max_len_name: int = 30, min_len_bytes: int=256,
             max_len_bytes: int = 4096, count_files = 42):
    global rad_strong
    for _ in range(count_files):
        rad_strong = ''.join(choice(WOVES)) if i % 3 == 0 else choice(CONSTANTS)
                for i in range(randint(min_len_name, max_len_name))
        data = bytes(randint(0, 255) for _ in range(min_len_bytes, max_len_bytes))
        with open(f'{rad_strong}.{extension}', 'wb') as f:
            f.write(data)

