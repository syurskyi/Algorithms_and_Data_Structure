from typing import List

OCR_INPUT = [
    ' _     _  _     _  _  _  _  _ ',
    '| |  | _| _||_||_ |_   ||_||_|',
    '|_|  ||_  _|  | _||_|  ||_| _|',
    '                              ',
]
OCR_WIDTH = 3
OCR_HEIGHT = 4


def split_ocr_numbers(ocr_numbers: List[str]) -> List[List[str]]:
    ocrs_split = []
    len_line = len(ocr_numbers[0])
    for start in range(0, len_line, OCR_WIDTH):
        ocrs_split.append(
            [line[start:start+OCR_WIDTH] for line in ocr_numbers]
        )
    return ocrs_split

OCR_NUMBERS = split_ocr_numbers(OCR_INPUT)


def split_ocr_lines(ocr_numbers: List[str]) -> List[List[str]]:
    ocr_lines = []
    for start in range(0, len(ocr_numbers), OCR_HEIGHT):
        ocr_lines.append(ocr_numbers[start:start+OCR_HEIGHT])
    return ocr_lines


def validate_ocr_numbers(ocr_numbers: List[str]):
    n_first_line = len(ocr_numbers[0])
    if n_first_line % OCR_WIDTH:
        message = str(n_first_line) + ' is not a multiple of ' + str(OCR_WIDTH)
        raise ValueError(message)
    if len(ocr_numbers) % OCR_HEIGHT:
        message = 'numbers of rows is not a multiple of ' + str(OCR_HEIGHT)
        raise ValueError(message)
    if any(len(line) != n_first_line for line in ocr_numbers[1:]):
        raise ValueError('All lines must have the same length.')


def validate_numbers(numbers: str):
    if not numbers.isdigit():
        raise ValueError(numbers + ' is not a digit')


def _convert_ocr_line(ocr_numbers: List[str]) -> str:
    ocrs_split = split_ocr_numbers(ocr_numbers)
    numbers = [
        str(OCR_NUMBERS.index(ocr)) if ocr in OCR_NUMBERS else '?'
        for ocr in ocrs_split
    ]
    return ''.join(numbers)


def number(ocr_numbers: List[str]) -> str:
    validate_ocr_numbers(ocr_numbers)
    return ','.join(
        [_convert_ocr_line(line) for line in split_ocr_lines(ocr_numbers)]
    )


def grid(numbers: str) -> List[str]:
    validate_numbers(numbers)
    ocr_numbers_split = [
        OCR_NUMBERS[int(number)] for number in numbers
    ]
    return [
        ''.join(lines) for lines in zip(*ocr_numbers_split)
    ]


multiline_ocr = [
                " _     _ ",
                " _|  ||_|",
                " _|  ||_|",
                "         ",
                " _     _ ",
                " _|  ||_|",
                " _|  ||_|",
                "         ",
]
assert number(multiline_ocr) == '318,318'


