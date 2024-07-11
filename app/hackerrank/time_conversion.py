"""
https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
Simplifies Hour Conversion:

hr % 12 handles the conversion of hour 12 to 0.
(period == 'PM') * 12 adds 12 if the period is PM.
"""


def my_way(s):
    time, am_pm = s[:-2], s[-2:]
    hr, _min, sec = time.split(':')
    if am_pm == 'PM':
        if int(hr) < 12:
            print(f'{int(hr) + 12}:{_min}:{sec}')
        else:
            print(f'{hr}:{_min}:{sec}')
    else:
        if int(hr) == 12:
            print(f'00:{_min}:{sec}')
        else:
            print(f'{hr}:{_min}:{sec}')


def optimize_from_gpt(s):
    time, am_pm = s[:-2], s[-2:]
    hr, _min, sec = time.split(':')

    hr = int(hr)

    if am_pm == 'PM' and hr != 12:
        hr += 12
    elif am_pm == 'AM' and hr == 12:
        hr = 0

    return f'{hr:02}:{_min}:{sec}'


def convert_to_24_hour_format1(s):
    time, period = s[:-2], s[-2:]
    hr, _min, sec = map(int, time.split(':'))

    hr = (hr % 12) + (period == 'PM') * 12

    return f'{hr:02}:{_min:02}:{sec:02}'


def convert_to_24_hour_format(s):
    """
    Explanation:
        Lambda Function:
            The lambda function now takes four arguments: the hour (h),the minutes (m), the seconds (s), and the period.
            The hour conversion is performed with (h % 12 + (period == "PM") * 12).
        String Formatting:
            The formatted string f'{...:02}:{s[3:5]}:{s[6:8]}' ensures that the hour is two digits and directly includes
            the minutes and seconds from the input string.
    """
    return f'{(lambda h, m, sec, period: (h % 12 + (period == "PM") * 12))(int(s[:2]), s[3:5], s[6:8], s[-2:]):02}:{s[3:5]}:{s[6:8]}'


# Example usage
s = '12:01:00AM'
print(convert_to_24_hour_format(s))  # Expected output: 00:01:00
s = '01:01:00AM'
print(convert_to_24_hour_format(s))  # Expected output: 01:01:00
s = '12:01:00PM'
print(convert_to_24_hour_format(s))  # Expected output: 12:01:00
s = '01:01:00PM'
print(convert_to_24_hour_format(s))  # Expected output: 13:01:00
