for i in range(13):
    num_of_month = int(input())

    if num_of_month > 12:
        print("Wrong number")
    elif num_of_month <= 2 or num_of_month == 12:
        print("Winter")
    elif num_of_month >= 3 and num_of_month <= 5:
        print("Spring")
    elif num_of_month >= 6 and num_of_month <= 8:
        print("Summer")
    elif num_of_month >= 9 and num_of_month <= 11:
        print("Autumn")
