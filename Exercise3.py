def calculate_future_hour():
    hour = int(input("Enter hour: "))
    am_pm = int(input("am (1) or pm (2)? "))
    hours_ahead = int(input("How many hours ahead? "))

    total_hours = hour + hours_ahead
    new_hour = total_hours % 12

    if am_pm == 1 and total_hours >= 12:
        am_pm = 2
    elif am_pm == 2 and total_hours >= 12:
        am_pm = 1

    if am_pm == 1:
        p = "am"
    else:
        p = "pm"

    print("New hour: {} {}".format(new_hour, p))


calculate_future_hour()
