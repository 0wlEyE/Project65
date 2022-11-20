"""DAY"""
def days():
    """2011"""
    date = int(input())
    month = int(input())
    date_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date_in_month = sum(date_of_month[:month-1]) + date
    day = date_in_month % 7
    if day == 1:
        print("Saturday")
    elif day == 2:
        print("Sunday")
    elif day == 3:
        print("Monday")
    elif day == 4:
        print("Tuesday")
    elif day == 5:
        print("Wednesday")
    elif day == 6:
        print("Thursday")
    else:
        print("Friday")
days()
