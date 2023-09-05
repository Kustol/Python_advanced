import argparse
import logging

LOG_FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(filename='date_checker.log', filemode='a', encoding='utf-8', level=logging.INFO,
                    format=LOG_FORMAT, style='{')
logger = logging.getLogger(__name__)

def is_leap_year(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def validate_date(date_str: str) -> bool:
    if date_str is None:
        logger.error('Date is not provided')
        return False

    try:
        day, month, year = map(int, date_str.split('.'))
    except ValueError as e:
        logger.error(f'Failed to parse the date string! Error: {e}')
        raise ValueError(e)

    if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
        return False

    if (month not in (4, 6, 9, 11) or day <= 30) and (month != 2 or day <= 29 or not is_leap_year(year)) and (
            month != 2 or day <= 28 or is_leap_year(year)):
        logger.info(f'Date: {date_str} is valid')
        return True

    return False



def parse_date():
    parser = argparse.ArgumentParser(prog='check_date',
                                     description='Check if the input date string is valid',
                                     epilog='Date example: 01.01.10000')
    parser.add_argument('-d', '--date', help='Date to check', type=str)
    args = parser.parse_args()
    return validate_date(args.date)

if __name__ == '__main__':
    print(parse_date())

