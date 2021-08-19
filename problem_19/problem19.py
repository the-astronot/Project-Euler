'''
PROBLEM 19:

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''


def run():
    sum = 0
    current_year = 1901
    end_year = 2001
    day_index = 2
    while current_year != end_year:
        for i in range(12):
            if day_index == 0:
                sum += 1
            delta = months[i]
            if i == 1:
                # All hell breaks loose
                if current_year % 4 == 0:
                    delta += 1
                if current_year % 100 == 0:
                    delta -= 1
                if current_year % 400 == 0:
                    delta += 1
            day_index = (day_index + delta) % 7
        current_year += 1
    print("{} Sundays occurred on the first of the month over that period"\
          .format(sum))

days = ["Su", "Mo", "Tu", "Wd", "Th", "Fr", "Sa"]
months = [31,28,31,30,31,30,31,31,30,31,30,31]


if __name__ == '__main__':
    run()
