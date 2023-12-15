#date_converter.py

from datetime import datetime, timedelta
start_date = datetime(2000, 1, 1)
end_date = datetime(2099, 12, 31)
total_days = (end_date - start_date).days + 1

def date_to_code(date):
    """
    Convert a given date to a unique four-letter code.
    """
    days_since_start = (date - start_date).days

    base26 = []
    while days_since_start > 0:
        base26.append(days_since_start % 26)
        days_since_start //= 26

    while len(base26) < 4:
        base26.append(0)

    code = ''.join(chr(97 + digit) for digit in reversed(base26))
    return code

def code_to_date(code):
    """
    Convert a four-letter code back to a date.
    """
    digits = [ord(char) - 97 for char in code]

    days_since_start = 0
    for digit in digits:
        days_since_start = days_since_start * 26 + digit

    date = start_date + timedelta(days=days_since_start)
    return date