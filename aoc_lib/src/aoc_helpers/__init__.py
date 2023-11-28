import datetime
import pathlib

import bs4
import requests
from aoc_helpers import credentials

session = credentials.get_session()
storage_dir = pathlib.Path(__file__).parent.parent.parent.parent / 'puzzle_inputs'#credentials.get_storage_dir()

print(storage_dir)

def get_puzzle_lines(day: int, year: int = None, force: bool = False):
    return get_puzzle_input(day, year, force, True)


def get_puzzle_input(day: int, year: int = None, force: bool = False, readlines=False):
    if year is None:
        year = get_year()
    curr_folder = (storage_dir / f'{year:4d}')
    curr_folder.mkdir(exist_ok=True, parents=True)
    filepath = curr_folder / f'input_{day:02d}'

    if not filepath.exists() or force:
        response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': session})

        if not response.ok:
            print(response.content)
            raise Exception()

        storage_dir.mkdir(exist_ok=True)
        with open(filepath, 'w+') as f:
            f.write(response.text)

    with open(filepath, 'r') as f:
        if readlines:
            content = list(map(lambda x: x.strip('\n'), f.readlines()))
        else:
            content = f.read()
    return content


def post_answer(answer: str, day: int, part: int, year: int = None):
    if year is None:
        year = get_year()

    response = requests.post(f'https://adventofcode.com/{year}/day/{day}/answer', cookies={'session': session},
                             data={'level': part, 'answer': answer})
    if not response.ok:
        print(response.content)
        raise Exception()

    soup = bs4.BeautifulSoup(response.content, 'html5lib')
    print(soup.find('main').article.p.text)

    return response


def get_year() -> int:
    now = datetime.datetime.utcnow()
    return now.year if now.month == 12 else now.year - 1
